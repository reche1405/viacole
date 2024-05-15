from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

ANSWER_TYPES = (
    ("TE", "TEXT FIELD"),
    ("NU", "NUMBER FIELD"),
    ("RA", "RADIO FIELD"),
    ("TA", "TEXT AREA"),
)




# Create your models here.
class QuoteQuestion(models.Model):
    question = models.TextField()
    answer_type = models.CharField(choices=ANSWER_TYPES, max_length=2 )
    icon = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question


# The third party services that are offered in partnership with viacole
class Service(models.Model):
    def service_upload(instance, filename):
        return f"services/{instance.title}/{filename}"
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to=service_upload, blank=True, null=True)
    display_order = models.IntegerField(unique=True, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    

# The categories of interest on the platform
class Category(models.Model):
    def category_upload(instance, filename):
        return f"categories/{instance.title}/{filename}"
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to=category_upload, blank=True, null=True)
    video = models.FileField(
        upload_to=category_upload, 
        validators=[FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'avi', 'mkv'])],                         
        blank=True, null=True
    )
    display_order = models.IntegerField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    def get_home_cateogires():

        categories = Category.objects.all().order_by("id")
        return categories

    def get_all():
        return Category.objects.all()

class Project(models.Model):
    customer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name="projects")
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
    
    def get_home_portfolio():

        projects = Project.objects.all().order_by("?")[0:4]
        return projects


class ProjectMedia(models.Model):
    def project_directory_path(instance, filename):
        return f"projects/{instance.project.slug}/{filename}"
    
    file = models.FileField(
        upload_to=project_directory_path, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'avi', 'mkv'])]
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="media")


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
    categories_one = models.ManyToManyField(Category, related_name='first_slide')

    image_two = models.ImageField(upload_to=slider_directory_path)
    title_two =models.CharField(max_length=100)
    info_two = models.TextField()
    categories_two = models.ManyToManyField(Category, related_name='second_slide')

    is_current = models.BooleanField(default=False)

    def get_current():
        return CompareSlider.objects.get(is_current=True)

    def __str__(self):
        return self.title_one

class Testimonial(models.Model):
    def testimonial_directory_path(instance, filename):
        return f"testimonials/{filename}"
    statement = models.TextField()
    client_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to=testimonial_directory_path)

    def get_random_tesimonials():
        return Testimonial.objects.all().order_by("?")[0:3]

    def __str__(self):
        return self.statement

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, editable=False)
    description = models.TextField(blank=True, null=True)
    keywords=models.TextField()
    tab_title = models.TextField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_page(page):
        try: 
            return Page.objects.get(title=page)
        except ObjectDoesNotExist as e:
            print(f"There has been an error as the following page: {page} does not exist.")


class BudgetRange(models.Model):
    from_value = models.IntegerField()
    to_value = models.IntegerField()

    def __str__(self):
        return f"{self.from_value} - {self.to_value}"
    


class AboutContent(models.Model):

    def upload_legend(instance, filename):
        return f"about/{filename}"
    
    about_legend = models.ImageField(upload_to=upload_legend)
    legend_title = models.CharField(max_length=100)
    legend_text = models.TextField()
    title_one = models.CharField(max_length=100, blank=True, null=True)
    text_one = models.TextField()
    title_two = models.CharField(max_length=100, blank=True, null=True)
    text_two = models.TextField(blank=True, null=True)
    title_three = models.CharField(max_length=100,  blank=True, null=True)
    text_three = models.TextField(blank=True, null=True)
    datetime_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_current = models.BooleanField(default=False)

    def get_current():
        try:
            return AboutContent.objects.get(is_current=True)
        except ObjectDoesNotExist as e:
            return None

    def save(self, *args, **kwargs): 
        if AboutContent.get_current():
            old_current = AboutContent.get_current()
            if old_current != self and self.is_current:
                old_current.is_current = False
                old_current.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ABOUT {self.datetime_added.strftime('%d%m%Y')}"

class Term(models.Model):
    title = models.CharField(max_length=200)
    section = models.IntegerField()
    sub_section = models.IntegerField()
    body = models.TextField()

    def get_terms():
        return Term.objects.all().order_by('section', 'sub_section')

    def __str__(self) -> str:
        if self.title: 
            return f"{self.section}.{self.sub_section} - {self.title}"
        return f"{self.section}.{self.sub_section}"
    
class FrequentlyAskedQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self) -> str:
        return self.question


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="profile", blank=True, null=True)
    phone_number = models.TextField(max_length=16, default="NOT PROVIDED")
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    buyers_budget = models.ForeignKey(
        BudgetRange,
        on_delete=models.DO_NOTHING,
        blank=True, null=True,
        related_name="buyers_profile"
    )
    sellers_budget = models.ForeignKey(
        BudgetRange,
        on_delete=models.DO_NOTHING,
        blank=True, null=True,
        related_name="sellers_profile"
    )
    interested_services = models.ManyToManyField(Category, related_name="buyers_profiles")
    interested_consignments  = models.ManyToManyField(Category, related_name="sellers_profiles")
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    
    def create_profile(user, data):

        
        profile = Profile.objects.create(
            user=user, phone_number=data["tel_num"], is_buyer=data['is_buyer'],
            is_seller=data['is_vendor'],                           
        )

        if data['is_buyer']:
            range_str = data["purchase_range"]
            range_arr = range_str.split(" - ")
            purchase_range = BudgetRange.objects.create(from_value=range_arr[0], to_value=range_arr[1])  
            purchase_range.save()
            profile.buyers_budget = purchase_range
        if data['is_vendor']:
            range_str = data["consignment_range"]
            range_arr = range_str.split(" - ")
            consignment_range = BudgetRange.objects.create(from_value=range_arr[0], to_value=range_arr[1])
            consignment_range.save()
            profile.sellers_budget = consignment_range
        profile.save()
        return profile
    
    def user_profile_exists(user):
        profile = Profile.objects.filter(user=user)
        return profile.exists()

class SocialMediaAccount(models.Model):
    base_url = models.URLField()
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    icon = models.TextField()

    def __str__(self):
        return self.name
    
    def get_full_url(self):
        return f"{self.base_url}/{self.tag}"