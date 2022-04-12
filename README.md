# ProjectGuadaFit

Sitio Guada Fitness




[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Flujo de Proyecto

Nombre del Proyecto: ProjectGuadaFit

Descarga de Django Cookiecutter

Instalacion de requerimientos

Migracion de base de datos pre configuradas

Creamos la app students

Dentro de la carpeta students en el archivo models.py tenemos tres diferentes clases.

La primer clase son los datos principales del alumno 
La segunda clase son datos personales
La tercera clase datos extra

Todos los models se encuentran migrados a la base de datos
La base de datos utilizada es la de posgres SQL Elephantp

Tenemos la ruta principal denominada 'rutas' que nos lleva a la pagina principal del proyecto

Alli en la barra de navegacion cuando hacemos click en  registro (navegacion entre templates) se nos abre otra pagina 
(herencia de templates) con el formulario para que el alumno registre su nombre, apellido y direccion.

Para chequear el ingreso de estos datos en la DB, dentro de Visual S Code descargue el paquete DataClient

Retornando a la ruta principal "rutas" haciendo click en registro podemos acceder al formulario de busqueda , que ingresando el nombre, si este alumno existe en la base de datos me retorna el apellido y la direccion.


NOTA 
Existen elementos comentados en el archivo rutas/views.py para agregar posteriormente las clases o modelos restantes.










## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy projectguadafit

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
