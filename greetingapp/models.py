from django.db import models


class Visitor(models.Model):
	name = models.CharField('Ім\'я', max_length=50)
	surname = models.CharField('Прізвище', max_length=50)
