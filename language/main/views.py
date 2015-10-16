from django.shortcuts import render 
import datetime 
# Create your views here.
def main(request):
    now=datetime.datetime.now()
    context = {'message':'Django 很棒','time':now}
    return render(request, 'main/main.html', context)