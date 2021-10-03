from django.shortcuts import render
from web import models
def index (request):
    page = models.Page.get(name = 'cs')
    content = models.Content.objects.filter(page__pk = page.pk)

    context = {
        'content' : content,
        'title' : page.title,

    }

    return  render(request, 'web/index.html', context)
# Create your views here.
