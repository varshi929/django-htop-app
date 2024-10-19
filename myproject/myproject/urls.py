from django.contrib import admin
from django.urls import path
from htopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', views.htop_view),  # URL for `/htop/`
    path('', views.home_view),  # URL for `/` (root)
]
