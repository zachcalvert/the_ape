from django.db import models
from django.contrib.auth.models import User

from classes.models import ApeClass


class UserProfile(models.Model):
    """
    A user profile model for tracking additional user metadata.
    """
    user = models.OneToOneField(User, related_name='profile')

    # Used to enable a user's publicly accessible profile
    public = models.BooleanField(default=False)

    # Used to track how this user profile object was created
    source = models.CharField(max_length=10, default="admin")
    classes = models.ManyToManyField(ApeClass, through='ClassMember', related_name='students')

    def __str__(self):
        return u'%s <%s>' % (self.user.get_full_name(), self.user.email,)

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'user_id': self.user.pk})


class ClassMember(models.Model):
    student = models.ForeignKey(UserProfile, related_name='class_membership')
    ape_class = models.ForeignKey(ApeClass, related_name='class_membership', null=True)
    has_paid = models.BooleanField(default=False)
