from django.shortcuts import render
import requests

# Create your views here.


def test_view(request):
    user_token = 'Token ' + request.session.get('token')
    user_header = {'Authorization': user_token}
    requestURL = "http://127.0.0.1:8000/api/profile/"
    user = request.session['user']

    r = requests.get(
        requestURL,
        headers=user_header,
    )

    # print(r.status_code)
    content = r.json()
    # print(content)
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

def login_view(request):
    email = 'test@test.ru'
    password = 'test123'
    r = requests.post("http://127.0.0.1:8000/api/login/", data={'username': email, 'password': password})
    status = r.status_code
    if status == 200:
        content = r.json()
        request.session['token'] = content['token']
        requestURL = "http://127.0.0.1:8000/api/profile/"
        user_token = 'Token ' + request.session.get('token')
        user_header = {'Authorization': user_token}

        r = requests.get(
            requestURL,
            headers=user_header,
        )
        users_list = r.json()
        user = [item for item in users_list if item['email'] == email][0]
        # user = next(item for item in users_list if item['email'] == email)
        # user = next(filter(lambda item: item['email'] == email, users_list))
        request.session['user'] = user
        message = 'Welcome, {}!'.format(request.session['user']['name'])
        # message = 'Welcome!'
    else:
        message = 'Access denied... Please, try again.'

    context = {
        'message': message,
        }
    return render(request, 'profiles/login_view.html', context)

