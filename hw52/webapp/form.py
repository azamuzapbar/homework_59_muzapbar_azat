from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='title')
    description = forms.CharField(max_length=3000, required=True, label='description' )
    detailed_view = forms.CharField(max_length=3500, required=True, label='description')
    status = forms.CharField(max_length=300,required=True)

