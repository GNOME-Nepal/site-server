# Register your models here.
from django.db.models import F, Count
from django.contrib import messages
from django import forms
from . import models
from core.base_admin import SummernoteModelAdmin, SummernoteInlineMixin
from django.contrib import admin
from django.utils.html import format_html
from nested_admin import NestedModelAdmin, NestedStackedInline


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["event", "start_time", "end_time"]
    search_fields = ["event", "start_time", "end_time"]


class EventScheduleInline(SummernoteInlineMixin, NestedStackedInline):
    model = models.Schedule
    extra = 1
    autocomplete_fields = ["speakers"]


class EventImagesInline(SummernoteInlineMixin, NestedStackedInline):
    model = models.EventImage
    extra = 1


class ParticipantsInline(SummernoteInlineMixin, NestedStackedInline):
    model = models.Participant
    extra = 0

    def get_extra(self, request, obj=None, **kwargs):

        if obj:  # Ensure we're dealing with an existing Event object
            if obj.participants.count() < obj.max_capacity:
                return 1  # Show one extra form
        return 0  # Don't show any extra forms

    def has_add_permission(self, request, obj=None):
        """
        Prevent adding new participants if the event is full.
        """
        if obj:  # Ensure we're dealing with an existing Event object
            if obj.participants.count() >= obj.max_capacity:
                messages.warning(
                    request,
                    "The event is full. You cannot add more participants.",
                )
                return False  # Hide "Add another" button
        return super().has_add_permission(request, obj)


class ParticipantAdminForm(forms.ModelForm):
    class Meta:
        model = models.Participant
        fields = "__all__"

    """
    Overriding the __init__ method to filter the events that are checked
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["events"].queryset = models.Event.objects.annotate(
            participant_count=Count("participants")
        ).filter(
            requires_registration=True, participant_count__lt=F("max_capacity")
        )  # Ensures max_capacity > p_count


class EventAdminForms(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = "__all__"
        help_texts = {
            "slug": "This is a unique identifier for the event",
            "title": "This is the title of the event",
            "start_date": "This is the date the event will start",
            "end_date": "This is the date the event will end",
            "description": "This is the description of the event",
            "requires_registration": "Check if the event needs registration",
            "rsvp_url": "This is the link to the RSVP page",
            "add_to_calender_url": "Add the event to your calendar",
            "is_draft": "This is the status of the event",
            "max_capacity": "This is the maximum capacity of the event",
            "price": "This is the price of the event",
            "registration_deadline": "This is the deadline for registration",
            "event_type": "What type of event is this",
            "location": "This is the location of the event",
            "hot_topics": "Keywords describing the event",
        }


@admin.register(models.Event)
class EventModelAdmin(NestedModelAdmin, SummernoteModelAdmin):
    form = EventAdminForms
    list_display = ["title", "is_draft", "start_date", "end_date"]
    search_fields = ["slug", "title"]
    readonly_fields = ["created_at", "updated_at", "slug"]
    inlines = [EventScheduleInline, EventImagesInline]
    autocomplete_fields = ["location", "event_type", "hot_topics"]

    """Overriding this method to conditionally
    add the ParticipantsInline to the inlines list
    """

    def get_inline_instances(self, request, obj=None):
        inline_instances = super().get_inline_instances(request, obj)
        if obj and obj.requires_registration:
            inline_instances.append(
                ParticipantsInline(self.model, self.admin_site)
            )
            return inline_instances


@admin.register(models.Speaker)
class SpeakersAdmin(SummernoteInlineMixin, admin.ModelAdmin):
    list_display = ["name", "profession", "linkedin", "twitter"]
    search_fields = ["name", "profession"]


@admin.register(models.EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(models.EventLocation)
class EventLocationAdmin(admin.ModelAdmin):
    list_display = ["name", "get_google_map_location"]
    search_fields = ["name"]

    def get_google_map_location(self, obj):
        return format_html(
            '<a href="{}" target="_blank">View on Google Maps</a>',
            obj.google_maps_location,
        )

    get_google_map_location.short_description = "Google Maps Location"


@admin.register(models.HotTopic)
class HotTopicAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(models.Participant)
class ParticipantAdmin(admin.ModelAdmin):
    form = ParticipantAdminForm
    list_display = [
        "first_name",
        "last_name",
        "email",
        "academy",
        "phone_number",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "academy",
        "phone_number",
    ]


admin.site.register(
    [
        models.EventImage,
    ],
    SummernoteModelAdmin,
)
