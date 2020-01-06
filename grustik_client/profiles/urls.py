from django.urls import path
import profiles.views as profiles

app_name = 'profiles'

urlpatterns = [
    path('test/', profiles.test_view, name='test_view'),
    path('add/', profiles.add_view, name='add_view'),
    path('login/', profiles.login_view, name='login_view'),
]

