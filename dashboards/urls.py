from django.urls import path
from django.conf import settings
from dashboards.views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(template_name = 'pages/dashboards/index.html'), name='index'),
    
    path('<str:page>/list/', DashboardView.as_view(template_name = 'pages/apps/list.html'), name='list'),
    path('<str:page>/create/', DashboardView.as_view(template_name = 'pages/apps/create.html'), name='create'),
    path('<str:page>/detail/<slug:slug>/', DashboardView.as_view(template_name = 'pages/apps/detail.html'), name='detail'),
    path('<str:page>/edit/<slug:slug>/', DashboardView.as_view(template_name = 'pages/apps/edit.html'), name='edit'),
    path('<str:page>/delete/<slug:slug>/', DashboardView.as_view(template_name = 'pages/apps/delete.html'), name='delete'),

    path('error/<slug:slug>/', DashboardView.as_view(template_name = 'pages/system/error.html'), name='error'),
]