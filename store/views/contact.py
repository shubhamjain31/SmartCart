from django.shortcuts import render , redirect
from store.models.contacts import Contact
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import  View

class ContactUs(View):
    def get(self , request):
        return render(request , 'contactus.html')

    def post(self , request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        error = None
        customer = Customer.get_customer_by_email(email)
        if name == '' or email == '' or phone == '' or desc == '':
        	error = 'Please fill the blank field !!'
        	return render(request, 'contactus.html',{'error':error})
        elif customer:
            if request.session.has_key('customer'):
                con = Contact(name=name,
                        email=email,
                        phone=phone,
                        desc=desc)
                con.save()
            else:
            	error = 'You are not logged in !!'
            	return render(request, 'contactus.html',{'error':error})
        else:
        	error = 'You are not registered !!'
        	return render(request, 'contactus.html',{'error':error})
        return render(request, 'contactus.html')