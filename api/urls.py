
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from api import views
urlpatterns = [
	path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
	path('usuario/', views.UserList.as_view(), name = views.UserList.name),
	path('usuario/<int:pk>/', views.UserDetail.as_view(), name = views.UserDetail.name),
	path('candidate/', views.CandidateList.as_view(), name = views.CandidateList.name),
	path('candidate/<int:pk>/', views.CandidateDetail.as_view(), name = views.CandidateDetail.name),
	path('company/', views.CompanyList.as_view(), name = views.CompanyList.name),
	path('company/<int:pk>/', views.CompanyDetail.as_view(), name = views.CompanyDetail.name),
	path('address/', views.AddressList.as_view(), name = views.AddressList.name),
	path('address/<int:pk>/', views.AddressDetail.as_view(), name = views.AddressDetail.name),
]
