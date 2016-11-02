from django.contrib import admin
from .models import Member, Comment, Like, Media, HashTag, Follow

admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Media)
admin.site.register(HashTag)
admin.site.register(Follow)
