from django.shortcuts import render
from django import views
from .models import LegendVideo

TEMPLATE_BASE = "promo/"

# Create your views here.
class HomeView(views.View):
    def get(self, *args, **kwargs):
        home_video = LegendVideo.get_current()
        context = {
            "legend" : home_video.file.url
        }
        return render(self.request, f'{TEMPLATE_BASE}index.html', context)