# Create your views here.
import json
import os
from decimal import *
from collections import UserDict
# from My_App.context_processor import Owner_Property_renderer 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from My_App.models import User,customer,owner,customer_phone,owner_phone,owner_property,property_images
from django.contrib import messages
from Agile_Design_Thinking_DBMS import settings
from django.contrib.auth import authenticate, login as mylogin, logout as mylogout

# Create your views here.
def home(request):
    return render(request, "home_page/index.html")   

def register(request):

    if request.method == "POST":

        if request.POST['role'] == 'customer':
        
           username = request.POST['username']
           fname = request.POST['fname']
           lname = request.POST['lname']
           email = request.POST['email']
           pass1 = request.POST['pass1']
           pass2 = request.POST['pass2']
           phone_number_1 = request.POST['pn1']
           phone_number_2 = request.POST['pn2']
           gender = request.POST['gender']
           soi = request.POST['soi']
           income = request.POST['income']
           age = request.POST['age']
           bio = request.POST['bio']
           profile_pic = request.FILES.get('imageupload')
           is_customer = True

           if User.objects.filter(username=username):
            return redirect('home')
        
           if User.objects.filter(email=email).exists():
            return redirect('home')
        
           if len(username)>30:
            return redirect('home')
        
           if pass1 != pass2:
            return redirect('home')

           if phone_number_1 == phone_number_2:
              return redirect('home')
        
           if not username.isalnum():
            return redirect('home')

           myuser = User.objects.create_user(password = pass1,username = username,first_name = fname,last_name = lname,email = email,is_customer = is_customer)

           myuser.save()

           customer_id = User.objects.only('id').get(username = username).id

           customer_profile= customer.objects.create(user_id = customer_id ,gender=gender,soi=soi,income=income,age=age,bio=bio,customer_profile_picture = profile_pic)

           customer_profile.save()

           customer_phone_number= customer_phone.objects.create(customer_phone_id_id = customer_id,phone_number=phone_number_1)
                              
           customer_phone_number.save()

        #    customer_phone_number= customer_phone.objects.create(customer_phone_id_id = customer_id,phone_number=phone_number_2)
                              
        #    customer_phone_number.save()

           messages.success(request, "Your account has been successfully created")
           return redirect('login')

        if request.POST['role'] == 'owner':
        
           username = request.POST['username']
           fname = request.POST['fname']
           lname = request.POST['lname']
           email = request.POST['email']
           pass1 = request.POST['pass1']
           pass2 = request.POST['pass2']
           phone_number_1 = request.POST['pn1']
           phone_number_2 = request.POST['pn2']
           gender = request.POST['gender']
           soi = request.POST['soi']
           income = request.POST['income']
           age = request.POST['age']
           bio = request.POST['bio']
           profile_pic = request.FILES['imageupload']
           is_owner=True

        if User.objects.filter(username=username):
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            return redirect('home')
        
        if len(username)>20:
            return redirect('home')
        
        if pass1 != pass2:
            return redirect('home')

        if phone_number_1 == phone_number_2:
            return redirect('home')
        
        if not username.isalnum():
            return redirect('home')

        myuser = User.objects.create_user(password = pass1,username = username,first_name = fname,last_name = lname,email = email,is_owner = is_owner)

        myuser.save()

        owner_id = User.objects.only('id').get(username = username).id

        owner_profile= owner.objects.create(user_id = owner_id,gender=gender,soi=soi,income=income,age=age,bio=bio,owner_profile_picture = profile_pic)

        owner_profile.save()

        owner_phone_number= owner_phone.objects.create(owner_phone_id_id = owner_id,phone_number=phone_number_1)
                              
        owner_phone_number.save()

        # owner_phone_number= owner_phone.objects.create(owner_phone_id_id = owner_id,phone_number=phone_number_2)
                              
        # owner_phone_number.save()

        messages.success(request, "Your account has been successfully created")
        return redirect('login')
    
    return render(request, "login_and_register_pages/register.html")


