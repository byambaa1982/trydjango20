from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post 
# Create your views here.
def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}
	
	return render(request, "index.html", context)
def post_create(request):
	return HttpResponse("<h1>create byamba</h1>")
def post_detail(request):
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=3)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "index.html", context)
def post_update(request):
 	return HttpResponse("<h1>Hi Byambaa</h1>")
def post_delete(request):
 	return HttpResponse("<h1>Delete</h1>")