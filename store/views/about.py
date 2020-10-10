from django.shortcuts import render , redirect

from django.contrib.auth.hashers import check_password
from django.views import  View

class About(View):
    def get(self , request):
        return render(request , 'aboutus.html')