from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from .models import NewsletterSubscriber
from .serializers import NewsletterSubscriberSerializer


# View for creating a new newsletter subscription
class NewsletterCreateView(CreateAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer


# View for unsubscribing using the unique unsubscribe token
class UnsubscribeView(UpdateAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    lookup_field = "unsubscribe_token"

    def update(self, request, *args, **kwargs):
        subscriber = self.get_object()
        subscriber.is_active = False
        subscriber.save()
        return Response(
            {
                "message": "Unsubscribed Successfully",
            }
        )
