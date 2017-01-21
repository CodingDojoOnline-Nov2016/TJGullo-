from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
# Create your models here.
class EmailManager(models.Manager):
    def isValidEmail(self, data):
        errors = []
        email = data['email']

        if len(email) < 1:
            errors.append('email field must be filled out')
        elif not re.match(EMAIL_REGEX, email):
            errors.append('email must be valid')

        if errors:
            return [False, errors]
        else:
            email = self.create(email=email)
            print email
            return [True, email]

class Email(models.Model):
    email = models.EmailField()
    objects = EmailManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
