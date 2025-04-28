# SiiaLink - Proyecto Django

SiiaLink es un proyecto desarrollado con Django que tiene como objetivo gestionar proyectos y usuarios dentro de una plataforma.

## Requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.6 o superior
- Django 5.2 o superior

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/FrancoJOG/SiiaLink.git
    cd SiiaLink
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:
    - En Windows:
      ```bash
      venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Realiza las migraciones para configurar la base de datos:
    ```bash
    python manage.py migrate
    ```

6. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. Accede a la aplicación en tu navegador en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Estructura del proyecto

- `core/`: La aplicación principal que gestiona proyectos y usuarios.
- `templates/`: Plantillas HTML del proyecto.
- `static/`: Archivos estáticos (CSS, JavaScript, imágenes).
- `manage.py`: El archivo principal para gestionar el proyecto Django.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature-nueva`).
3. Realiza tus cambios.
4. Haz un commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
5. Empuja tus cambios (`git push origin feature-nueva`).
6. Crea un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
