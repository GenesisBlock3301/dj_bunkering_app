import logging
import os

from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.conf import settings
from .helpers import (get_bunker_fuels, get_services, get_check_input_values, get_country_list, get_team_members,
                      send_inquiry_email, get_sister_concern)

logger = logging.getLogger(__name__)

class HomeView(View):
    def get(self, request):
        our_sectors = get_services()
        context = {
            'header_title': 'Sea Marine Fuels Ltd - Leading Marine Fuel Supplier in Chittagong Port',
            'meta_description': 'Sea Marine Fuels Ltd provides high-quality marine fuel solutions, including LSMGO, '
                                'VLSFO, and HSD at Chittagong Port. Trusted partner for efficient marine operations',
            "our_sectors": our_sectors
        }
        return render(request, 'home.html', context=context)


class ConcernView(View):
    def get(self, request):
        sister_concern = get_sister_concern()
        context = {
            'header_title': "Our Commitment to Marine Fuel Solutions | Sea Marine Fuels Ltd",
            'meta_description': "Learn about our core values and concerns in providing reliable marine fuel services. "
                                "Focused on sustainability, compliance, and customer satisfaction.",
            'sister_concer': sister_concern
        }
        return render(request, 'concern.html', context=context)


class BunkeringView(View):
    def get(self, request):
        bunker_fuels = get_bunker_fuels()
        context = {
            "header_title": "LSMGO & VLSFO Bunkering Services in Chittagong Port | Sea Marine Fuels",
            'meta_description': "Reliable bunkering services for LSMGO 0.1%, VLSFO 0.5%, and HSD in Chittagong Port. "
                                "MARPOL-compliant, competitive pricing, and 24/7 delivery.",
            'bunker_fuels': bunker_fuels
        }
        return render(request, 'bunkering.html', context=context)


class TeamView(View):
    def get(self, request):
        teamMembers = get_team_members()
        context = {
            "header_title": "Meet Our Expert Team | Sea Marine Fuels Ltd",
            'meta_description': "Get to know the dedicated professionals behind Sea Marine Fuels Ltd. Our team ensures "
                                "exceptional service and fuel delivery for marine vessels.",
            'teamMembers': teamMembers
        }
        return render(request, 'team.html', context=context)


class FleetView(View):
    def get(self, request):
        context = {
            "header_title": "Our Advanced Marine Fleet | Sea Marine Fuels Ltd",
            'meta_description': "Explore our well-equipped marine fleet designed for efficient fuel delivery at"
                                " Chittagong Port. Ensuring reliability and safety."
        }
        return render(request, 'fleet.html', context=context)


class CareerView(View):
    def get(self, request):
        countryList = get_country_list()
        context = {
            "header_title": "Join Our Team | Career Opportunities at Sea Marine Fuels Ltd",
            'meta_description': "Looking for a career in the marine industry? Join Sea Marine Fuels Ltd and be part"
                                " of an innovative and professional team in marine fuel services.",
            'countryList': countryList
        }
        return render(request, 'career.html', context=context)

    def post(self, request):
        try:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            qualification = request.POST.get('qualification')
            experience = request.POST.get('experience')
            city = request.POST.get('city')
            zipcode = request.POST.get('zipcode')
            uploaded_file = request.FILES['form_file']
            # Send email
            subject = 'New Form Submission'
            to_email = settings.EMAIL_HOST_USER
            email_content = render_to_string('email_template/career_template.html', {
                'name': name,
                'mobile': mobile,
                'email': email,
                'qualification': qualification,
                'experience': experience,
                'city': city,
                'zipcode': zipcode
            })
            from_email = settings.DEFAULT_FROM_EMAIL
            email = EmailMessage(subject, email_content, from_email=from_email, to=[to_email])
            email.content_subtype = 'html'
            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            logger.info('Email sending....')
            email.send()
            logger.info('Email sent successfully')
            messages.success(request, 'Message successfully sent to admin')
        except Exception as e:
            logger.error('Error sending email: %s', e)
            messages.error(request, f"Sending message failed: {e}")
        return redirect('career')


class RequestQuotationView(View):
    def get(self, request):
        check_inputs_1 = get_check_input_values()[0]
        check_inputs_2 = get_check_input_values()[1]
        context = {
            "header_title": "Get a Quote for Marine Fuel Services | Sea Marine Fuels Ltd",
            'meta_description': "Request a quote for LSMGO, VLSFO, and HSD bunkering services at Chittagong Port. "
                                "Fast response and competitive pricing guaranteed.",
            'check_inputs_1': check_inputs_1,
            'check_inputs_2': check_inputs_2
        }
        return render(request, 'request_a_quote_form.html', context=context)

    def post(self, request):
        try:
            data = request.POST
            context = send_inquiry_email(data)
            subject = f"Inquiry from {context['company_name']}"
            html_message = render_to_string('email_template/quote_template.html', context)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = settings.EMAIL_HOST_USER
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
        context = {
            "header_title": "Contact Sea Marine Fuels Ltd | Marine Fuel Experts",
            'meta_description': "Reach out to Sea Marine Fuels Ltd for inquiries about marine fuel services. We're "
                                "here to assist you 24/7 for all your marine fuel needs."
        }
        return render(request, 'contact.html', context=context)

    def post(self, request):
        data = request.POST
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        subject = data.get('subject', '')
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = settings.EMAIL_HOST_USER
        if name and email and subject and message:
            email_subject = f"Contact Form: {subject} (from {name})"# Set the email message to use HTML
            email_body_html = render_to_string('email_template/contact_template.html', {
                'name': name, 'email': email, 'subject': subject, 'message': message,
            })
            try:
                email_message = EmailMessage(
                    subject=email_subject,
                    body=email_body_html,
                    from_email=from_email,
                    to=[to_email],
                )
                email_message.content_subtype = "html"
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
        context = {
            "header_title": "Terms & Conditions | Sea Marine Fuels Ltd",
            'meta_description': "Read the terms and conditions of using Sea Marine Fuels Ltd's services, including our "
                                "policies on fuel supply and customer agreements."
        }
        return render(request, 'terms_and_condition.html', context=context)
