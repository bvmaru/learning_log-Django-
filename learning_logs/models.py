from django.db import models

class Topic(models.Model):
	"""temat poznawany przez użytkownika"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		"""Zwraca reprezentację modelu w postaci ciągu tekstowego"""
		return self.text
