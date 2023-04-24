import time,datetime
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .models import *
from .forms import MobilePaymentForm
from paynow import Paynow



def loginView(request):
    messages=""
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home') 
            else:
                messages = "username or password is incorrect" 
        context = {
            'msg':messages,
        }
        return render(request,'registration/login.html',context)

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Home(request):
    form = MobilePaymentForm()
    balance_query = Customerbalance.objects.filter(parkCustomer = request.user)
    transaction_query = Transactions.objects.filter(parkCustomer = request.user)

    if request.method == 'POST' :
        amountpaid = request.POST.get("amount")
        
        
   

       
        try:
            amountpaid = float(amountpaid)
            balances = balance_query.last()
            amountpaid += int(balances.balance)
        except:
            pass


        customerBalance = Customerbalance(
            parkCustomer = request.user,
            balance = str(amountpaid),
        )
        customerBalance.save()
   
    balances = balance_query.last()
    context = {
        'form':form,
        'transaction_list':transaction_query,
        'balances': balances
    }
    return render(request,'Home.html',context)

def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else :
            form = UserCreationForm()
        return render(request,'registration/register.html',{'form':form})    

def generate_transaction_id():
    """
    Generates a unique id which will be used by paynow to refer to the payment
    initiated
    """
    return str(int(time.time() * 1000))


def paynow_mobile_payment(request):
    
    paynow = Paynow(
        'INTEGRATION_ID', 
        'INTEGRATION_KEY',
        'http://google.com', 
        'http://google.com'
        )

    payment = paynow.create_payment('Order', '[email protected]')

    payment.add('Payment for stuff', 1)

    response = paynow.send_mobile(payment, '0777777777', 'ecocash')


    if(response.success):
        poll_url = response.poll_url

        print("Poll Url: ", poll_url)

        status = paynow.check_transaction_status(poll_url)

        time.sleep(30)

        print("Payment Status: ", status.status)
