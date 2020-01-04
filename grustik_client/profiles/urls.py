from django.urls import path
import profiles.views as profiles

app_name = 'profiles'

urlpatterns = [
    path('test', profiles.test_view, name='test_view'),
]