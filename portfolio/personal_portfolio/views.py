from django.shortcuts import render
from blog.models import Post
from portfolio.models import EmailMessage


def home_page(request):
    post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:3]
    context = {'post': post}
    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html')

def service_page(request): 
    return render(request, 'services.html')

def contact_page(request):

    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']

    # Save to Database
        email_message = EmailMessage.objects.create (
        name = name,
        email = email,
        subject = subject,
        Message = message,
        )

        email_message.save()
        return render(request, 'contact.html')

    return render(request, 'contact.html')
