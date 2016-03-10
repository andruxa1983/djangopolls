# coding: utf-8
from __future__ import unicode_literals

from django.db import models
import random

STATUS_CHOICES = (
	('new', u'Новое обращение'),
	('published', u'Опубликованно'),
	('decline', u'Отклонен'),
	('duplicate', u'Дубликат'),
)


class Question(models.Model):
	request_num = models.IntegerField(u'Номер запроса', unique=True)
	title = models.CharField(u'Тема', max_length=255)
	text = models.TextField(u'Обращение')

	full_name = models.CharField(u'Имя пользователя', max_length=255)
	phone_number = models.CharField(u'Телефон', max_length=12, blank=True)
	user_email = models.EmailField(u'Email адресс')

	status = models.CharField(u'Статус', max_length=30, choices=STATUS_CHOICES)

	created_at = models.DateTimeField(u'Дата публикации', auto_now_add=True)
	updated_at = models.DateTimeField(u'Дата ответа', auto_now_add=True)

	#answer = models.TextField(u'Ответ:', null=True, blank=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.pk:
			self.request_num = 10 + random.randint(11, 9999)
			max_tries = 100
			request_num_not_unique = True
			while request_num_not_unique:
				self.request_num = 10 + random.randint(11, 9999)
				if max_tries == 0:
					# send message to tech staff
					break
				if Question.objects.filter(request_num=self.request_num).count() == 0:
					request_num_not_unique = False
				max_tries -= 1
			
		# try:
		# 	Question.objects.get(request_num=self.request_num)
		# 	super (Question, self).save(*args, **kwargs)
		# 	return
		# except Question.DoesNotExist:
		# 	self.request_num = 10 + random.randint(11, 9999)
		super (Question, self).save(*args, **kwargs)


			
# Create your models here.
