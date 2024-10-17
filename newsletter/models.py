from django.db import models
from django.utils import timezone
import uuid

# Custom Manager for active subscribers
class ActiveSubscriberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


# Create your models here.
class NewsletterSubscriber(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(
        max_length=300, 
        null=False, 
        blank=False, 
        unique=True, 
        primary_key=True
    )
    
    is_active = models.BooleanField(default=True)  # Track active/inactive status
    
    unsubscribe_token = models.CharField(
        max_length=100, 
        unique=True, 
        default=uuid.uuid4
    )  # Unique unsubscribe token
    
    subscription_date = models.DateTimeField(
        default=timezone.now, 
        editable=False
    )  # Subscription timestamp
    
    # Use the custom manager
    objects = models.Manager()  # Default manager
    active_subscribers = ActiveSubscriberManager()  # Manager for querying active subscribers

    def __str__(self):
        return self.email
