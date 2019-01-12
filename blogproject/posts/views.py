# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


from .models import Posts
from .models import Comments

from .forms import CommentForm

# Create your views here.

def index(request):

	posts = Posts.objects.all()[:10]

	context = {
	'title': 'Lastes Posts',
	'posts': posts,
	}

	#	return HttpResponse("Jebac policje");
	#	return render(request, 'posts/index.html');
	return render(request, 'posts/index.html', context);

def details(request,id):
	post = Posts.objects.get(id=id);
	comments = post.comments.all()
	form = None
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = Comments.objects.create(
			autor=form.cleaned_data['autorInput'],
			post=post,
			body=form.cleaned_data['bodyInput'],
			);
			#return HttpResponse('Added to base');

	else:
		form = CommentForm()
	
	context = {
		'post': post,
		'comments': comments,
		'form': form
	}

	return render(request, 'posts/details.html',context);
