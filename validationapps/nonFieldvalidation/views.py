from django.shortcuts import render,HttpResponse,redirect
from .forms import InpurMyForm
from django.contrib import messages
from django.views.generic import View


# def index(request):
#     if request.method == 'POST':
#         form = InpurMyForm(request.POST)
#         if form.is_valid():
#             pass  # does nothing, just trigger the validation
#     else:
#         form = InpurMyForm()
#     return render(request, 'index.html', {'form': form})








# Create your views here.

class OutputFunction(View):
    def get(self, request, *args, **kwargs):
        form=InpurMyForm()
        return render(request,'index.html',{'form': form})

    def post(self, request, *args, **kwargs):
        form=InpurMyForm(request.POST)
        if form.is_valid():
            return HttpResponse('send success--------------')
        else:
            print(request.POST)
            return render(request, 'index.html', {'form': form})