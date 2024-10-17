from rest_framework import serializers
from .models import NewsletterSubscriber


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    unsubscribe_token = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = NewsletterSubscriber
        fields = [
            "email",
            "is_active",
            "unsubscribe_token",
        ]
