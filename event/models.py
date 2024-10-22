from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=400, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    rsvp_url = models.URLField(max_length=500, null=True, blank=True)
    add_to_calender_url = models.URLField(
        max_length=500, null=True, blank=True
    )
    location = models.CharField(max_length=250, null=False, blank=False)
    is_draft = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hot_topics = models.ManyToManyField(
        "HotTopic",
        related_name="events",
        related_query_name="events",
    )

    def __str__(self):
        return self.title


class HotTopic(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    twitter = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)

    def __str__(self):
        return self.name


class Schedule(models.Model):

    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    # emojis have 2 length by default
    emoji = models.CharField(
        max_length=2,
        null=False,
        blank=False,
    )
    speakers = models.ManyToManyField(Speaker)

    def __str__(self):
        return f"Schedule from {self.start_time} to {self.end_time}"
