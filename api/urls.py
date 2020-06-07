
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from api import views
urlpatterns = [
    #path('api/',),
    
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('usuario/<int:pk>/', views.UserDetail.as_view(), name = views.UserDetail.name),
    path('usuario/', views.UserList.as_view(), name = views.UserList.name),
]
