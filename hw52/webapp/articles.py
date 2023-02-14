from django.shortcuts import render, redirect
from webapp.models import Article

def add_view(request):
    if request.method == 'GET':
        return render(request, 'article_add.html')
    print(request.POST, "\n")
    article_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status')
    }
    article = Article.objects.create(**article_data)
    return redirect(f'/article/?pk={article.pk}')

def article_view(request):
    article_pk = request.GET.get('pk')
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'article_view.html', context=context)




