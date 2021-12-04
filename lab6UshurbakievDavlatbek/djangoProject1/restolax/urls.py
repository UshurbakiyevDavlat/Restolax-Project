from django.conf.urls.static import static
from django.urls import path

from djangoProject1 import settings
from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('index.html', views.index, name='index'),
                  path('about.html', views.about, name='about'),
                  path('chefs.html', views.chefs, name='chefs'),
                  path('contact.html', views.contact, name='contact'),
                  path('events.html', views.events, name='events'),
                  path('gallery.html', views.gallery, name='gallery'),
                  path('menu.html', views.menu, name='menu'),
                  path('specials.html', views.specials, name='specials'),
                  path('signUp.html', views.signUp, name='signUp'),
                  path('addUser.html', views.addUser, name='addUser'),
                  path('<id>/updateAcc', views.updateAcc, name='updateAcc'),
                  path('<id>/updateUser', views.updateUser, name='updateUser'),
                  path('<id>/deleteAcc', views.deleteAcc, name='deleteAcc'),
                  path('<id>/deleteUser', views.deleteUser, name='deleteUser')
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
