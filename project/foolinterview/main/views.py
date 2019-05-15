import sys
sys.path.append('..')

from django.shortcuts import render
from django.shortcuts import redirect
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
    try:
        comments = get_comments(uuid)
    except:
        comments = []
    context = {'article': result,
               'author': author,
               'header_image': primary_image_url,
               'quotes': Quotes().display_quotes,
               'comments' : comments}
    return render(request, 'main/article.html', context=context)

def shuffle(request):
    if request.method == 'GET':
        context = {'quotes' : Quotes().display_quotes}
        return render(request, 'main/new_quotes.html', context=context)
    else:
        return redirect('/')


def get_images(articles):
    if not type(articles) == list:
        articles = [articles]

    results = []
    for article in articles:
        article['primary_image'] = article['images'][0]['url']
        results.append(article)
    return results

def addcomment(request, comment):
    print("POSTED!")

def get_comments(uuid):
    return Article_Comments.objects.get(article_reference=uuid)

# get_comments('123es')