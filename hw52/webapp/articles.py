from django.shortcuts import render, redirect
from django.urls import reverse
from webapp.models import Article

def add_view(request):
    if request.method == 'GET':
        return render(request, 'article_add.html')
    print(request.POST, "\n")
    article_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'detailed_view': request.POST.get('detailed_view')
    }
    article = Article.objects.create(**article_data)
    return redirect(reverse('detailed_view', kwargs={'pk': article.pk}))

def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context=context)




