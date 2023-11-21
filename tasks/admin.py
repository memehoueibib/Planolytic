from django.contrib import admin
from .models import Task, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'due_date', 'assigned_to')
    list_filter = ('status', 'priority', 'due_date', 'assigned_to')
    search_fields = ('title', 'description')
    inlines = [CommentInline]

admin.site.register(Task, TaskAdmin)
