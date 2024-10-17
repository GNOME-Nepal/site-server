from django.urls import path
from .views import NewsletterCreateView, UnsubscribeView

urlpatterns = [
    # Route for creating a new subscription
    path(
        "subscribe/", NewsletterCreateView.as_view(), name="newsletter-create"
    ),
    # Route for unsubscribing using a unique token
    path(
        "unsubscribe/<str:unsubscribe_token>/",
        UnsubscribeView.as_view(),
        name="unsubscribe",
    ),
]
