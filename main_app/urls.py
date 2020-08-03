from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('contact-us/', views.contact, name="contactus"),
    path('gallery/', views.gallery, name="gallery"),
    path('book-online/', views.book_online, name="book-online"),
    path('brands-used/', views.brands_we_use, name="brands-used"),
]
