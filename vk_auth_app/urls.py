from django.urls import path
from .views import index, logout

urlpatterns = [
    path('', index, name='main_page'),
    path('logout/', logout, name='logout')
]
