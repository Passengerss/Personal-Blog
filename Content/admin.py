from django.contrib import admin
from .models import *
@admin.register(Contentinfo)
class ContentinfoAdmin(admin.ModelAdmin):
    list_display = ["id","title","author","ttype"]
    list_per_page = 10
    list_display_links = ["title"]
    list_filter = ["ttype","title","author"]
    search_fields = ("title","content","author__username","ttype__type")

    # def changelist_view(self, request, extra_context=None):
    #     user = request.user
    #     if user.is_superuser:
    #         self.list_display = ["id","title","author","ttype"]
    #     else:
    #         self.list_display = ["id","title","author"]
    #     return super(ContentinfoAdmin, self).changelist_view(request, extra_context=None)


@admin.register(Contenttype)
class ContenttypeAdmin(admin.ModelAdmin):
    list_display = ["id","type"]
    ordering = ["id"]


admin.site.site_title = "我的网站"
admin.site.site_url = None
admin.site.site_header = "欢迎光临"
admin.site.index_title = "Hello,Boys"