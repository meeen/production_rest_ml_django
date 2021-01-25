from django.shortcuts import render
from .models import production, machine, tool_change, order
from .serializers import production_serializer, machine_serializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle

# Create your views here.

class ProductionViewSet(viewsets.ModelViewSet):
    queryset = production.objects.all()
    serializer_class = production_serializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = machine.objects.all()
    serializer_class = machine_serializer

    @action(detail=True, methods=['GET'])
    def build_model(self,request,pk=None):
        
        thismachine = machine.objects.get(id=pk)
        product_data = production.objects.filter(machine=thismachine)

        x1 = []
        x2 = []
        y = []

        for product in product_data:
            x1.append(product.tooltime)
            x2.append(product.machinetime)
            y.append(product.tolarance)

        
        product_to_df = {'tool_runtime':x1,'machine_runtime':x2,'tolerance':y}
        df_product = pd.DataFrame.from_dict(product_to_df)
        X = df_product[['tool_runtime', 'machine_runtime']]
        Y = df_product[['tolerance']]

        new_model = RandomForestRegressor(n_estimators=200, random_state=0)
        new_model.fit(X,Y.values.ravel())
        model_byte = pickle.dumps(new_model)
        thismachine.model = model_byte
        thismachine.save()
        data = {"message":"success"}
        return Response(data, status=200)

    
    @action(detail=True, methods=['POST'])
    def make_prediction(self,request,pk=None):
        thismachine = machine.objects.get(id=pk)
        model = pickle.loads(thismachine.model)
        product_data_pre = {'tool_runtime':[request.data['tooltime']],'machine_runtime':[request.data['machinetime']]}
        product_data_df = pd.DataFrame.from_dict(product_data_pre)
        predicted = model.predict(product_data_df)
        data = {"Tolerance":predicted[0]}
        return Response(data, status=200)

    # fürs debuggen
    @action(detail=True, methods=['GET'])
    def count_tool_use(self,request,pk=None):
        thismachine = machine.objects.get(id=pk)
        lastchange = tool_change.objects.filter(machine=thismachine).order_by('-created')[0]
        latestpro = production.objects.filter(machine=thismachine).filter(created__gt=lastchange.created)
        counter = len(latestpro)
        data = {"count":counter}
        return Response(data, status=200)


    @action(detail=True, methods=['GET'])
    def time_tool_use(self,request,pk=None):
        thismachine = machine.objects.get(id=pk)
        lastchange = tool_change.objects.filter(machine=thismachine).order_by('-created')[0]
        latestpro = production.objects.filter(machine=thismachine).filter(created__gt=lastchange.created)
        runtime = 0
        for product in latestpro:
            runtime = runtime + product.product.time
        data = {"time":runtime}
        return Response(data, status=200)


    @action(detail=True, methods=['GET'])
    def order_predict(self,request,pk=None):
        thismachine = machine.objects.get(id=pk)
        try:
            lastchange = tool_change.objects.filter(machine=thismachine).order_by('-created')[0]
            latestpro = production.objects.filter(machine=thismachine).filter(created__gt=lastchange.created)
        except:
            latestpro = production.objects.filter(machine=thismachine)
        runtime = 0
        for product in latestpro:
            runtime = runtime + product.product.time

        orders = order.objects.filter(machine=thismachine)
        ordersids = []
        ordersproduct = []
        orderprediction = []
        orderruntime = []
        ordermachinetime = []

        for orderobj in orders:
            orderruntime.append(runtime)
            ordermachinetime.append(0)
            ordersids.append(orderobj.id)
            ordersproduct.append(orderobj.product.name)
            runtime = runtime + orderobj.product.time
          

        try:
            model = pickle.loads(thismachine.model)
            product_data_pre = {'tool_runtime':orderruntime,'machine_runtime':ordermachinetime}
            product_data_df = pd.DataFrame.from_dict(product_data_pre)

            predicted = model.predict(product_data_df)

            for i in predicted:
                 orderprediction.append(round(i,4))
        except:
            for orderobj in orders:
                orderprediction.append("Kein Modell vorhanden")

        data = {"orderid":ordersids,"ordersproduct":ordersproduct,'orderprediction':orderprediction}

        return Response(data, status=200)


    @action(detail=True, methods=['GET'])
    def tool_change(self,request,pk=None):
        thismachine = machine.objects.get(id=pk)
        lastchange = tool_change.objects.create(machine=thismachine)
        lastchange.save()
        data = {"message":"success"}
        return Response(data, status=200)