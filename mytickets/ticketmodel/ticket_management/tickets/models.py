from django.db import models
from django.utils import timezone

# class Tickets(models.Model):
#     TICKET_TYPES = [
#         ('Type1', 'Type 1'),
#         ('Type2', 'Type 2'),
#         ('Type3', 'Type 3'),
#     ]
class Tickets(models.Model):
    TICKET_TYPES = (
        ("ASAP", "ASAP"),
        ("FUTURE", "FUTURE")
    )
    type = models.CharField(max_length=10, choices=TICKET_TYPES)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
