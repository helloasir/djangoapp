from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('web/', views.web, name='home'),
    path('domain', views.domain, name='home'),
    path('page', views.page, name='home'),
    path('data/', views.data, name='data'), path('data/page/<int:page>/', views.data, name='data-page'),

]
