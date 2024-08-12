from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:id>/', views.ProfileRetrieveUpdateDestroy.as_view(), name='profile-retrieve-update-destroy'),
    path('profiles/query/', views.ProfileList.as_view(), name='profile-list'),
]
