from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='home'),  # URL principal para listar proyectos
    path('404/', views.error, name='error'),  # URL para manejar errores 404, name es el nombre de la vista que se va a llamar cuando se produzca un error 404
    path('base/', views.base, name='base'),  # URL para la vista base
    path('home/', views.home, name='home'),  # URL para la vista de inicio
    path('projects/', views.project_list, name='project_list'),
    path('projects/new/', views.project_create, name='project_create'),
    path('stakeholders/', views.stakeholder_finder, name='stakeholder_finder'),
    path('recommend/advisor/', views.advisor_recommendations, name='advisor_recommendations'),
    path('recommend/collaborator/', views.collaborator_recommendations, name='collaborator_recommendations'),
    path('profile/', views.profile, name='profile'),
    path('messages/', views.message_list, name='messages'),
    path('messages/<int:message_id>/', views.view_message, name='view_message'),
    path('messages/compose/', views.compose_message, name='compose_message'),
    #all_notifications
    path('notifications/', views.all_notifications, name='all_notifications'),  # URL para ver todas las notificaciones
    #profile_settings
    path('profile/settings/', views.profile_settings, name='profile_settings'),  # URL para la configuración del perfil
    #activity_log
    path('activity_log/', views.activity_log, name='activity_log'),  # URL para el registro de actividad
    #logout
    path('logout/', views.logout_view, name='logout'),  # URL para cerrar sesión
]