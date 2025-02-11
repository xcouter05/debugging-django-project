from django.contrib import admin
from .models import blog, comments, reply, category, tag

# Register your models here.
admin.site.register(blog)
admin.site.register(comments)
admin.site.register(reply)
admin.site.register(category)
admin.site.register(tag)