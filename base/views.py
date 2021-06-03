from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'base.html')