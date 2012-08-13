from django.db import models
from datetime import date


class Guest(models.Model):

    GUEST_CHOICES = ((x, x) for x in xrange(1, 7))
    DATE_CHOICES = (
        (date(2012, 10, 31), '10/31'),
        (date(2012, 11, 1), '11/1'),
        (date(2012, 11, 2), '11/2'),
        (date(2012, 11, 3), '11/3'),
    )
    name = models.CharField(max_length=255)
    party_size = models.PositiveIntegerField(choices=GUEST_CHOICES, default=1)
    arrival_date = models.DateField(choices=DATE_CHOICES,
                                    default=date(2012, 11, 3))
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
