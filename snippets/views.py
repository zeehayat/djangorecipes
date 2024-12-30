from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet
# Create your views here.

def snippet_list(request):
    snippets = Snippet.objects.all()
    snippet_list=','.join([snippet.title for snippet in snippets])
    return HttpResponse(f"List of Snippets: {snippet_list}")


