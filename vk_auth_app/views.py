from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.urls import reverse_lazy

from vk_api import VkApi


def index(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'index.html')

    user_token = user.social_auth.get().tokens
    session = VkApi(token=user_token)
    api = session.get_api()
    friends = api.friends.get(count=5, fields=['first_name, last_name, photo_200'])
    return render(request, 'index.html', {'friends': friends['items']})

def logout(request):
    auth_logout(request)
    return redirect(reverse_lazy('main_page'))