from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title


class ReadBook(Book):
    date_completed = models.DateField()


class CodingPrinciplesBook(ReadBook):
    pass


class PersonalDevelopmentBook(ReadBook):
    pass


class ProfessionalDevelopmentBook(ReadBook):
    pass


class DesignBook(ReadBook):
    pass


class TechnologyBook(ReadBook):
    pass


class ReadingListBook(Book):
    pass