from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth import get_user_model

ANSWER_TYPES = (
    ("TE", "TEXT FIELD"),
    ("NU", "NUMBER FIELD"),
    ("RA", "RADIO FIELD"),
    ("TA", "TEXT AREA"),
)

class Profile(models.Model):
    user = get_user_model()


# Create your models here.
class QuoteQuestion(models.Model):
    question = models.TextField()
    answer_type = models.CharField(choices=ANSWER_TYPES, max_length=2 )
    icon = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question


class ProjectCategory(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    customer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(ProjectCategory, related_name="projects")
    overview = models.TextField()
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(self, Project).save(self, *args, **kwargs)


class ProjectMedia():
    def project_directory_path(instance, filename):
        return f"projects/{instance.project.title}/{filename}"
    
    file = models.FileField(
        upload_to=project_directory_path, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'avi', 'mkv'])]
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="media")


class Quote(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="quotes")
    #TODO: Add the fields that will relate to the quotes

class LegendVideo(models.Model):
    def legend_directory_path(instance, filename):
        return f"legends/{filename}"
    file = models.FileField(
        upload_to=legend_directory_path, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'avi', 'mkv'])]
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    is_current = models.BooleanField(default=False)

    def get_current():
        return LegendVideo.objects.get(is_current = True)

