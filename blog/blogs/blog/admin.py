from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import SomeModel

# Apply summernote to all TextField in model.
class BlogpostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)

admin.site.register(Blogpost, BlogpostAdmin)
# Register your models here.
