from django.shortcuts import render,redirect
from . forms import CreateUserForm,LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout

import openai
import os
from openai import OpenAI

#send email labriray
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    return render(request,'index.html')


def contact(request):
    if request.method=='POST':
        message=request.POST['comment']
        email=request.POST['email']
        name=request.POST['fname']

        send_mail('contact from: ',
                  message,'settings.EMAIL_HOST_USER',[email],
                  fail_silently=False)

    return render(request,'contact.html')


def certeficate(request):
    return render(request,'certeficate.html')

def about(request):
    return render(request,'about.html')
def comingsoon(request):
    return render(request,'comingsoon.html')
def skills(request):
    return render(request,'skills.html')

def chatgpt(request):
    
    return render(request,'comingsoon.html')




def chatanswer(request):
    text=request.POST["userask"]
    client= OpenAI()
    open_api_key=os.getenv("OPENAI_API_KEY")
    
    response = client.completions.create (
       # engine="text-davinci-003",
        model="gpt-3.5-turbo",
        max_tokens=140,
        n=1,
        stop=None,
        temperature=0.7,
        prompt="Who won the world series in 2020?",
        # messages=[
        #      {"role": "user", "content": "Who won the world series in 2020?"}
     
        #  ]
   )


    
    return render(request,'chatanswer.html',{"res":response})




def signup(request):

    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context={'signupform':form}

    return render(request,'signup.html',context=context)





def login(request):

    form =LoginForm()
    if request.method=="POST":
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("/admin")
    
    context={'loginform':form}

    return render(request,'login.html',context=context)

