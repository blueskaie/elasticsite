from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    return render_to_response('index.html',{})
def about(request):
    return render_to_response('about.html',{})
def analy(request):
    return render_to_response('analy.html',{})
def integration(request):
    return render_to_response('integration.html',{})
def market(request):
    return render_to_response('market.html',{})
def track(request):
    return render_to_response('track.html',{})
def careers(request):
    return render_to_response('careers.html',{})
