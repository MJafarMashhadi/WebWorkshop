from django.contrib import admin
from .models import Member, Comment, Like, Media, HashTag, Follow

admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(Like)

# Media.objects.filter(uploader__first_name__icontains='Mohammad')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['uploader', 'caption', 'created', 'first_name_has_s_in_it']
    # list_display_links = ['uploader', 'created']
    search_fields = ['caption', 'uploader__firstname', 'uploader__lastname', 'uploader__username']

    readonly_fields = ['uploader', 'file']
    fields = ('caption', ('uploader', 'file'), 'hash_tags')

    def first_name_has_s_in_it(self, row):
        if 's' in str(row.uploader):
            return 'Yes'
        else:
            return 'No'

admin.site.register(HashTag)
admin.site.register(Follow)
