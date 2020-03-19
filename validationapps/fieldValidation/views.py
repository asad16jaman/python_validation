from django.shortcuts import render,HttpResponse,redirect
from .models import myform,Author
from django.contrib import messages


def index(request):
    data=Author.objects.all()
    p=myform()
    if request.method=='POST':
        p=request.POST['even_field']
        if Author.objects.filter(even_field=p):
            messages.info(request,'inter unic email this email is exist ')
            return redirect('/')
        else:
            form=myform(request.POST)
            if form.is_valid():
                form.save()
            print(form.errors)
            messages.info(request,f"{ form.errors }")

            print('----------------------------------------')
            return redirect('/')

    return render( request,'index2.html', {'data':p,'table':data})