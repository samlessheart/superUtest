from django.urls import path 
from .views import AddUserView , UserDetailView

urlpatterns = [ 
    
    path('adduser/', AddUserView.as_view(), name='adduser'),
    path('user/', UserDetailView.as_view(), name='user'),
    


]