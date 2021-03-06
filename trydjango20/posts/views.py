from urllib.parse import quote_plus
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm 
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def post_list(request):
	queryset_list = Post.objects.all() #.order_by("-timestamp")
	paginator = Paginator(queryset_list, 10)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try: 
		queryset=paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset=paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var
	}
	
	return render(request, "post_list.html", context)
def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Profile details updated.')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
def post_detail(request, id=None):
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id)
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", context)
def post_update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_form.html", context)
def post_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")