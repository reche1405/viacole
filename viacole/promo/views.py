from django.shortcuts import render, redirect
from django import views
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import CompareSlider, LegendVideo, Project, ProjectMedia, Testimonial,\
     Term, Page, AboutContent, Service, Profile, Category
from .forms import RegistrationForm
import requests, json



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
    
class CategoriesView(views.View):
    def get(self, *args, **kwargs):
        meta = Page.get_page("Categories")
        categories = Category.get_all()
        context = {
            meta : "meta",
            "categories" : categories
        }
        return render(self.request, f"{TEMPLATE_BASE}categories.html", context)
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

            url = settings.CHECKBOARD_BASE_URL
            payload = {
                "client_id" : settings.CHECKBOARD_CLIENT_ID,
                "phone" : profile.phone_number,
                "bundle_id" : settings.CHECKBOARD_BUNDLE_ID,
                "user_id" : profile.id,
                "email" : user.email,
            }
            headers = {
                "Authorization" : f"Bearer {settings.CHECKBOARD_BEARER_TOKEN}",
                "Accept" : "application/json"
            }
            try:
                response = requests.request("POST", url=url, headers=headers, data=payload)
                result = response.json()
                if response["Status"] == "Created":
                    messages.add_message(self.request, messages.SUCCESS, "Account Created. Please keep an eye out for a verification text.")
                    return redirect("promo:register-confirmation")

            except Exception as e:
                messages.add_message(self.request, messages.ERROR, "There was an error trying to verify your details. Please try again.")
                return redirect("promo:register")
                print(e)
            """ subject = "Welcome to VIACOLE - Verify your details."
            body = f   #Would need to add back in triple quoutes
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
            #Would need to add back in triple quoutes
            to_list = [user.email]
            from_address = settings.EMAIL_HOST_USER
            msg = EmailMessage(subject,body, from_address, to_list)
            msg.content_subtype = "html"
            msg.send(fail_silently=False) """
           #TODO: send the htnl email
        else:
            messages.add_message(self.request, messages.ERROR, "There was an error creating your account, Please try again.")
            return redirect("promo:register")

            
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
    