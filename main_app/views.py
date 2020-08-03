from django.shortcuts import render

from .models import BrandsWeUse


# Create your views here.
def index(request):

    return render(request, "main_app/index.html", {})


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
