import logging
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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


class RequestQuotationView(View):
    def get(self, request):
        check_inputs_1 = get_check_input_values()[0]
        check_inputs_2 = get_check_input_values()[1]
        return render(request, 'request_a_quote_form.html', context={
            'check_inputs_1': check_inputs_1,
            'check_inputs_2': check_inputs_2
        })

    def post(self, request):
        data = request.POST
        # company_name = data.get('company_name', '')
        # contact_person = data.get('contact_person', '')
        # telephobe = data.get('telephone', '')
        # email = data.get('email', '')
        # select_value_1 = data.get('select_value_1', '')
        # select_value_2 = data.get('select_value_1', '')
        # quantity = data.get('quantity', '')
        # vessel_name = data.get('vessel_name', '')
        # port = data.get('port', '')
        # birth_loc = data.get('birth_loc', '')
        # eda = data.get('eda', '')
        # eta = data.get('eta', '')
        # edd = data.get('etd', '')
        # etd = data.get('eta', '')
        # agent = data.get('agent', '')
        # message = data.get('message', '')
        try:
            context = send_inquiry_email(data)
            subject = f"Inquiry from {context['company_name']}"
            html_message = render_to_string('email_template/quote_template.html', context)
            # plain_message = strip_tags(html_message)
            from_email = context['email']
            to_email = 'freelancersifat380@gmail.com'

            email = EmailMessage(subject, html_message, from_email, [to_email])
            email.content_subtype = 'html'
            email.send()
        except Exception as e:
            logging.error('Error sending email: %s', e)
            messages.error(request, f"Sending message failed: {e}")
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
