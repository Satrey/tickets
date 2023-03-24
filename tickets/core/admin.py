from django.contrib import admin
from .models import Theme, Ticket, Question, Answer


class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 0


class ThemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class TicketAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]
    ordering = ('theme', 'number')
    list_filter = ['theme']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    ordering = ('theme',)
    list_filter = ['theme', 'ticket']
    search_fields = ['text', 'theme', 'number']


# class AnswerAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer, AnswerAdmin)
