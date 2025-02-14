from django.urls import path
from rango import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'rango'

urlpatterns = [
    #maps /rango/ to the index view
    path('', views.index, name='index'),
    #maps '/rango/about/' to 'about'
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path("login/", views.user_login, name="login"),
    path("restricted/", views.restricted, name="restricted"),
    path("logout/", views.user_logout, name="logout"),
]