import json

from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.db.models import Sum
from django.template.loader import render_to_string
from django.core.mail import send_mail

from . import constants
from . import models
from . import utils
from . import settings


def get_context():
    return {"MAIN_BLUETIDES_URL": constants.MAIN_BLUETIDES_URL}


class Home(View):
    def get(self, request):
        template = loader.get_template('home.html')
        context = {
            'simulations': models.Simulation.objects.all(),
            "BASE_API": settings.BASE_API,
            "BASE_COSMO": settings.BASE_COSMO
        }

        return HttpResponse(template.render(context, request))

    post = get


class Simulations(View):
    def get(self, request, pk):
        template = loader.get_template('simulation.html')
        simulation = models.Simulation.objects.filter(id=pk).first()
        snapshots = models.Snapshot.objects.filter(simulation_id=pk).prefetch_related('species_set', 'fof_group_set')

        if simulation:
            context = {
                'simulation': simulation,
                'snapshots': snapshots,
                "BASE_API": settings.BASE_API,
                "BASE_COSMO": settings.BASE_COSMO
            }

            if snapshots:
                related_sizes = {}
                for snapshot in snapshots:
                    species_size = 0
                    fof_group_size = 0
                    for row in snapshot.species_set.all():
                        species_size += row.folder_size
                    for row in snapshot.fof_group_set.all():
                        fof_group_size += row.folder_size
                    related_sizes[snapshot.id] = {
                        'species_set_size': species_size,
                        'fof_group_set_size': fof_group_size
                    }

                context['related_sizes'] = related_sizes
        else:
            context = get_context()

        return HttpResponse(template.render(context, request))

    post = get


class Snapshot(View):
    def get(self, request, pk):
        snapshot = models.Snapshot.objects.filter(id=pk).prefetch_related('species_set',
                                                                          'fof_group_set').first()
        if snapshot:
            species_size = 0
            fof_group_size = 0
            for row in snapshot.species_set.all():
                species_size += row.folder_size
            for row in snapshot.fof_group_set.all():
                fof_group_size += row.folder_size

            simulation = models.Simulation.objects.filter(id=snapshot.simulation_id).first()

            context = {
                "snapshot": snapshot,
                "simulation": simulation,
                "fof_group_size": fof_group_size,
                "species_size": species_size,
                "BASE_API": settings.BASE_API,
                "BASE_COSMO": settings.BASE_COSMO
            }
        else:
            context = get_context()
        template = loader.get_template('snapshot.html')
        return HttpResponse(template.render(context, request))

    post = get


class Fofgroups(View):
    def get(self, request, pk):
        snapshot = models.Snapshot.objects.filter(id=pk).prefetch_related('species_set',
                                                                          'fof_group_set').first()
        if snapshot:
            species_size = 0
            for row in snapshot.species_set.all():
                species_size += row.folder_size

            simulation = models.Simulation.objects.filter(id=snapshot.simulation_id).first()

            context = {
                "snapshot": snapshot,
                "simulation": simulation,
                "species_size": species_size,
                "BASE_API": settings.BASE_API,
                "BASE_COSMO": settings.BASE_COSMO
            }
        else:
            context = get_context()
        template = loader.get_template('fofgroups.html')
        return HttpResponse(template.render(context, request))

    post = get


class Species(View):
    def get(self, request, pk):
        snapshot = models.Snapshot.objects.filter(id=pk).prefetch_related('species_set',
                                                                          'fof_group_set').first()
        if snapshot:
            fof_group_size = 0
            for row in snapshot.fof_group_set.all():
                fof_group_size += row.folder_size

            simulation = models.Simulation.objects.filter(id=snapshot.simulation_id).first()

            context = {
                "snapshot": snapshot,
                "simulation": simulation,
                'fof_group_size': fof_group_size,
                "BASE_API": settings.BASE_API,
                "BASE_COSMO": settings.BASE_COSMO
            }
        else:
            context = get_context()
        template = loader.get_template('species.html')
        return HttpResponse(template.render(context, request))

    post = get


class DownloadModal(View):
    def get(self, request, file_requested=None):
        context = {'file_requested': file_requested}
        template = loader.get_template('email_modal.html')
        return HttpResponse(template.render(context, request))

    def post(self, request, file_requested=None):
        # Send an email with instructions

        file_requested_split = file_requested.split("-")

        file_requested = file_requested.replace("-", "_")
        data_folder = file_requested_split[0] + "_" + file_requested_split[1]

        context = {"data_folder": data_folder,
                   "data_file": file_requested + ".tar.gz"}
        template = loader.get_template('success_modal.html')
        email_text = render_to_string('email.txt', context)
        email_html = render_to_string('email.html', context)

        send_mail(
            'BlueTides Data',
            email_text,
            'do-not-reply@psc.edu',
            [request.POST['email-input']],
            html_message=email_html
        )

        return HttpResponse(template.render(context, request))
