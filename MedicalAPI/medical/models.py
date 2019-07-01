from django.db import models

# Create your models here.

class Disease(models.Model):
	DiseaseName = models.CharField(max_length=50)

	DrName = models.SlugField()

	symptom = models.TextField()

	date = models.DateTimeField(auto_now_add=True)

	profilePicture = models.ImageField(default='default.png', blank=True)


	def __str__(self):
		return "> {}".format(self.DiseaseName)		#here we giving output to admin page from database

	def  sort_symptom(self):
		return self.symptom[:50] + ' .....'