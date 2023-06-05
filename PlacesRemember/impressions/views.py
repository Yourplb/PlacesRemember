from django.shortcuts import render
from vk_api import VkApi
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'impressions/index.html')


@login_required
def vk_auth(request):
    user_social_auth = request.user.social_auth.get(provider='vk-oauth2')
    access_token = user_social_auth.extra_data['access_token']
    vk_id = user_social_auth.uid

    vk_session = VkApi(token=access_token)
    vk = vk_session.get_api()
    user_info = vk.users.get(user_ids=vk_id, fields='photo,photo_200,first_name,nickname')[0]
    user_name = user_info['first_name'] + ' ' + user_info['nickname']
    user_photo = user_info['photo_200']

    user_social_auth = request.user.social_auth.get(provider='vk-oauth2')
    if user_social_auth:
        extra_data = user_social_auth.extra_data
        photo_url = extra_data.get('photo_max_orig')
        name = extra_data.get('first_name')

    data = {
        'user_name': user_name,
        'user_photo': user_photo,
        'user_info': vk.users.get(user_ids=vk_id, fields='photo,photo_200,first_name,nickname'),
        'first_name': extra_data.get('first_name'),
        'photo_url': photo_url,
        'name': name,
    }

    return render(request, 'impressions_list.html', data)


@login_required
def impressions_list(request):
    return render(request, 'impressions/impressions_list.html')
