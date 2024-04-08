from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

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


class Service(models.Model):
    title = models.CharField(max_length=30)
    descritption = models.TextField()

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    customer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    services = models.ManyToManyField(Service, related_name="projects")
    overview = models.TextField()
    slug = models.SlugField(unique=True, editable=False, blank=True)
    is_featured = models.BooleanField(default=False)

    def get_feauted():
        return Project.objects.get(is_featured=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.is_featured:
            try:
                old_featured =  Project.get_feauted()
            except ObjectDoesNotExist as e:
                print(e)
            else:
                if not old_featured == self:
                    old_featured.is_featured = False
                    old_featured.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectMedia():
    def project_directory_path(instance, filename):
        return f"projects/{instance.project.slug}/{filename}"
    
    file = models.FileField(
        upload_to=project_directory_path(), null=True,
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
    title = models.CharField(max_length=100, default="Current Video")
    info = models.TextField()
    file = models.FileField(
        upload_to=legend_directory_path, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'avi', 'mkv'])]
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    is_current = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def get_current():
        return LegendVideo.objects.get(is_current = True)


class CompareSlider(models.Model):
    def slider_directory_path(instance, filename):
        return f"compare/{instance.id}/{filename}"
    image_one = models.ImageField(upload_to=slider_directory_path)
    title_one = models.CharField(max_length=100)
    info_one = models.TextField()
    services_one = models.ManyToManyField(Service, related_name='first_slide')

    image_two = models.ImageField(upload_to=slider_directory_path)
    title_two =models.CharField(max_length=100)
    info_two = models.TextField()
    services_two = models.ManyToManyField(Service, related_name='second_slide')

    is_current = models.BooleanField(default=False)

    def get_current():
        return CompareSlider.objects.get(is_current=True)

    def __str__(self):
        return self.title_one

