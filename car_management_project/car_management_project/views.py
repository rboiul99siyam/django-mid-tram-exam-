from django.shortcuts import render
from posts.models import UserPostModel
from brands.models import brandModel


def home(request, brand_slug=None):
    data = UserPostModel.objects.all()
    if brand_slug is not None:
        brand = brandModel.objects.get(slug = brand_slug)
        data = UserPostModel.objects.filter(brand = brand)
    brands = brandModel.objects.all()
    return render(request, "home.html", {"data": data, "brand": brands})
