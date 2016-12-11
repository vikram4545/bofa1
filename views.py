from django.shortcuts import render
from .models import Number, Holder, Employer, Number1
from .forms import NumberForm, HolderForm, EmployerForm, NumberForm1, SearchForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, DeleteView,ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
import random
from django import forms

@login_required(login_url='/login/')
def index(request):
    number = Number.objects.all()
    number1 = Number.objects.all()
    employer = Employer.objects.all()
    form = NumberForm(request.POST,request.FILES)
    if form.is_valid():
        number = form.save(commit=False)
        if number.anumber in [ x.employeId for x in employer ]:
            number.anumber = 'BL'
            while len(number.anumber) <= 13:
                y = random.randrange(0, 1000000)
                number.anumber = number.anumber + str(y)
                print(len(number.anumber))
                if len(number.anumber) == 12:
                    number.save()
                    print(number)
                    if number.anumber in [p.anumber for p in number1]:
                        return HttpResponseRedirect("/bofa/home/")
                    return render(request,'index.html',{'form':form,'number':number, })
    return render(request,'index.html',{'form':form,'number':number, })


@login_required(login_url='/login/')
def hbalance(request):
    holder = Holder.objects.all()
    number1 = Number.objects.all()
    employer = Employer.objects.all()
    form=HolderForm(request.POST or None)
    if form.is_valid():
        holder = form.save(commit= False)
        for y in number1:
            if y.anumber == holder.number and y.name==holder.name:
                for x in number1:
                    if str(x.anumber) == str(holder.number):
                
                        h = x.anumber
                        print(x.balance)
                        if x.balance >= holder.withdraw:
                            x.balance = x.balance-holder.withdraw
                        else:
                            return HttpResponse('You have no sufficient Funds')
                        x.balance = x.balance+holder.deposite
                        holder.balance = x.balance

                        z1 = holder.deposite
                        z2 = holder.withdraw
                        if z1 > 0 and z2 > 0:
                            return HttpResponse("Both deposite and withdraw should not be done at the same time")
                        elif z1 == 0 and z2 == 0:
                           return render(request,'2.html',{'holder':holder,'number1':number1,'form':form,'h':h})
                        else:
                            x.save()
                            holder.save()
                            return HttpResponseRedirect('/bofa/home/')
                        return render(request,'2.html',{'holder':holder,'number1':number1,
                                                        'form':form,'h':h,'employer':employer})
    return render(request,'1.html',{'holder':holder,'form':form,'number1':number1})


@login_required(login_url='/login/')
def transactions(request,id):
    number1 = Number.objects.get(id=id)
    employer = Employer.objects.all()
    holder=Holder.objects.filter(name = number1.name)
    s = SearchForm(request.POST or None)
    if s.is_valid():
        print(s)
    return render(request,'3.html',{'holder': holder,'number1':number1 ,'employer':employer, 's':s})


class Delete1(DetailView):
    model = Holder
    template_name = 'boapp/detail.html'
    context_object_name = 'j'
    success_url = reverse_lazy('delete')


class Delete2(DetailView):
    model = Number
    template_name = 'boapp/holder.html'
    context_object_name = 'i'
    success_url = reverse_lazy('delete1')


@login_required(login_url='/login/')
def home1(request):
    number = Number1.objects.all()
    number1 = Number.objects.all()
    holder = Holder.objects.all()
    employer = Employer.objects.all()
    form = NumberForm1(request.POST or None)
    if form.is_valid():
        number = form.save(commit= False)
        h = str(number.anumber)
        return render(request,'home2.html', {'number':number, 'number1': number1, 'holder': holder,'form': form,'h':h})
    return render(request,'home1.html',{'number':number,'number1':number1,'holder':holder,'form':form, 'employer':employer})


class Updatev(UpdateView):
    login_required= True
    model= Number
    fields = ['name']
    print(1345)
    context_object_name = 'j'


class CustomerDetails(ListView):
    model = Number
    template_name = 'boapp/customer.html'
    context_object_name = 'j'
    success_url = reverse_lazy('delete3')
