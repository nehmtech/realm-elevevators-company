from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.views import View
from .models import Help






def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # save the form data to the database
            form.save()

            # send the email
            subject = 'New contact request'
            message = 'Name: {}\nEmail: {}\nServices: {}\nSubject: {}'.format(
                form.cleaned_data['fullname'],
                form.cleaned_data['email'],
                form.cleaned_data['services'],
                form.cleaned_data['subject']
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]
            send_mail(subject, message, from_email, recipient_list)

            # redirect to a success page
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'contact_form.html', {'form': form})


def contact_success(request):
  return render(request, 'results_page.html')

def success(request):
  return render(request, 'success.html')






    


class ContactFormView(View):
    def get(self, request):
        return render(request, 'contactpage.html')
    
    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Help(name=name, phone=phone, email=email, subject=subject, message=message)
        contact.save()

        # Send email to a specified email address
        send_mail(
            f'New Contact from {name}',
            f'You have received a new contact message from {name} ({email}):\n\n{message}',
            email,
            ['info@realmelevators.com'], # Replace with your email address
            fail_silently=False,
        )

        return redirect('success')

