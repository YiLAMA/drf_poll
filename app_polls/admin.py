from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Poll, Question, Options, Answer, User
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(User)
admin.site.register(Answer)
