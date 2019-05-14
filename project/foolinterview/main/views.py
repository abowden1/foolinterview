import sys
sys.path.append('..')



from django.shortcuts import render
from django.http import HttpResponse
from .utils import Articles, Quotes

def home(request):
    a = Articles()
    a.generate_content()
    context = {'title': 'Articles',
               'primary': a.primary,
               'secondary': a.secondary}
    return render(request, 'main/home.html', context=context)

def article(request, uuid):
    a = Articles()
    result = a.get_article_by_uuid(uuid=uuid)
    context = {'article': result,
               'quotes': Quotes().quotes}
    return render(request, 'main/article.html', context=context)


