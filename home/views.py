from django.shortcuts import render
from django.shortcuts import redirect
from data.models import machine,order
from .forms import machine_form, order_form
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def maschines_main_view(request):
    token = Token.objects.get(user=request.user)
    machines = machine.objects.all()
    template_name = 'home/machines.html'
    context = {"machines":machines,"token":token}
    return render(request, template_name, context) 

@login_required(login_url='/login')
def machine_create(request):
    template_name = 'home/machine_create.html'
    token = Token.objects.get(user=request.user)
    form = machine_form(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            obj = machine.objects.create(**form.cleaned_data) 
            obj.save()
            return redirect("/maschine/"+obj.domain)
    else:
        form = machine_form()
    context = {"form":form,"token":token}
    return render(request, template_name, context) 

@login_required(login_url='/login')
def machine_detail_view(request,slug):
    machineobj = machine.objects.get(domain=slug)
    token = Token.objects.get(user=request.user)
    form = order_form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = order.objects.create(**form.cleaned_data) 
            obj.machine = machineobj
            obj.save()
            return redirect("/maschine/"+machineobj.domain)
    else:
        form = order_form()
    orders = order.objects.filter(machine=machineobj)
    template_name = 'home/machine_detail.html'
    context = {"machine":machineobj,"orders":orders,"form":form,"token":token}
    return render(request, template_name, context) 

@login_required(login_url='/login')
def home_view(request):
    token = Token.objects.get(user=request.user)
    template_name = 'home/home.html'
    context = {"token":token}
    return render(request, template_name, context) 
