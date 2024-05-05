from .models import SocialMediaAccount

def social_media(request):
    return {
        'social_accounts' : SocialMediaAccount.objects.all()
    }
