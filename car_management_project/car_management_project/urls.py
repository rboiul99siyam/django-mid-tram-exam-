from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user_authencated/", include("user_auth.urls")),
    path("car_details/", include("posts.urls")),
    path('car_data/', include('car.urls')),
    path("", views.home, name="home"),
    path("brand<slug:brand_slug>/", views.home, name="slugdata"),


    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
