from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Project
from django.contrib import messages  
from django.core.paginator import Paginator
#import forms
from .forms import ProjectForm


def project_list(request): #Esta es la vista que se encarga de mostrar la lista de proyectos
    projects = Project.objects.all()  # Obtén todos los proyectos
    return render(request, 'project_list.html', {'projects': projects})

def error(request):#EL nombbre de la funcion puede ser cualquier nombre que desees, pero es recomendable que sea descriptivo y relacionado con la funcionalidad de la vista
    return render(request, '404.html') #Abre la url :http://127.0. 0.1:8000/404/ para ver la vista de error 404

def base(request):
    return render(request, 'base.html') #Abre la url :http://127.0. 0.1:8000/base/ para ver la vista de base

def home(request):
    return render(request, 'home.html') #Abre la url :http://127.0. 0.1:8000/ para ver la vista de inicio

def project_create(request):
    if request.method == 'POST':
        # Aquí puedes manejar la creación de un nuevo proyecto
        pass  # Reemplaza esto con tu lógica de creación de proyecto
    return render(request, 'project_create.html')  # Renderiza la plantilla para crear un nuevo proyecto

def stakeholder_finder(request):
    if request.method == 'POST':
        # Aquí puedes manejar la búsqueda de interesados
        pass  # Reemplaza esto con tu lógica de búsqueda de interesados
    return render(request, 'stakeholder_finder.html')  # Renderiza la plantilla para buscar interesados

def advisor_recommendations(request):
    if request.method == 'POST':
        # Aquí puedes manejar las recomendaciones de asesores
        pass  # Reemplaza esto con tu lógica de recomendaciones de asesores
    return render(request, 'advisor_recommendations.html')  # Renderiza la plantilla para recomendaciones de asesores

def collaborator_recommendations(request):
    if request.method == 'POST':
        # Aquí puedes manejar las recomendaciones de colaboradores
        pass  # Reemplaza esto con tu lógica de recomendaciones de colaboradores
    return render(request, 'collaborator_recommendations.html')  # Renderiza la plantilla para recomendaciones de colaboradores

def profile(request):
    if request.method == 'POST':
        # Aquí puedes manejar la actualización del perfil
        pass  # Reemplaza esto con tu lógica de actualización de perfil
    return render(request, 'profile.html')  # Renderiza la plantilla para el perfil del usuario

#@login_required
def message_list(request):
    messages_list = messages.objects.filter(receiver=request.user).order_by('-sent_at')
    return render(request, 'messages/list.html', {
        'messages_list': messages_list,
        'unread_messages_count': messages.objects.filter(receiver=request.user, read=False).count()
    })

#@login_required
#def view_message(request, message_id): 
#    message = get_object_or_404(Message, id=message_id, receiver=request.user)
#    if not message.read:
#        message.read = True
#        message.save()
#    return render(request, 'messages/detail.html', {'message': message})

#Sin backend
def view_message(request, message_id):
    # Simula la lógica de obtener un mensaje por ID
    message = {
        'id': message_id,
        'sender': 'Juan',
        'subject': 'Reunión programada',
        'content': 'Hola, tenemos una reunión programada para mañana a las 10 AM.',
        'sent_at': '2023-10-01 12:00',
        'read': False
    }
    return render(request, 'messages/detail.html', {'message': message})



#@login_required
def compose_message(request):
    # Implementa la lógica para enviar mensajes
    pass

#all_notifications (sin backend)
def all_notifications(request):
    notifications = [
        {'id': 1, 'message': 'Nuevo proyecto disponible', 'timestamp': '2023-10-01 12:00'},
        {'id': 2, 'message': 'Nuevo mensaje de Juan', 'timestamp': '2023-10-02 14:30'},
        {'id': 3, 'message': 'Reunión programada para mañana', 'timestamp': '2023-10-03 09:00'},
    ]
    return render(request, 'notifications/all_notifications.html', {'notifications': notifications})

#profile_settings
def profile_settings(request):
    # Implementa la lógica para la configuración del perfil
    if request.method == 'POST':
        # Aquí puedes manejar la actualización de la configuración del perfil
        pass  # Reemplaza esto con tu lógica de actualización de configuración
    return render(request, 'profile_settings.html')  # Renderiza la plantilla para la configuración del perfil

#activity_log 
def activity_log(request):
    # Simula la lógica de obtener el registro de actividad
    activity_log = [
        {'timestamp': '2023-10-01 12:00', 'action': 'Creación de proyecto'},
        {'timestamp': '2023-10-02 14:30', 'action': 'Envío de mensaje'},
        {'timestamp': '2023-10-03 09:00', 'action': 'Actualización de perfil'},
    ]
    return render(request, 'activity_log.html', {'activity_log': activity_log})


#logout
def logout_view(request):
    # Implementa la lógica para cerrar sesión
    pass  # Reemplaza esto con tu lógica de cierre de sesión
#login

def login_view(request):
    # Implementa la lógica para iniciar sesión
    pass  # Reemplaza esto con tu lógica de inicio de sesión
#register

def register_view(request):
    # Implementa la lógica para registrar un nuevo usuario
    pass  # Reemplaza esto con tu lógica de registro de usuario

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, '¡Proyecto creado exitosamente!')
            return redirect('project_list')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = ProjectForm()
    
    return render(request, 'project_create.html', {'form': form})


















"""def project_list(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 10)  # 10 projects per page
    page_number = request.GET.get('page') # Get the page number from the request
    page_obj = paginator.get_page(page_number) # Get the projects for the current page
    # Render the template with the paginated projects
    return render(request, 'core/project_list.html', {'page_obj': page_obj})"""



    #request es el objeto que contiene la información de la solicitud HTTP como la URL, los parámetros, las cookies, etc.
    #Puedes acceder a los parámetros de la solicitud a través de request.GET o request.POST dependiendo del método HTTP utilizado
    #request.GET se utiliza para obtener los parámetros de la URL (método GET)
    #request.POST se utiliza para obtener los parámetros del cuerpo de la solicitud (método POST)
    #esto es una API RESTful, por lo que se espera que la vista devuelva un objeto JSON en lugar de una plantilla HTML

    #render es una función que se encarga de renderizar una plantilla HTML y devolverla como respuesta HTTP
    #Los parámetros que recibe son:
    #request: el objeto de la solicitud HTTP
    #template_name: el nombre dse la plantilla HTML que se va a renderizar
    #context: un diccionario que contiene los datos que se van a pasar a la plantilla
    
    #En este caso, se está pasando un diccionario con la clave 'projects' y el valor de la lista de proyectos obtenida de la base de datos
    #El método all() se utiliza para obtener todos los objetos de la tabla Project en la base de datos


    #Si quieres mostrar otro tipo de vista, puedes usar la siguiente función como ejemplo:
    #def project_list(request):
    #    projects = Project.objects.all()  # Obtén todos los proyectos
    #    return render(request, 'project_list.html', {'projects': projects})
    # Si quieres implementar paginación, puedes usar el siguiente código como ejemplo:  
