from django.contrib import admin
from django.urls import path, include
from restaurant.router import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("restaurant/booking/", include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
