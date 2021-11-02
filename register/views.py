import json
import os
from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render
from web3 import Web3
from .models import Registration, Reservation


# Create your views here.


def home(request):
    return render(request, 'register.html')


def verification(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('UTF-8'))
        address = data['address']
        user = Reservation.objects.filter(address=address[0])
        access = False
        if user.exists() or check_staker(address[0]):
            request.session['bsc_address'] = address[0]
            access = True
        return HttpResponse(json.dumps({'access': access}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'msg': 'request type is not allowed !!'}), content_type="application/json")


def check_staker(add):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'GriseToken.json'
    file = open(file_location, encoding='utf-8')
    w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org:443'))
    currentAbis = json.loads(file.read())
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
        msg = "Your Nami wallet address is updated !!"
    except:
        user = Registration()
        user.bsc_address = bsc_address
        user.nami_address = address
        user.save()
        msg = "Thank you for registering Nami wallet address !!"
    return render(request, 'register.html', {'msg': msg})
