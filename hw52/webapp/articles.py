from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Article
from webapp.form import ArticleForm


def add_view(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'article_add.html', context={'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                detailed_view=form.cleaned_data['detailed_view'],
            )
            return redirect('detailed_view', pk=article.pk)
        else:
            return render(request, 'article_add.html', context={'form': form})

def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context=context)


def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(initial={
            'title': article.title,
            'description': article.description,
            'status': article.status,
            'detailed_view':article.detailed_view
        })
        return render(request, 'article_update.html', context={'form': form, 'article': article})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.description = form.cleaned_data['description']
            article.status = form.cleaned_data['status']
            article.detailed_view = form.cleaned_data['detailed_view']
            article.save()
            return redirect('detailed_view', pk=article.pk)
        else:
            return render(request, 'article_update.html', context={'form': form, 'article': article})


def article_delete(requst, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(requst, 'confirm.html', context={'article': article})


def confirm(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')
