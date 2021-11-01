import json

from django.http import HttpResponse
from django.shortcuts import render
from web3 import Web3
from .models import Registration
# Create your views here.


def home(request):
    return render(request,'register.html')


def verification(request):
    if request.is_ajax():
        data=json.loads(request.body.decode('UTF-8'))
        address= data['address']
        request.session['bsc_address'] = address[0]
        user = Registration.objects.filter(bsc_address=address[0])
        access = False
        if user.exists() or check_staker(address[0]):
            access = True
        return HttpResponse(json.dumps({'access': access}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'msg': 'request type is not allowed !!'}), content_type="application/json")


def check_staker(add):
    f = open('register/GriseToken.json', "r")
    w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org:443'))
    currentAbis = json.loads(f.read())
    address = w3.toChecksumAddress('0xb359e4290573a3974616b7c26ea86939689b9ec4')
    contract = w3.eth.contract(address=address, abi=currentAbis['abi'])
    return contract.functions.isStaker(w3.toChecksumAddress(add)).call()


def register(request):
    bsc_address = request.session.get('bsc_address')
    address = request.POST.get('nami_address')
    try:
        user = Registration.objects.get(bsc_address=bsc_address)
        user.nami_address = address
        user.save()
    except:
        user = Registration()
        user.bsc_address = bsc_address
        user.nami_address = address
        user.save()
    print(bsc_address)
    print(address)
    return render(request,'register.html',{'msg':'Thanks for registering !!'})
