from django.shortcuts import render
from .models import User, Project
from django.core.paginator import Paginator

def project_list(request):
    projects = Project.objects.all()  # Obtén todos los proyectos
    return render(request, 'project_list.html', {'projects': projects})

"""def project_list(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 10)  # 10 projects per page
    page_number = request.GET.get('page') # Get the page number from the request
    page_obj = paginator.get_page(page_number) # Get the projects for the current page
    # Render the template with the paginated projects
    return render(request, 'core/project_list.html', {'page_obj': page_obj})"""



