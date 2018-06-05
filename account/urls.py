from django.urls import path
from .views import user_login, registration_form, user_logout

urlpatterns = [

    path('user-login/', user_login, name='user-login'),
    path('user-logout/', user_logout, name='user-logout'),
    path('user-registration/', registration_form, name='user-registration'),


]
