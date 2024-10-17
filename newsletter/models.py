from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class NewsletterSubscriber(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(
        max_length=300, null=False, blank=False, unique=True, primary_key=True
    )

    is_active = models.BooleanField(
        default=True
    )  # Track active/inactive status

    unsubscribe_token = models.CharField(
        max_length=100, unique=True, default=uuid.uuid4
    )  # Unique unsubscribe token

    def __str__(self):
        return self.email
