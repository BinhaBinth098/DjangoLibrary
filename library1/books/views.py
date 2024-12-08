from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

from books.models import Books
@login_required
def viewbooks(request):
    # k=con.execute('select * from Books')


    # k=modelname.objects.all()
    k=Books.objects.all()  #reads all records from the book table
    context={'books':k}   #sends data from view fun to html page
    return render(request,'viewbooks.html',context)

@login_required
def viewbdetails(request,p):
    k=Books.objects.get(id=p)  # read a particular record
    context={'books':k}
    return render(request,'viewbdetails.html',context)


@login_required
def delete(request,p):
    k=Books.objects.get(id=p)  # read a particular record
    k.delete()
    return redirect('books:viewbooks')


@login_required
def edit(request,p):
    k=Books.objects.get(id=p)  # read a particular record

    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.language=request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES.get('i')
        if(request.FILES.get('pd')==None):
            k.save()
        else:
            k.pdf=request.FILES.get('pd')
        k.save()
        return redirect('books:viewbooks')

    context = {'books': k}
    return render(request,'edit.html',context)

@login_required
def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        l=request.POST['l']
        i=request.FILES['i']
        pd=request.FILES['pd']
        b=Books.objects.create(title=t,author=a,language=l,cover=i,pdf=pd)
        b.save()
        return viewbooks(request)
    return render(request,'addbooks.html')