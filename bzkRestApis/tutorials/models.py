from django.db import models


class Tutorial(models.Model):
    CRITICAL = 'CR'
    HIGH = 'HI'
    MEDIUM = 'MD'
    LOW = 'LO'
    INFORMATIVE = 'IN'

    LEVEL_CHOICES = (
        (CRITICAL, 'Critical'),
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
        (INFORMATIVE, 'Informative'),
    )

    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        default=MEDIUM,
    )
    published = models.BooleanField(default=False)
