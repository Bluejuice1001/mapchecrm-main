from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
 # mapche_key = models.UUIDField(null=True, blank=True, editable=True, unique=True)
  mapche_key = models.CharField(max_length=36, blank=True, null=True)

  def __str__(self):
    return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)