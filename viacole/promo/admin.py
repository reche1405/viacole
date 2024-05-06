from django.contrib import admin
from .models import LegendVideo, CompareSlider, Service,\
Project, ProjectMedia, Testimonial, Page, BudgetRange,\
AboutContent, FrequentlyAskedQuestion, Term, SocialMediaAccount, Profile
# Register your models here.

admin.site.register(LegendVideo)
admin.site.register(CompareSlider)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ProjectMedia)
admin.site.register(Profile)
admin.site.register(Testimonial)
admin.site.register(Page)
admin.site.register(BudgetRange)
admin.site.register(AboutContent)
admin.site.register(FrequentlyAskedQuestion)
admin.site.register(Term)
admin.site.register(SocialMediaAccount)