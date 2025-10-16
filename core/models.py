from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# =======================================
# FUNCIONES DE VALORES POR DEFECTO
# =======================================

def default_end_date():
    """Fecha de fin por defecto para proyectos."""
    return datetime.date(2099, 12, 31)

# =======================================
# OPCIONES (Choices) PARA CAMPOS
# =======================================

ACCOUNT_TYPE_CHOICES = (
    ('alumnoUDG', 'alumnoUDG'), #Credenciales siiau
    ('profesorUDG', 'profesorUDG'), #Credenciales siiau
    ('investigadorUDG', 'investigadorUDG'), #Credenciales siiau
    #('alumno', 'Alumno'),
    #('profesor', 'Profesor'), 
    #('investigador', 'Investigador'), 
    #('Empresa', 'Empresa'),
    #('externo', 'Externo'), #Empresario, estudiante o profesor de otra universidad
)

PROJECT_TYPE_CHOICES = (
    ('investigación', 'Investigación'),
    ('Modular', 'Modular'),
    ('Recreativo', 'Recreativo'),
    ('Independiente', 'Independiente'),
)
#En un proyecto modular solo puede ser asesor un profesor de udg y participar integrantes de udg
PROJECT_STATUS_CHOICES = (
    ('active', 'Activo'),
    ('completed', 'Completado'),
    #('abandonado', 'Abandonado'),
    #('Pausado', 'Pausado'),
)

ROLE_REQUIRED_CHOICES = (
    ('asesor', 'Asesor'),
    #('Coasesor', 'coasesor'),
    ('colaborador', 'Colaborador'),
    ('ExIntegrante', 'ExIntegrante'),
    #('Expulsado', 'Expulsado'),
    #('Desertor', 'Desertor'),
    ('Cliente', 'Cliente'),
    #('Patrocinador', 'Patrpcinador'),
)

# =======================================
# MODELOS DEL SISTEMA
# =======================================

class User(AbstractUser):
    # Extensión del modelo de usuario estándar
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPE_CHOICES,
        default='alumno'
    )

class Project(models.Model):
    # Proyecto de investigación o desarrollo
    title = models.CharField(max_length=100, default="Sin título")  # Título del proyecto
    description = models.TextField(default="Sin descripción")       # Descripción del proyecto
    area = models.CharField(max_length=100, default="Área desconocida")  # Área temática o de conocimiento
    objectives = models.TextField(default="Sin objetivos")          # Objetivos del proyecto
    keywords = models.CharField(max_length=100, default="Sin palabras clave")  # Palabras clave para búsqueda
    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPE_CHOICES,
        default='investigación'
    )   # Tipo de proyecto: investigación o desarrollo
    requirements = models.TextField(default="Sin requisitos")       # Requisitos para participar en el proyecto
    advisor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='advised_projects',
        null=True,
        blank=True
    )  # Asesor asignado al proyecto
    start_date = models.DateField(default=timezone.now)             # Fecha de inicio
    end_date = models.DateField(default=default_end_date)           # Fecha estimada de término
    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS_CHOICES,
        default='active'
    )   # Estado actual del proyecto (activo/completado)
    collaborators = models.ManyToManyField(
        User,
        related_name='collaborated_projects',
        blank=True
    )   # Usuarios colaboradores en el proyecto
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owned_projects',
        null=True,
        blank=True
    )   # Usuario propietario o responsable del proyecto
    is_open = models.BooleanField(default=True)                    # ¿El proyecto está abierto para nuevos miembros?
    role_required = models.CharField(
        max_length=20,
        choices=ROLE_REQUIRED_CHOICES,
        blank=True,
        null=True
    )   # Rol que se requiere para participar en este proyecto

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} - {self.sender} to {self.receiver}"

    class Meta:
        ordering = ['-sent_at']


