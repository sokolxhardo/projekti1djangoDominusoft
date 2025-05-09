from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context ={"products":products,"categories":categories}
    return render(request, "ProjektiH.html", context)

def category_products(request,id):
    categories = Category.objects.all()
    categoryDetail = Category.objects.get(pk=id)
    caregoryProducts = Product.objects.filter(product_category=categoryDetail)
    context = {"categories":categories, "categoryDetail":categoryDetail,
               "categoryProducts":caregoryProducts }
    return render(request, "makinaH.html", context)

# def category_products(request):
#     return render(request, "motorraH.html")

def rrethNesh(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, "rrethNeshH.html", context)

def kontakt(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    if request.method == "POST":
        infoFirstName = request.POST["emri"]
        infoLastName = request.POST["mbiemer"]
        infoEmail = request.POST["email"]
        infoPhoneNumber = request.POST["numer"]
        infoComent = request.POST["mesazhi"]
        if infoFirstName !="" and infoLastName !="" and infoEmail !="" and infoComent !="":
            Contact(
            contact_firstName = infoFirstName,
            contact_lastName = infoLastName,
            contact_email = infoEmail,
            contact_phoneNumber = infoPhoneNumber,
            contact_comment = infoComent,
            ).save()
        messages.success(request, "Message send!")
    else:
        messages.error(request, "Message not send! Please fill the form.")
    return render(request, "kontaktoH.html", context)

def product(request, id):
    categories = Category.objects.all()
    productDetail = Product.objects.get(pk=id)
    context = {"categories":categories, "productDetail":productDetail}
    return render(request, "audiH.html", context)

