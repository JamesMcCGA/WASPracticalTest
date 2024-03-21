from django.contrib import admin
from .models import Student, Cat

class CatInline(admin.TabularInline):
    model = Cat

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [CatInline]

admin.site.register(Cat)