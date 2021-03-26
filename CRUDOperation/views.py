from django.shortcuts import render
from CRUDOperation.models import EmpModel
from django.contrib import messages
from CRUDOperation.forms import EmpForms


def showemp(request): 
    showall=EmpModel.objects.all()
    return render(request,'Index.html',{"data":showall})  


def insertEmp(request):
    if request.method=="POST":
        if request.POST.get('empnombre') and  request.POST.get('empapellido') and  request.POST.get('cargo') and  request.POST.get('salario') and  request.POST.get('genero') :
            saverecord=EmpModel()
            saverecord.empnombre=request.POST.get('empnombre')
            saverecord.empapellido=request.POST.get('empapellido')
            saverecord.cargo=request.POST.get('cargo')
            saverecord.salario=request.POST.get('salario')
            saverecord.genero=request.POST.get('genero')
            saverecord.save()
            messages.success(request,'Empleado '+saverecord.empnombre+' fue guardado exitosamente...!')
            return render(request,'Insert.html')
    else:
        return render(request,'Insert.html') 



def editarEmp(request,id):
    editarEmpObj=EmpModel.objects.get(id=id)
    return render(request,'Editar.html',{'EmpModel':editarEmpObj}) 
        

def actualizarEmp(request,id):
    ActualizarEmp=EmpModel.objects.get(id=id)
    form=EmpForms(request.POST, instance=ActualizarEmp)
    if form.is_valid():
        form.save()
        messages.success(request,'Empleado actualizado exitosamente..!')
        return render(request,'Editar.html',{'EmpModel':ActualizarEmp})
    

def eliminar(request,id):
    eliminarEmpleado=EmpModel.objects.get(id=id)
    eliminarEmpleado.delete()
    showdata=EmpModel.objects.all()
    return render(request,'Index.html',{'data':showdata})
