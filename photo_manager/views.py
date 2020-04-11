from django.shortcuts import render
from django.views import generic

from photo_manager.models import *


class HomeView(generic.ListView):
    template_name = 'photo_manager/index.html'
    context_object_name = 'all_homepagephotos'

    def get_queryset(self):
        queryset = HomePagePhoto.objects.filter()
        return queryset


class AboutView(generic.ListView):
    template_name = 'photo_manager/about.html'
    context_object_name = 'about_info'

    def get_queryset(self):
        queryset = AboutInfo.objects.filter()
        return queryset


def PhotographyView(request):
    weddings = PhotographyPhoto.objects.filter(category="Weddings")
    cars = PhotographyPhoto.objects.filter(category="Cars")
    models = PhotographyPhoto.objects.filter(category="Models")
    events = PhotographyPhoto.objects.filter(category="Events")
    landscapes = PhotographyPhoto.objects.filter(category="Landscapes")
    visual_communication = PhotographyPhoto.objects.filter(category="Visual Communication")
    product_design = PhotographyPhoto.objects.filter(category="Product Design")
    portraits = PhotographyPhoto.objects.filter(category="Portraits")
    nature = PhotographyPhoto.objects.filter(category="Nature")

    return render(request, "photo_manager/photography.html", {
        'weddings': weddings,
        'cars': cars,
        'models': models,
        'events': events,
        'landscapes': landscapes,
        'visual_communication': visual_communication,
        'product_design': product_design,
        'portraits': portraits,
        'nature': nature,
    })


def WeddingView(request):
    weddings = PhotographyPhoto.objects.filter(category="Weddings")

    return render(request, "photo_manager/weddings.html", {
        'weddings': weddings
    })


def CarsView(request):
    cars = PhotographyPhoto.objects.filter(category="Cars")

    return render(request, "photo_manager/cars.html", {
        'cars': cars
    })


def ModelsView(request):
    models = PhotographyPhoto.objects.filter(category="Models")

    return render(request, "photo_manager/models.html", {
        'models': models
    })


def EventsView(request):
    events = PhotographyPhoto.objects.filter(category="Events")

    return render(request, "photo_manager/events.html", {
        'events': events
    })


def LandscapesView(request):
    landscapes = PhotographyPhoto.objects.filter(category="Landscapes")

    return render(request, "photo_manager/landscapes.html", {
        'landscapes': landscapes
    })


def VisualCommunicationView(request):
    visual_communication = PhotographyPhoto.objects.filter(category="Visual Communication")

    return render(request, "photo_manager/art.html", {
        'visual_communication': visual_communication
    })


def ProductDesignView(request):
    product_design = PhotographyPhoto.objects.filter(category="Product Design")

    return render(request, "photo_manager/design.html", {
        'product_design': product_design
    })


def PortraitView(request):
    portrait = PhotographyPhoto.objects.filter(category="Portraits")

    return render(request, "photo_manager/portraits.html", {
        'portraits': portrait
    })


def NatureView(request):
    nature = PhotographyPhoto.objects.filter(category="Nature")

    return render(request, "photo_manager/nature.html", {
        'nature': nature
    })


def PortfolioView(request):
    education = PortfolioEntry.objects.filter(category="Education")
    experience = PortfolioEntry.objects.filter(category="Experience")

    return render(request, "photo_manager/portfolio.html", {
        'education': education,
        'experience': experience,
    })
