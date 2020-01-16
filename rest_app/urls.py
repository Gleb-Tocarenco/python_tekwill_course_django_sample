from django.urls import path
from rest_app import views

urlpatterns = [
    path('fancy-cats/', views.FanctCatListView.as_view(), name='fancy_cats_list'),
    path('fancy-cats/<int:pk>/', views.FanctCatDetailView.as_view(), name='fancy_cats_detail')
]
