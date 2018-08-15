from django.contrib import admin
from core.models import Movie, Person, Role


class RoleAdminInline(admin.TabularInline):
    model = Role
    extra = 0

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie
    inlines = [
        RoleAdminInline
    ]

admin.site.register(Person)
admin.site.register(Role)
