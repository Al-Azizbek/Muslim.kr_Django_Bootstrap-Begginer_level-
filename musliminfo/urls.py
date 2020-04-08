from django.urls import path
from .views import homepage, contactpage,aboutpage,newspage,loginpage,signuppage,charitypage,calendarpage,themingpage


urlpatterns =[
  path('', homepage, name='home'),
  path('contact/', contactpage, name='contact'),
  path('aboutus/', aboutpage, name='aboutus'),
  path('news/', newspage, name='news'),
  path('login/', loginpage, name='login'),
  path('signup/', signuppage, name='signup'),
  path('charity/', charitypage, name='charity'),
  path('calendar/', calendarpage, name='calendar'),
  path('theming/', themingpage, name='theming'),
  ]