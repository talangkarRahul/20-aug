from django.contrib import admin

# Register your models here.
from apps.polls.models import Question
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class QuestionAdmin(ImportExportActionModelAdmin):
    list_display = ['question_text', 'user']


admin.site.register(Question, QuestionAdmin)
