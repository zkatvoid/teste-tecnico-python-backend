from django.contrib import admin

from foco.models import Foco


@admin.register(Foco)
class FocoAdmin(admin.ModelAdmin): ...
