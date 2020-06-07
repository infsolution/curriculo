from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Candidate(models.Model):
	name = models.CharField(max_length=100)
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate')

class Company(models.Model):
	name = models.CharField(max_length=100)
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
	candidates = models.ManyToManyField(Candidate)

class Address(models.Model):
	candidate = models.ForeignKey(Candidate, null=False, blank=False, on_delete=models.CASCADE, related_name='address')
	street = models.CharField(max_length=100, null=False)
	number = models.CharField(max_length=10)
	district = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=12)


class Phone(models.Model):
	code = models.CharField(max_length=5)
	number = models.CharField(max_length=20)
	candidate = models.ForeignKey(Candidate, null=False, blank=False, on_delete=models.CASCADE, related_name='phone')

class Curriculum(models.Model):
	candidate = models.ForeignKey(Candidate, null=False, blank=False, on_delete=models.CASCADE, related_name='curriculum')


class Academic(models.Model):
	curriculum = models.ForeignKey(Curriculum, null=False, blank=False, on_delete=models.CASCADE, related_name='academic')
	TYPE =(
		('fundamental', 'FUNDAMENTAL'),
		('tecnico', 'TÉCNICO'),
		('graduacao', 'GRADUAÇÃO'),
		('pos-graduacao', 'PÓS-GRADUAÇÃO'),
		)
	STATUS = (
		('incompleto', 'INCOMPLETO'),
		('cursando', 'CURSANDO'),
		('completo', 'COMPLETO'),
		)

	type_course = models.CharField(max_length=50, choices=TYPE, null=False, blank=False, default='fundamental')
	status = models.CharField(max_length=50, choices=STATUS, null=False, blank=False, default='incompleto')
	name = models.CharField(max_length=100)
	school = models.CharField(max_length=100)
	init_date = models.DateField()
	closing_date = models.DateField()
class Experience(models.Model):
	curriculum = models.ForeignKey(Curriculum, null=False, blank=False, on_delete=models.CASCADE, related_name='experience')
	company = models.CharField(max_length=100)
	office = models.CharField(max_length=100)
	init_date = models.DateField()
	closing_date = models.DateField()

class Skill(models.Model):
	curriculum = models.ForeignKey(Curriculum, null=False, blank=False, on_delete=models.CASCADE, related_name='skill')

class Objective(models.Model):
	curriculum = models.ForeignKey(Curriculum, null=False, blank=False, on_delete=models.CASCADE, related_name='objective')
	description = models.TextField()

class AdditionalEmail(models.Model):
	curriculum = models.ForeignKey(Curriculum, null=False, blank=False, on_delete=models.CASCADE, related_name='email')
	email = models.CharField(max_length=100) 

class Language(models.Model):
	STATUS = (
		('fluente', 'FLUENTE'),
		('avancado', 'AVANÇADO'),
		('intermediario', 'INTERMEDIÁRIO'),
		('basico', 'BÁSICO'),
		)
	curriculum = models.ForeignKey(Curriculum, null=False, blank=False, on_delete=models.CASCADE, related_name='language')
	name = models.CharField(max_length=100)
	status = models.CharField(max_length=50, choices=STATUS, null=False, blank=False, default='basico')

class Reference(models.Model):
	curriculum = models.ForeignKey(Curriculum, null=False, blank=False, on_delete=models.CASCADE, related_name='reference')
	name = models.CharField(max_length=100)
	office = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=50)