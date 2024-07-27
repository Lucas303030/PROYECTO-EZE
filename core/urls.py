from django.urls import path
from trackitems import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView, name='home'),
    path('tracking/<int:id>/', views.TrackingDetailView, name='tracking'),
    path('tracking/edit/<int:id>/', views.edit_tracking, name='edit_tracking'),
]
