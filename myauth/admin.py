from django.contrib import admin

from .models import SignUpCode

class SignUpCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    list_filter = ('created_at',)

admin.site.register(SignUpCode, SignUpCodeAdmin)