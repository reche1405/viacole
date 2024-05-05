from django.shortcuts import render
from django import views
from .models import CompareSlider, LegendVideo, Project, ProjectMedia, Testimonial,\
     Term, Page, AboutContent, Service
from .forms import RegistrationForm

TEMPLATE_BASE = "promo/"

# Create your views here.
class HomeView(views.View):
    def get(self, *args, **kwargs):
        legend_video = LegendVideo.get_current()
        compare_slider = CompareSlider.get_current()
        featured_project = Project.get_feauted()
        featured_video = ProjectMedia.objects.filter(project=featured_project)
        featured_video = featured_video[0]
        portfolio_slides =  Project.get_home_portfolio()
        testimonials = Testimonial.get_random_tesimonials()
        page_meta = Page.get_page("Home")
        context = {
            "legend" : legend_video,
            "compare" : compare_slider,
            "featured" : featured_project,
            "featured_video" : featured_video,
            "testimonials" : testimonials,
            "portfolio" : portfolio_slides,
            "meta" : page_meta

        }
        return render(self.request, f'{TEMPLATE_BASE}index.html', context)
    
class AboutView(views.View):
    def get(self, *args, **kwargs):
        meta = Page.get_page("About")
        about_content =  AboutContent.get_current()
        context = {
            'meta' : meta,
            'about' : about_content,
            
        }
        return render(self.request, f'{TEMPLATE_BASE}about.html', context )
    
class ServicesView(views.View):
    def get(self, *args, **kwargs):
        meta = Page.get_page("Services")
        services = Service.objects.all()
        context = {
            "meta" : meta,
            "services" : services
        }
        return render(self.request, f"{TEMPLATE_BASE}services.html", context)
    
class RegisterView(views.View):
    def get(self, *args, **kwargs):
        form = RegistrationForm()
        services = Service.objects.all()
        context = {
            'form' : form,
            'services' : services
        }
        return render(self.request,f"{TEMPLATE_BASE}register.html", context)
    def post(self, *args, **kwargs):
        form = RegistrationForm(self.request.POST)
        if form.is_valid():
            pass

    
class LoginView(views.View): 
    def get(self, *args, **kwargs): 
        form = RegistrationForm
        meta= Page.get_page("Login")
        context = {
            'meta' : meta,
            'form' : form
        }
        return render(self.request, f"{TEMPLATE_BASE}")
        pass


class TermsView(views.View):
    def get(self, *args, **kwargs):
        meta = Page.get_page("Terms")
        terms = Term.get_terms()
        context = {
            'meta' : meta,
            'terms' : terms,
        }
        return render(self.request, f"{TEMPLATE_BASE}terms.html", context)
    