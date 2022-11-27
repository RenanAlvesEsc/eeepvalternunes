from django.contrib import admin
from informatica.models import *

# Register your models here.
class NoticesAdmin(admin.ModelAdmin):
    pass
class HomeSlidesAdmin(admin.ModelAdmin):
    pass
class CategoriasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Notice, NoticesAdmin)
admin.site.register(HomeSlide, HomeSlidesAdmin)
admin.site.register(Categoria, CategoriasAdmin)
