from django.shortcuts import render
import requests

# Create your views here.


def test_view(request):
    print('start test_view')
    response = requests.get("http://127.0.0.1:8000/api/hello-view/")
    content = response.json()
    print(content)
    print("Код операции: ", response.status_code)
    return render(request, 'profiles/test_view.html', content)

