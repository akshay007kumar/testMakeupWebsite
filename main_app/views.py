from django.shortcuts import render
import datetime

from .models import BrandsWeUse, MakeupOffers


# Create your views here.
def index(request):
    offers = MakeupOffers.objects.filter(end_date__gte=datetime.date.today())
    context = {
        'artist_name': 'Makeup Artist',
        'artist_location': 'Delhi',
        'whatsapp_number': '9149883693',
        'offers': offers,
        'hasOffers': True if offers else False,
    }

    return render(request, "main_app/index.html", context)


def about(request):

    return render(request, "main_app/about.html", {})


def service(request):

    return render(request, "main_app/pricing_table.html", {})


def contact(request):

    return render(request, "main_app/contactus.html", {})


def gallery(request):

    return render(request, "main_app/gallery.html", {})


def book_online(request):

    return render(request, "main_app/book_online.html", {})


def brands_we_use(request):
    brands = BrandsWeUse.objects.all()
    context = {
        'brands': brands
    }

    return render(request, "main_app/brands_we_use.html", context)
