from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.template.loader import render_to_string
from django.core.mail import send_mail

from . import constants
from . import models

import ads


def add_navigation_urls(input_dictionary: dict = None):
    if input_dictionary:
        input_dictionary['BASE_API_URL'] = constants.BASE_API_URL
        input_dictionary['BASE_DATA_SHARING_PORTAL_URL'] = constants.BASE_DATA_SHARING_PORTAL_URL
        input_dictionary['BASE_ORIGINAL_BLUETIDES_URL'] = constants.BASE_ORIGINAL_BLUETIDES_URL
    else:
        input_dictionary = {
            'BASE_API_URL': constants.BASE_API_URL,
            'BASE_DATA_SHARING_PORTAL_URL': constants.BASE_DATA_SHARING_PORTAL_URL,
            'BASE_ORIGINAL_BLUETIDES_URL': constants.BASE_ORIGINAL_BLUETIDES_URL,
        }
    return input_dictionary


# Create your views here.
class Home(View):
    def get(self, request):
        template = loader.get_template('webapps/home.html')
        context = add_navigation_urls()
        return HttpResponse(template.render(context, request))

    post = get

class People(View):
    def get(self, request):
        template = loader.get_template('webapps/people.html')
        context = add_navigation_urls()
        return HttpResponse(template.render(context, request))
    def post(self, request):
        template = loader.get_template('webapps/people.html')

        context = {
            "contact_email": request.POST['email'],
            "contact_name": request.POST['name'],
            "contact_message": request.POST['message']
        }

        email_text = render_to_string('email.txt', context)
        email_html = render_to_string('email.html', context)

        send_mail(
            'Contact Form Submission - Bluetides',
            email_text,
            'do-not-reply@psc.edu',
            ['do-not-reply@domain.com'],
            html_message=email_html
        )

        context = add_navigation_urls()
        return HttpResponse(template.render(context, request))

class Results(View):
    def get(self, request):
        # Hit ADS API for results
        ads.config.token = constants.ADS_DEV_KEY
        papers = list(ads.SearchQuery(abstract="BlueTides"))

        template = loader.get_template('webapps/results.html')
        context = add_navigation_urls()
        context['papers'] = papers

        return HttpResponse(template.render(context, request))

    post = get

class Reference(View):
    def get(self, request):
        template = loader.get_template('webapps/api-reference.html')
        context = {
            'endpoints': models.Endpoint.objects.all(),
        }
        context = add_navigation_urls(input_dictionary=context)
        return HttpResponse(template.render(context, request))

    post = get


class Tutorial(View):
    def get(self, request):
        template = loader.get_template('webapps/tutorial.html')
        context = add_navigation_urls()
        return HttpResponse(template.render(context, request))

    post = get


class Structure(View):
    def get(self, request):
        template = loader.get_template('webapps/data-structure.html')
        context = add_navigation_urls()
        return HttpResponse(template.render(context, request))

    post = get


class DataAccess(View):
    def get(self, request):
        template = loader.get_template('webapps/data-access.html')
        context = add_navigation_urls()
        return HttpResponse(template.render(context, request))

    post = get


class About(View):
    def get(self, request):
        template = loader.get_template('webapps/about.html')
        context = add_navigation_urls()
        return HttpResponse(template.render(context, request))

    post = get

class Gallery(View):
    def get(self, request):
        template = loader.get_template('webapps/gallery.html')
        context = add_navigation_urls()
        return HttpResponse(template.render(context, request))

    post = get