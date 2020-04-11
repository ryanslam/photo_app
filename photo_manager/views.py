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
    ocean = PhotographyPhoto.objects.filter(category="Ocean")
    gadgets = PhotographyPhoto.objects.filter(category="Gadgets")
    sky = PhotographyPhoto.objects.filter(category="Sky")
    wildlife = PhotographyPhoto.objects.filter(category="Wildlife")
    portraits = PhotographyPhoto.objects.filter(category="Portraits")
    urban = PhotographyPhoto.objects.filter(category="Urban")
    product_design = PhotographyPhoto.objects.filter(category="Product Design")
    forest = PhotographyPhoto.objects.filter(category="Forest")
    flower = PhotographyPhoto.objects.filter(category="Flower")

    return render(request, "photo_manager/photography.html", {
        'ocean': ocean,
        'gadgets': gadgets,
        'sky': sky,
        'wildlife': wildlife,
        'urban': urban,
        'forest': forest,
        'product_design': product_design,
        'portraits': portraits,
        'flower': flower,
    })


def ocean_view(request):
    ocean = PhotographyPhoto.objects.filter(category="Ocean")

    return render(request, "photo_manager/ocean.html", {
        'ocean': ocean
    })


def gadgets_view(request):
    gadgets = PhotographyPhoto.objects.filter(category="Gadgets")

    return render(request, "photo_manager/gadgets.html", {
        'gadgets': gadgets
    })


def sky_view(request):
    sky = PhotographyPhoto.objects.filter(category="Sky")

    return render(request, "photo_manager/sky.html", {
        'sky': sky
    })


def wildlife_view(request):
    wildlife = PhotographyPhoto.objects.filter(category="Wildlife")

    return render(request, "photo_manager/wildlife.html", {
        'wildlife': wildlife
    })


def forest_view(request):
    forest = PhotographyPhoto.objects.filter(category="Forest")

    return render(request, "photo_manager/forest.html", {
        'forest': forest
    })


def urban_view(request):
    urban = PhotographyPhoto.objects.filter(category="Urban")

    return render(request, "photo_manager/urban.html", {
        'urban': urban
    })


def product_design_view(request):
    product_design = PhotographyPhoto.objects.filter(category="Product Design")

    return render(request, "photo_manager/product_design.html", {
        'product_design': product_design
    })


def portrait_view(request):
    portrait = PhotographyPhoto.objects.filter(category="Portraits")

    return render(request, "photo_manager/portraits.html", {
        'portraits': portrait
    })


def flower_view(request):
    flower = PhotographyPhoto.objects.filter(category="Flower")

    return render(request, "photo_manager/flower.html", {
        'flower': flower
    })


def PortfolioView(request):
    education = PortfolioEntry.objects.filter(category="Education")
    experience = PortfolioEntry.objects.filter(category="Experience")

    return render(request, "photo_manager/portfolio.html", {
        'education': education,
        'experience': experience,
    })
