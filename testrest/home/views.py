from django.shortcuts import render
from django.shortcuts import redirect

from data.models import machine,order

from .forms import machine_form, order_form


def maschines_main_view(request):
    machines = machine.objects.all()
    template_name = 'home/machines.html'
    context = {"machines":machines}
    return render(request, template_name, context) 

def machine_create(request):
    template_name = 'home/machine_create.html'
    form = machine_form(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            obj = machine.objects.create(**form.cleaned_data) 
            obj.save()
            return redirect("/maschine/"+obj.domain)
    else:
        form = machine_form()
    context = {"form":form}
    return render(request, template_name, context) 

def machine_detail_view(request,slug):

    machineobj = machine.objects.get(domain=slug)
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
    context = {"machine":machineobj,"orders":orders,"form":form}
    return render(request, template_name, context) 


