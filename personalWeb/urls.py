from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
     path('contact', views.contact,name='contact'),
     path('certeficate',views.certeficate,name='certeficate'),
     path('about',views.about,name='about'),
     path('comingsoon',views.comingsoon,name='comingsoon'),
     path('skills',views.skills,name='skills'),
     path('chatanswer',views.chatanswer,name='chatanswer'),
     path('chatgpt',views.chatgpt,name='chatgpt'),
     path('signup',views.signup,name='signup'),
     path('login',views.login,name='login'),

]
