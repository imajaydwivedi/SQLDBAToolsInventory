from django.contrib import admin
from quiz.models import *
# Register your models here.


@admin.register(Questiontechnology)
class QuestiontechnologyAdmin(admin.ModelAdmin):
    list_display = ['technologyid', 'category',
                    'subcategory', 'level', 'description']
