from django.db import models
from datetime import date


class Guest(models.Model):

    GUEST_CHOICES = (
        (0, 'Regrets'),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )
    DATE_CHOICES = (
        (date(2012, 10, 31), '10/31'),
        (date(2012, 11, 1), '11/1'),
        (date(2012, 11, 2), '11/2'),
        (date(2012, 11, 3), '11/3'),
    )
    name = models.CharField(max_length=255)
    party_size = models.PositiveIntegerField(choices=GUEST_CHOICES, default=2)
    arrival_date = models.DateField(choices=DATE_CHOICES,
                                    default=date(2012, 11, 3), blank=True,
                                    null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
