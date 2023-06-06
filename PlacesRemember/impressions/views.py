from django.shortcuts import render, redirect
from vk_api import VkApi
from django.contrib.auth.decorators import login_required
from .models import Impressions
from .forms import ImpressionsForm


def index(request):
    return render(request, 'impressions/index.html')


@login_required
def vk_auth(request):
    user_social_auth = request.user.social_auth.get(provider='vk-oauth2')
    access_token = user_social_auth.extra_data['access_token']
    vk_id = user_social_auth.uid

    vk_session = VkApi(token=access_token)
    vk = vk_session.get_api()
    user_info = vk.users.get(user_ids=vk_id, fields='photo,photo_200')[0]
    user_photo = user_info['photo_200']

    extra_data = user_social_auth.extra_data
    photo_url = extra_data.get('photo_max_orig')

    data = {
        'user_photo': user_photo,
        'user_info': vk.users.get(user_ids=vk_id, fields='photo,photo_200,first_name,nickname'),
        'first_name': extra_data.get('first_name'),
        'photo_url': photo_url,
    }

    return render(request, 'impressions_list.html', data)


@login_required
def impressions_list(request):

    impressions = Impressions.objects.filter(author=request.user)

    data = {
        'impressions': impressions,
    }

    return render(request, 'impressions/impressions_list.html', data)


@login_required
def impressions_create(request):
    if request.method == 'POST':
        form = ImpressionsForm(request.POST)
        if form.is_valid():
            impressions = form.save(commit=False)
            impressions.author = request.user
            impressions.save()
            return redirect('http://127.0.0.1:8000/impressions/')
    else:
        form = ImpressionsForm()

    data = {
        'form': form,
    }

    return render(request, 'impressions/impressions_create.html', data)
