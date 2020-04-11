from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from photo_manager import views

app_name = "photo_manager"

urlpatterns = [
	path('', views.HomeView.as_view(), name='index'),
	path('about/', views.AboutView.as_view(), name='about'),
	path('photography/', views.PhotographyView, name='photography'),
	path('weddings/', views.WeddingView, name='weddings'),
	path('cars/', views.CarsView, name='cars'),
	path('models/', views.ModelsView, name='models'),
	path('events/', views.EventsView, name='events'),
	path('landscapes/', views.LandscapesView, name='landscapes'),
	path('art/', views.VisualCommunicationView, name='art'),
	path('design/', views.ProductDesignView, name='design'),
	path('portraits/', views.PortraitView, name='cars'),
	path('nature/', views.NatureView, name='nature'),
	path('portfolio/', views.PortfolioView, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
