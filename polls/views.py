#! /usr/bin/env python
# encoding:utf-8

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello,world')
