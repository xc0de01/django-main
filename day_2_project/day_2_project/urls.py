from django.contrib import admin
from django.urls import path
from main import views   # import your app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # maps root URL to test.html
]
