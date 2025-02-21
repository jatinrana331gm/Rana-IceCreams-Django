from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),          # <-- Notice the comma
    path('about', views.about, name='about'),    # <-- Comma here too
    path('services', views.services, name='services'),
  path('contact', views.contact_view, name='contact'),

]
