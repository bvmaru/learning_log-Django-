from django.db import models

class Topic(models.Model):
	"""temat poznawany przez użytkownika"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		"""Zwraca reprezentację modelu w postaci ciągu tekstowego"""
		return self.text

class Entry(models.Model):
	"""Konkretne informacje o postępie w nauce"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Zwraca reprezentację modelu w postaci ciągu tekstoewgo"""
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
		else:
			return self.text
