from django.shortcuts import render
import requests

# Create your views here.


def test_view(request):
    r = requests.get("http://127.0.0.1:8000/api/profile/")

    content = r.json()
    print(len(content))
    context = {
        "users_qty": len(content),
        "user_data": content,
    }
    return render(request, 'profiles/test_view.html', context)

def add_view(request):
    r = requests.post("http://127.0.0.1:8000/api/profile/", data={'email': 'test2@test.ru', 'name': 'Test Client 2', 'password': 'test123'})
    print(r.url)

    context = {
        "user_name": 'Test Client 2',
        "user_email": 'test2@test.ru',
    }
    return render(request, 'profiles/add_view.html', context)

