from django.db import models

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=255)
	summary = models.TextField()
	content = models.TextField()
	tfidf = models.TextField()
	entity = models.TextField()
	timestamp = models.DateTimeField()


	def __str__(self):
		return '%s of %s' % (self.content, self.tfidf, self.entity)
