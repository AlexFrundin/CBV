from django.contrib import admin
from core.models import Movie, Person, Role


class RoleAdminInline(admin.TabularInline):
    model = Role
    extra = 0
    # fieldsets = (
    #     (None,{
    #         'fields':()
    #
    #     }),
    #     ('Advanced',{
    #         'classes': ('collapse',),
    #         'fields':('person', 'name')
    #     }),
    # )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie
    inlines = [
        RoleAdminInline
    ]




admin.site.register(Person)
admin.site.register(Role)