def login(request):

    if request.method == 'POST':
    
            username = request.POST['username']
            pass1 = request.POST['pass1']

            user = authenticate(username = username , password=pass1)

            if user is not None and user.is_customer == True:
                    
                    mylogin(request,user)

                    request.session['fname'] = user.first_name
                    request.session['lname'] = user.last_name
                    request.session['email'] = user.email 
                    request.session['username'] = user.username
                    customer_id = User.objects.only('id').get(username = username).id
                    mycustomer = customer.objects.all().get(user_id = customer_id)
                    my_customer_phone = customer_phone.objects.all().get(customer_phone_id_id = customer_id)
                    request.session['gender']=mycustomer.gender
                    request.session['age']=mycustomer.age
                    request.session['bio']=mycustomer.bio
                    request.session['soi']=mycustomer.soi
                    request.session['income'] = json.dumps(mycustomer.income, default=str)
                    request.session['customer_profile_picture'] = str(mycustomer.customer_profile_picture)
                    request.session['customer_phone_number']=my_customer_phone.phone_number
                    property_list = owner_property.objects.all()
                    # request.session['property_list'] = list(property_list)
                    # owner_property = owner_property.objects.all()
                    # request.session['property_number']=owner_property.property_number
                    # request.session['state']=owner_property.state 
                    # request.session['city']=owner_property.city
                    # request.session['pincode']=owner_property.pincode
                    # request.session['property_area']=owner_property.property_area
                    # request.session['locality']=owner_property.locality
                    # request.session['house_number']=owner_property.house_number
                    # request.session['room_type']=owner_property.room_type
                    # request.session['nob']=owner_property.number_of_bathrooms
                    # request.session['property_discription']=owner_property.property_discription
                    # request.session['is_booked']=owner_property.is_booked
                    # request.session['rent_of_property']=json.dumps(owner_property.rent_of_property,default = str)
                    owner_property_id_list = owner_property.objects.all().only('user_id')
                    owner_property_images_list = property_images.objects.all().only('user_id')
                    
                    return render(request, "customer/customer.html",{"property_list":property_list,"owner_property_id_list":owner_property_id_list,"owner_property_images_list":owner_property_images_list})
                    # "soi":customer_soi,"age":customer_age,"bio":customer_bio,"customer_profile_picture":customer_profile_picture,"income":customer_income,"gender":customer_gender,"customer_phone_number":customer_phone_number,"property_list":property_list,"owner_property_id_list":owner_property_id_list})

                    # "customer_details":customer_details
            elif user is not None and user.is_owner == True:
    
                    mylogin(request,user)

                    request.session['fname'] = user.first_name
                    request.session['lname'] = user.last_name
                    request.session['email'] = user.email 
                    request.session['username'] = user.username
                    owner_id = User.objects.only('id').get(username = username).id
                    myowner = owner.objects.all().get(user_id = owner_id)
                    my_owner_phone = owner_phone.objects.all().get(owner_phone_id_id = owner_id)
                    request.session['gender']=myowner.gender
                    request.session['age']=myowner.age
                    request.session['bio']=myowner.bio
                    request.session['soi']=myowner.soi
                    request.session['income'] = json.dumps(owner.income, default=str)
                    request.session['owner_profile_picture'] = str(myowner.owner_profile_picture)
                    request.session['owner_phone_number']=my_owner_phone.phone_number
                    owner_details = owner.objects.all().get(user_id = owner_id)
                    owner_property_list = owner_property.objects.all().filter(user_id = owner_id)
                    owner_property_images_list = property_images.objects.all().only('user_id')
                    # Owner_Property_renderer(owner_id,request)
                    # owner_phone_list = User.objects.all('phone_number').filter(user_id = owner_id)

                    return render(request, "owner/owner.html",{"owner":owner_details,"owner_property_list":owner_property_list,"owner_property_images_list":owner_property_images_list})
                    # "soi":owner_soi,"age":owner_age,"bio":owner_bio,"owner_profile_picture":owner_profile_picture,"income":owner_income,"gender":owner_gender,"owner_phone_number":owner_phone_number,"owner_property_list":owner_property_list})

            elif user is not None and user.is_admin == True:
    
                    mylogin(request,user)
                    return render(request, "admin/admin.html")
                    
            else:
                    return redirect('home')
        
    return render(request, "login_and_register_pages/login.html")


def logout(request):
    mylogout(request)
    return redirect('home')

def customer_profile(request):
    return render(request, "customer/customer_profile.html")

def owner_profile(request):
    return render(request, "owner/owner_profile.html")

def customer_page(request):
    return render(request, "customer/customer.html")

def owner_page(request):
    return render(request, "owner/owner.html")

def customer_chat_owner(request):
    return render(request, "customer/customer_chat_owner.html")

def owner_chat_customer(request):
    return render(request, "owner/owner_chat_customer.html")

def customer_search_property(request):

    if request.method == "POST":
        get_state = request.POST.get('state')
        get_city = request.POST.get('city')
        string = "\""
        mystring = string+get_city+string
        print(mystring) 
        property_list = owner_property.objects.filter(city = get_city)
        return render(request,'customer/customer.html', {"property_list":property_list})

    return render(request, 'customer/customer.html')

def add_property(request):

    if request.method == "POST":
        
        username = request.POST['username']
        owner_id = User.objects.only('id').get(username = username).id
        pnum = request.POST['property_number']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        property_area = request.POST['area']
        locality = request.POST['locality']
        hnum = request.POST['house']
        room_type = request.POST['room_type']
        nob = request.POST['nob']
        rent = request.POST['rent']
        property_discription = request.POST['discription']
        # image_1 = request.FILES['image_1']
        # image_2 = request.FILES['image_2']
        # image_3 = request.FILES['image_3']
        # image_4 = request.FILES['image_4']
        # image_5 = request.FILES['image_5']
        image_1 = request.FILES.get('image_1'," ")
        image_2 = request.FILES.get('image_2'," ")
        image_3 = request.FILES.get('image_3'," ")
        image_4 = request.FILES.get('image_4'," ")
        image_5 = request.FILES.get('image_5'," ")

        new_owner_property=owner_property.objects.create(user_id  = owner_id, property_number = pnum,state = state,city = city,pincode=pincode,property_area = property_area,locality=locality,house_number = hnum, room_type = room_type , number_of_bathrooms = nob, rent_of_property = rent, property_discription = property_discription)
        new_owner_property.save()
        new_image = property_images.objects.create(user_id  = owner_id,property_image = image_1)
        new_image.save()
        # new_image = property_images.objects.create(user_id  = owner_id,property_image = image_2)
        # new_image.save()
        # new_image = property_images.objects.create(user_id  = owner_id,property_image = image_3)
        # new_image.save()
        # new_image = property_images.objects.create(user_id  = owner_id,property_image = image_4)
        # new_image.save()
        # new_image = property_images.objects.create(user_id  = owner_id,property_image = image_5)
        # new_image.save()
        return redirect('owner_page')

    return render(request, "owner/owner_add_property.html")

def customer_request(request):

    if request.method == "POST":
        # is_booked
        # new_request = booking.objects.create()
        return redirect('customer_chat_owner')
    
    return render(request, "customer/customer.html")








