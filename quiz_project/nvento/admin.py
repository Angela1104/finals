from django.contrib import admin
from .models import Quiz, QuizQuestion, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of choices displayed in the admin form

class QuizQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Quiz)
admin.site.register(QuizQuestion, QuizQuestionAdmin)
# No need to register Choice, as it's included as an inline in QuizQuestionAdmin
