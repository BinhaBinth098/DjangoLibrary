from django.shortcuts import render,redirect
from employ.models import Employee

# Create your views here.
def view(request):
    k=Employee.objects.all()
    context={'employee':k}
    return render(request,'view.html',context)

def addemployee(request):
    if (request.method == "POST"):
        e=request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        g = request.POST['g']
        pl = request.POST['pl']
        d = request.POST['d']
        i = request.FILES['i']
        e= Employee.objects.create(emid=e,name=n,age=a,gender=g,place=pl,designation=d,image=i)
        e.save()
        return redirect('view')
    return render(request,'add.html')

def edit(request,p):
    e = Employee.objects.get(id=p)
    if (request.method=="POST"):
        e.emid = request.POST['e']
        e.name = request.POST['n']
        e.age = request.POST['a']
        e.gender = request.POST['g']
        e.place = request.POST['pl']
        e.designation = request.POST['d']
        if (request.FILES.get('i') == None):
            e.save()
        else:
            e.image = request.FILES.get('i')
        return redirect('view')

    context = {'employ': e}
    return render(request,'edit.html',context)

def delete(request,p):
    e=Employee.objects.get(id=p)
    e.delete()
    return redirect('view')