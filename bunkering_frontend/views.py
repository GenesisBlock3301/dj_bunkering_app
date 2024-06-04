import logging
from django.shortcuts import render, redirect
from django.views import View
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from .helpers import get_bunker_fuels, get_services, get_check_input_values, get_country_list


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
        teamMembers = [
            {'name': "Mohammed Rafiqul Islam", 'designation': mark_safe("<b>Chairman</b>"),
             'img': '/assets/img/team/boss.jpeg',
             'bio': mark_safe("<b>Mohammed Rafiqul Islam</b> started his journey as a broker in Khatungonj, "
                              "Chittagong. Later on he joined Abul Khair Group and gathered many knowledges about Industry "
                              "handling, Import – Export, Trading and many more. He started his own Import – Export firm named"
                              " as RR Trading Corporation in 1980. After that he saw many problems in the bunkering Industry of "
                              "Bangladesh then he saw the opportunity to bring a better solution to the Industry then Sea "
                              "marine fuel suppliers & Co was established in 1990. Later He established Bricks manufacturing "
                              "company in 2008 and Real estate company named RR RAINBOW BD HOLDINGS LTD in 2021.")},
            {
                'name': "Mohammed Amanur Rashid", 'designation': mark_safe("<b>Managing partner</b>"),
                'img': "/assets/img/team/amanur.jpeg",
                'bio': mark_safe("<b>Md. Amanur Rashid</b> is a Marine Engineer by profession, before joining with us "
                                 "he served in American Bureau of Shipping (ABS), Singapore as Marine Surveyor. He was assigned in "
                                 "new building construction and successfully delivered three container ships and two offshore supply"
                                 " vessels as new construction surveyor. His career at a glance: After passing out from Marine "
                                 "Academy, Chittagong, Bangladesh in 1991 he joined Neptune Ship management services, Singapore "
                                 "as Assistant Engineer. He joined Anglo Eastern Ship management UK as a Second Engineer in 1998 "
                                 "and was promoted to the rank of Chief Engineer in 2003. He has enormous experience in Chemical"
                                 " Tanker, Crude Oil Tanker, Product Tanker and Bulk Carrier.Joined in Ocean Tankers Pte Ltd, "
                                 "Singapore, as Technical Superintendent in 2004. He also served DNV Petroleum Services Singapore,"
                                 " as Technical Advisor\n")},
            {'name': "Mohammed Rezaul Islam ", 'designation': mark_safe("<b>Managing director</b>"),
             'img': "/assets/img/team/rezaul.jpeg",
             'bio': mark_safe(
                 "<b>Mohammed Rezaul Islam</b> is a managing director of RR RAINBOW BD HOLDINGS LTD. He completed his "
                 "High School from the BAF SHAHEEN COLLEGE CHATTOGRAM in 2018. He later went on to complete his "
                 "undergraduate from the Independent University Bangladesh, in Bachelor of Business Administration ("
                 "Hons) with a major in Accounting and Finance. He is a big believer in technological innovation-led "
                 "development to increase efficiency within the work environment and the fostering of overall "
                 "organizational growth.")},
        ]
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


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        data = request.POST
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        subject = data.get('subject', '')
        try:
            send_mail(
                subject=subject,
                message=f"From: {name} ({email})\n\n{message}",  # Include sender details in message
                from_email=email,
                recipient_list=['freelancersifat380@gmail.com'],
                fail_silently=False,  # Raise an exception on failure
            )
            return redirect('contact')
        except Exception as e:
            # Handle email sending errors gracefully (e.g., log the error)
            logging.error(str(e))
            return render(request, 'contact.html', {'error_message': 'Email sending failed. Please try again later.'})


class TermsAndConditionView(View):
    def get(self, request):
        return render(request, 'terms_and_condition.html')
