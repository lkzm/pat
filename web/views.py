from django.shortcuts import render
from web import models
def index (request):
    page = models.Page.objects.get(name = 'cs')
    content = models.Content.objects.filter(page__pk = page.pk)
    socials = models.Social.objects.all()
    bg = models.Background.objects.all()
    ut = models.UToken.objects.all()


    context = {
        'content' : content,
        'title' : page.title,
        'socials' : socials,
        'ut' : ut,
        'bg' : bg,

    }

    return  render(request, 'web/index.html', context)
# Create your views here.
