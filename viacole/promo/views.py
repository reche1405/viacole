from django.shortcuts import render, redirect
from django import views
from django.core.mail import EmailMessage
from django.conf import settings
from .models import CompareSlider, LegendVideo, Project, ProjectMedia, Testimonial,\
     Term, Page, AboutContent, Service, Profile, Category
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
        category_slides =  Category.get_home_cateogires()
        testimonials = Testimonial.get_random_tesimonials()
        page_meta = Page.get_page("Home")
        context = {
            "legend" : legend_video,
            "compare" : compare_slider,
            "featured" : featured_project,
            "featured_video" : featured_video,
            "testimonials" : testimonials,
            "categories" : category_slides,
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
        if not self.request.user.is_authenticated:
            return redirect("account_signup")        
        form = RegistrationForm()
        categories = Category.objects.all().order_by("-id")
        context = {
            'form' : form,
            'categories' : categories
        }
        return render(self.request,f"{TEMPLATE_BASE}register.html", context)
    def post(self, *args, **kwargs):
        form = RegistrationForm(self.request.POST)
        if form.is_valid():
            user = self.request.user
            if(Profile.user_profile_exists(user)):
                #TODO: Change this to a you already have an account page rather than home.
                return redirect("promo:home")
            profile = Profile.create_profile(self.request.user, form.cleaned_data)

            subject = "Welcome to VIACOLE - Verify your details."
            body = f""" 
            <!DOCTYPE html>
            <html lang="en-gb">
                <head>
                </head>
                <body style="background-color:#333333; color:#ffffff;">
                    <h1>Welcome</h1>
                    <p>Thank you for signing up to VIACOLE.</p>
                    <p>To verify your account, please follow the below link</p>
                    <a href="">VEERIFY MY ACCOUNT</a>
                    <p>Here at VIACOLE, we simplify the buying and selling process by
                    ensuring all of our clients</p>
                </body>
            </html>
            """
            to_list = [user.email]
            from_address = settings.EMAIL_HOST_USER
            msg = EmailMessage(subject,body, from_address, to_list)
            msg.content_subtype = "html"
            msg.send(fail_silently=False)
           #TODO: send the htnl email
            return redirect("promo:register-confirmation")
        else:
            print(f"{form.data}")
            services = Service.objects.all().order_by("-id")
            context = {
                "form" : form,
                "services" : services
            }
            return render(self.request,f"{TEMPLATE_BASE}register.html", context)

            
class RegisterConfirmationView(views.View):
    def get(self, *args, **kwargs):
        return render(self.request, f"{TEMPLATE_BASE}register-confirm.html")
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
    