import logging
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .helpers import (get_bunker_fuels, get_services, get_check_input_values, get_country_list, get_team_members,
                      send_inquiry_email)


class HomeView(View):
    def get(self, request):
        our_sectors = get_services()
        return render(request, 'home.html', context={
            "our_sectors": our_sectors
        })


class BunkeringView(View):
    def get(self, request):
        bunker_fuels = get_bunker_fuels()
        return render(request, 'bunkering.html', context={
            'bunker_fuels': bunker_fuels
        })


class TeamView(View):
    def get(self, request):
        teamMembers = get_team_members()
        return render(request, 'team.html', context={
            'teamMembers': teamMembers
        })


class CareerView(View):
    def get(self, request):
        countryList = get_country_list()
        return render(request, 'career.html', context={
            'countryList': countryList
        })

    def post(self, request):
        try:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            qualification = request.POST.get('qualification')
            experience = request.POST.get('experience')
            city = request.POST.get('city')
            zipcode = request.POST.get('zipcode')
            # Handle file upload
            uploaded_file = request.FILES['form_file']
            file_name = default_storage.save(uploaded_file.name, ContentFile(uploaded_file.read()))
            file_url = default_storage.url(file_name)
            full_file_url = request.build_absolute_uri(file_url)

            # Send email
            subject = 'New Form Submission'
            to_email = 'freelancersifat380@gmail.com'
            email_content = render_to_string('email_template/career_template.html', {
                'name': name,
                'mobile': mobile,
                'email': email,
                'qualification': qualification,
                'experience': experience,
                'city': city,
                'zipcode': zipcode,
                'file_url': full_file_url,
            })
            email = EmailMessage(subject, email_content, to=[to_email])
            email.content_subtype = 'html'
            email.send()
            messages.success(request, 'Message successfully sent to admin')
        except Exception as e:
            logging.error('Error sending email: %s', e)
            messages.error(request, f"Sending message failed: {e}")
        return redirect('career')


class RequestQuotationView(View):
    def get(self, request):
        check_inputs_1 = get_check_input_values()[0]
        check_inputs_2 = get_check_input_values()[1]
        return render(request, 'request_a_quote_form.html', context={
            'check_inputs_1': check_inputs_1,
            'check_inputs_2': check_inputs_2
        })

    def post(self, request):
        try:
            data = request.POST
            context = send_inquiry_email(data)
            subject = f"Inquiry from {context['company_name']}"
            html_message = render_to_string('email_template/quote_template.html', context)
            from_email = context['email']
            to_email = 'freelancersifat380@gmail.com'
            email = EmailMessage(subject, html_message, from_email, [to_email])
            email.content_subtype = 'html'
            email.send()
            messages.success(request, 'Quotation send successfully.')
        except Exception as e:
            logging.error('Error sending email: %s', e)
            messages.error(request, f"Sending sending quotation failed: {e}")
        return redirect(reverse_lazy('quote'))


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        data = request.POST
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        subject = data.get('subject', '')
        if name and email and subject and message:
            email_subject = f"Contact Form: {subject} (from {name})"
            email_body_html = render_to_string('email_template/contact_template.html', {
                'name': name, 'email': email, 'subject': subject, 'message': message,
            })
            try:
                email_message = EmailMessage(
                    subject=email_subject,
                    body=email_body_html,
                    from_email=email,
                    to=['freelancersifat380@gmail.com'],
                )
                email_message.content_subtype = "html"  # Set the email message to use HTML
                email_message.send(fail_silently=False)
                messages.success(request, 'Message successfully sent to admin')
            except Exception as e:
                logging.error('Error sending email: %s', e)
                messages.error(request, f"Sending message failed: {e}")
        else:
            messages.error(request, 'Fill all mandatory field.')
        return redirect(reverse_lazy('contact'))


class TermsAndConditionView(View):
    def get(self, request):
        return render(request, 'terms_and_condition.html')
