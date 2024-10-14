from rest_framework import serializers
from .models import NewsletterSubscriber

class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email', 'name', 'is_active', 'subscription_date', 'last_sent', 'unsubscribe_token']
