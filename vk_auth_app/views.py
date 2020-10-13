from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from social_django.models import UserSocialAuth
from vk_api import VkApi


@login_required
def index(request):
    user_id = request.user.id
    try:
        user = UserSocialAuth.objects.get(user=user_id)
    except UserSocialAuth.DoesNotExist:
        return render(request, 'auth.html')

    user_token = user.access_token
    session = VkApi(token=user_token)
    api = session.get_api()
    friends = api.friends.get(count=6, fields=['first_name, last_name, photo_200'])
    return render(request, 'index.html', {'friends': friends['items']})
