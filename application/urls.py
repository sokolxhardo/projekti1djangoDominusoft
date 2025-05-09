from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="homePage"),
    path("makina/<id>", views.category_products, name="makinaHPage"),
    # path("motorraH", views.home, name="motorraHPage"),
    path("rrethNesh/", views.rrethNesh, name="rrethNeshHPage"),
    path("kontakto/", views.kontakt, name="kontaktoHPage"),
    path("info/<id>", views.product, name="audiHPage")
]