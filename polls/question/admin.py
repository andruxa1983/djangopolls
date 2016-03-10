from django.contrib import admin
from question.models import Question


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('request_num', 'status', 'created_at')
	list_filter = ['status']
	readonly_fields = (
		'request_num', 'title', 'text', 'created_at', 'full_name',
		 'phone_number', 'user_email'
	)

	def has_add_permission(self, perm):
		return False
# Register your models here.
admin.site.register(Question, QuestionAdmin)