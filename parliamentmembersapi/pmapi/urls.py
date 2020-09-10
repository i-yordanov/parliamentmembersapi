from django.urls import path
from . import views

urlpatterns = [
    path('/list', views.ListParliamentMemberAPIView.as_view()),
    path('/search', views.SearchParliamentMemberAPIView.as_view()),
    path('/pm/<pk>/', views.RetrieveByIDParliamentMemberAPIVIEW.as_view()),
]
