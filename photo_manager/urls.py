from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from photo_manager import views

app_name = "photo_manager"

urlpatterns = [
	path('', views.HomeView.as_view(), name='index'),
	path('about/', views.AboutView.as_view(), name='about'),
	path('photography/', views.PhotographyView, name='photography'),
	path('ocean/', views.ocean_view, name='ocean'),
	path('gadgets/', views.gadgets_view, name='gadgets'),
	path('sky/', views.sky_view, name='sky'),
	path('wildlife/', views.wildlife_view, name='wildlife'),
	path('forest/', views.forest_view, name='forest'),
	path('urban/', views.urban_view, name='urban'),
	path('product_design/', views.product_design_view, name='product_design'),
	path('portraits/', views.portrait_view, name='portraits'),
	path('flower/', views.flower_view, name='flower'),
	path('portfolio/', views.PortfolioView, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
