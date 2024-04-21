from django.shortcuts import render
from django import views
from .models import CompareSlider, LegendVideo, Project, ProjectMedia, Testimonial

TEMPLATE_BASE = "promo/"

# Create your views here.
class HomeView(views.View):
    def get(self, *args, **kwargs):
        legend_video = LegendVideo.get_current()
        compare_slider = CompareSlider.get_current()
        featured_project = Project.get_feauted()
        featured_video = ProjectMedia.objects.filter(project=featured_project)
        featured_video = featured_video[0]
        testimonials = Testimonial.get_random_tesimonials()
        context = {
            "legend" : legend_video,
            "compare" : compare_slider,
            "featured" : featured_project,
            "featured_video" : featured_video,
            "testimonials" : testimonials

        }
        return render(self.request, f'{TEMPLATE_BASE}index.html', context)