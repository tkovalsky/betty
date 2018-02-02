from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import reverse

from django_extensions.db.models import TimeStampedModel

class Profile(TimeStampedModel):
	user = models.OneToOneField('auth.User')
	phone_number = models.CharField(max_length=25, blank=True)

	def get_absolute_url(self):
		return reverse('edit-profile')


@receiver(post_save, sender=User)
def user_profile(sender, **kwargs):
	user = kwargs.get('instance')
	created = kwargs.get('created')
	if created:
		Profile.objects.create(user=user)
		