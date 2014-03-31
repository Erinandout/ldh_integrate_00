from django.contrib import admin

from .models import Chunk, Alert, Panel, Thumbnail


class ChunkAdmin(admin.ModelAdmin):
    pass


class AlertAdmin(admin.ModelAdmin):
    pass


class PanelAdmin(admin.ModelAdmin):
    pass


class ThumbnailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chunk, ChunkAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Panel, PanelAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)
