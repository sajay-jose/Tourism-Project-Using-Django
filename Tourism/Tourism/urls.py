"""
URL configuration for Tourism project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('user_register', views.user_register, name="user_register"),
    path('agency_register', views.agency_register, name="agency_register"),
    path('Login', views.Login, name="Login"),
    path('Logout', views.Logout, name="Logout"),
    path('contact', views.contact, name="contact"),
    path('index', views.index),
    path('packages', views.packages, name="packages"),
    path('search_package', views.search_package, name="search_package"),


    path('add_package', views.add_package, name="add_package"),
    path('health_assistance', views.health_assistance, name="health_assistance"),
    path('delete_healthassistant/<int:id>', views.delete_healthassistant, name="delete_healthassistant"),
    path('agencyindex', views.agencyindex, name="agencyindex"),
    path('edit_bookingstatus/<int:id>', views.edit_bookingstatus, name="edit_bookingstatus"),
    path('edit_agencyprofile', views.edit_agencyprofile, name="edit_agencyprofile"),
    path('edit_package/<int:id>', views.edit_package, name="edit_package"),
    path('delete_package/<int:id>', views.delete_package, name="delete_package"),
    path('rating/<int:id>', views.rating, name="rating"),



    path('userHome', views.userHome, name="userHome"),
    path('edit_userprofile', views.edit_userprofile, name="edit_userprofile"),
    path('user_packages', views.user_packages, name="user_packages"),
    path('usersearch_package', views.usersearch_package, name="usersearch_package"),
    path('user_contact', views.user_contact, name="user_contact"),
    path('packageDetails/<int:id>', views.packageDetails, name="packageDetails"),
    path('userviewbookings', views.userviewbookings, name="userviewbookings"),
    path('cancel_booking/<int:id>', views.cancel_booking, name="cancel_booking"),
    path('add_review/<int:id>', views.add_review, name="add_review"),
    path('payments/<int:id>', views.payments, name="payments"),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
