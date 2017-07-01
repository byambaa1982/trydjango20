from django.contrib import admin

# Register your models here.
from .models import Post
class PostModelAdmin(admin.ModelAdmin):  
	list_display = ["title", "updated", "timestamp"]  
 	list_display_links = ["updated"]  
	list_editable = ["title"]  	list_filter = ["updated", "timestamp"]  

admin.site.register(Post)  No newline at end of file  
	search_fields = ["title", "content"]  
	class Meta:  
 			model = Post  
