from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect



admin.site.site_header = "Administration Mupeppbo"
admin.site.site_title = "Mupeppbo"
admin.site.index_title = "Tableau de bord MUPEPPBO"

def home(request):
    return redirect('/admin/')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]
