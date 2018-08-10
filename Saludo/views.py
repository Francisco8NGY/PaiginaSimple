from django.shortcuts import HttpResponse
from django.template import Context, loader

# Create your views here.
def HolaMundo(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
