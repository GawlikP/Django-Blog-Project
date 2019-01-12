from django import forms

class CommentForm(forms.Form):
	autorInput = forms.CharField(label='autor',max_length=100)
	bodyInput = forms.CharField(label='comment',widget=forms.Textarea)
