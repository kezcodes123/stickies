from django.db import models


# Create your models here.
class Sticky(models.Model):
    """
    Represents a sticky note in the application.
    This model stores the basic information needed for each note.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        """
        Returns a string representation of the sticky note.
        This helps identify the sticky note in the admin interface.
        """
        return self.name
