from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
# Register your models here.
 