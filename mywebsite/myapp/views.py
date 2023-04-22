from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return HttpResponse('<h1>สวัสดี ครับ</h1>')
