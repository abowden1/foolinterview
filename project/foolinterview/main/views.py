import sys
sys.path.append('..')

import json

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import Articles, Quotes
from .models import Article_Comments

def home(request):
    a = Articles()
    a.generate_content()
    context = {'title': 'Articles',
               'primary': a.primary,
               'secondary': a.secondary,
               'primary_image' : get_images([a.primary])[0]['primary_image'],
               'secondary_images': get_images(a.secondary)}
    return render(request, 'main/home.html', context=context)

def article(request, uuid):
    a = Articles()
    result = a.get_article_by_uuid(uuid=uuid)
    primary_image_url = result['images'][0]['url']
    author = result['authors'][0]['byline']
    comments = get_comments(uuid)

    context = {'article': result,
               'author': author,
               'header_image': primary_image_url,
               'quotes': Quotes().display_quotes,
               'comments' : comments}
    return render(request, 'main/article.html', context=context)

def get_images(articles):
    if not type(articles) == list:
        articles = [articles]

    results = []
    for article in articles:
        article['primary_image'] = article['images'][0]['url']
        results.append(article)
    return results

@csrf_exempt #simplification since we are allowing anonymous comments
def addcomment(request):
    data = json.loads(request.body.decode('utf8'))
    if request.method == 'POST':
        Article_Comments.objects.create(article_reference=data['uuid'], comment=data['comment'])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

def get_comments(uuid):
    try:
        comments = Article_Comments.objects.filter(article_reference=uuid)
    except:
        comments = None
    return comments