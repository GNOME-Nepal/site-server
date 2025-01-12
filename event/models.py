from datetime import datetime
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify


class EventType(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class EventLocation(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    # it is nullable as the location may be not always findable
    google_maps_location = models.URLField(
        max_length=500, blank=True, null=True
    )

    def __str__(self):
        return self.name


class HotTopic(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


# Create your models here.
class Event(models.Model):
    slug = models.SlugField(
        max_length=350,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(max_length=400, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    requires_registration = models.BooleanField(default=False)
    rsvp_url = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(
        upload_to="%Y/%m/%d/events", null=True, blank=True
    )
    add_to_calender_url = models.URLField(
        max_length=500, null=True, blank=True
    )
    is_draft = models.BooleanField(default=False)
    max_capacity = models.IntegerField(
        null=False,
        blank=False,
    )
    # this is null to signify free events
    price = models.IntegerField(null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    registration_deadline = models.DateTimeField(null=False, blank=False)

    event_type = models.ForeignKey(
        EventType,
        null=True,
        on_delete=models.SET_NULL,
    )

    location = models.ForeignKey(
        "EventLocation",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )

    hot_topics = models.ManyToManyField(
        HotTopic,
        related_name="events",
        related_query_name="events",
    )

    def clean_start_date(self):
        """
        Validate the start date if it is in the past

        Raises:
            ValidationError: If the start date is in the past

        Returns:
            datetime: The valid start date
        """
        date_now = datetime.now().date()  # Convert to date

        if self.start_date.date() < date_now:  # Convert to date for comparison
            raise ValidationError("Start date cannot be in the past")

        return self.start_date

    def clean_end_date(self):
        """
        Validate the end date if it is in the past

        Raises:
            ValidationError: If the end date is in the past

        Returns:
            datetime: The valid end date
        """
        date_now = datetime.now().date()  # Convert to date

        if self.end_date.date() < date_now:  # Convert to date for comparison
            raise ValidationError("End date cannot be in the past")

        return self.end_date

    def clean_registration_deadline(self):
        """
        Validate the end date if it is in the past

        Raises:
            ValidationError: If the end date is in the past

        Returns:
            datetime: The valid end date
        """
        date_now = datetime.now().date()  # Convert to date

        if (
            self.registration_deadline.date() < date_now
        ):  # Convert to date for comparison
            raise ValidationError("Registration date cannot be in the past")

        return self.registration_deadline

    def clean(self):
        """
        Validate if the values are righly related to each other according
        to business later.

        Raises:
            ValidationError:
                - If start_date is greater than end date
                - If Registration deadline is greater than start_date

        Returns:
            None


        """
        super().clean()  # Ensure parent class's clean method is called

        # Check if start_date is greater than end_date
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be less than end date.")

        if self.registration_deadline:

            # Check if registration_deadline is greater than start_date
            if self.registration_deadline.date() > self.start_date:
                raise ValidationError(
                    "Registration deadline must be less than start date."
                )

        """
        validation if the participants exceeds the maximum capacity"""
        if self.participants.count() > self.max_capacity:
            raise ValidationError(
                "Participants cannot be more than the maximum capacity"
            )

    def save(self, *args, **kwargs):
        """
        We are overriding events save model
        so that we can create slug for the model once
        created.

        The slug is not changeable,
        if slug is changed, URL will be changed as well
        so for that reason, the slug will not be changed
        """
        if not self.slug:
            self.slug = slugify(self.title) + "-" + str(uuid4())[0:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    twitter = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    description = models.TextField(blank=False, null=True)
    image = models.ImageField(
        upload_to="%Y/%m/%d/speakers/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Schedule(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=False, null=True)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    # emojis have 2 length by default
    emoji = models.CharField(
        max_length=2,
        null=False,
        blank=False,
    )
    image = models.ImageField(
        upload_to="%Y/%m/%d/schedules/",
        null=True,
        blank=True,
    )
    speakers = models.ManyToManyField(Speaker)
    # location can be like "In building A, room number 5 etc"
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    def __str__(self):
        return f"Schedule from {self.start_time} to {self.end_time}"


class EventImage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="event_images",
        to_field="slug",
    )
    caption = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="%Y/%m/%d/event_images", null=True, blank=True
    )
    position = models.IntegerField(default=1)
    published = models.BooleanField(default=False)

    def __str__(self):
        return str(self.event)

    class Meta:
        ordering = ["position"]


class Participant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    academy = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                # makes sure the it is at least 10 and no more than 14
                regex=r"^\+?[0-9]{10,14}$",
                message=(
                    "Phone number must be 10 digit",
                    "long and  Up to 14 digits allowed including +977",
                ),
            )
        ],
    )
    events = models.ForeignKey(
        Event,
        related_name="participants",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    age = models.IntegerField(null=False, blank=False)

    def clean(self):
        """
        Do not allow saving the participant if the event is full.
        """
        if self.events.participants.count() >= self.events.max_capacity:
            raise ValidationError("Event is full")
        if not self.events:
            raise ValidationError("Event is required")

    def save(self, *args, **kwargs):
        # Call clean() before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name
