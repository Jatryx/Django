---
attachments: [Clipboard_2023-10-24-13-35-42.png, Clipboard_2023-10-24-13-36-21.png, Clipboard_2023-10-24-13-37-51.png, Clipboard_2023-10-24-14-10-11.png]
favorited: true
title: DJANGO
created: '2024-1-07'
modified: '2024-1-27'
---

# DJANGO
--------------

[//]: # (version: 1.0)
[//]: # (author: Francisco Javier Nievas Rosado)
[//]: # (date: 2024-1-07)



# Tabla de contenidos
- [DJANGO](#django)
- [Tabla de contenidos](#tabla-de-contenidos)
- [Introducción](#introducción)
- [Instalación Django](#instalación-django)
  - [Explicamos que consiste cada archivo que se ha creado mediante comando](#explicamos-que-consiste-cada-archivo-que-se-ha-creado-mediante-comando)
  - [Ejecutar el servidor de desarrollo](#ejecutar-el-servidor-de-desarrollo)
  - [Crear una aplicación de Django](#crear-una-aplicación-de-django)
- [Instalación PyCharm](#instalación-pycharm)
- [Sintaxis de Django](#sintaxis-de-django)
  - [Comentarios](#comentarios)
  - [Variables](#variables)
    - [Casting en variables](#casting-en-variables)
    - [Obtención de tipo de datos de variables](#obtención-de-tipo-de-datos-de-variables)
    - [Asignación de multiples variables](#asignación-de-multiples-variables)
    - [Concatenación de variables](#concatenación-de-variables)
    - [Funciones globales y variables globales](#funciones-globales-y-variables-globales)
    - [Tipos de datos](#tipos-de-datos)
    - [Operadores](#operadores)
    - [Diferencias entre listas, tuplas, sets y diccionarios](#diferencias-entre-listas-tuplas-sets-y-diccionarios)
      - [Listas](#listas)
      - [Tuplas](#tuplas)
      - [Sets](#sets)
      - [Diccionarios](#diccionarios)
    - [Estrucuturas de control](#estrucuturas-de-control)
      - [If](#if)
      - [While](#while)
      - [For](#for)
    - [Funciones](#funciones)
    - [Lambda](#lambda)
    - [Arrays](#arrays)
    - [Iteradores](#iteradores)
    - [Polimorfismo](#polimorfismo)
    - [Módulos](#módulos)
  - [POO en Python](#poo-en-python)
    - [Clases y objetos](#clases-y-objetos)
    - [Métodos](#métodos)
    - [Getter y Setter](#getter-y-setter)
    - [Encapsulación](#encapsulación)
    - [Herencia](#herencia)
    - [Métodos especiales de Python](#métodos-especiales-de-python)
    - [Métodos estáticos](#métodos-estáticos)
    - [Métodos de clase](#métodos-de-clase)
    - [Herencia múltiple](#herencia-múltiple)
    - [Clases abstractas](#clases-abstractas)
  - [Crud en Django](#crud-en-django)
    - [Preparación del entorno](#preparación-del-entorno)
    - [Creación del proyecto](#creación-del-proyecto)
    - [Creación del modelo](#creación-del-modelo)
    - [Configuración de la base de datos](#configuración-de-la-base-de-datos)
    - [Pasos a seguir para crear el crud](#pasos-a-seguir-para-crear-el-crud)
      - [Creacion de las rutas](#creacion-de-las-rutas)
      - [Creación de FORMS.py](#creación-de-formspy)

<div style="page-break-after: always;"></div>




# Introducción
[Tabla de contenidos](#tabla-de-contenidos)

Django es un framework gratuito, es un marco de desarrollo de web de alto nivel y de código abierto que fomenta el desarrollo rápido y limpio en Python. 

Las características claves de Django se centran en la eficiencia y simplicidad. Proporciona un conjunto robusto de herramientas y componentes que permiten a los desarrolladores construir aplicaciones web de manera rápida y con un código claro y mantenible.

El marco sigue el patrón de diseño de Modelo-Vista-Controlador(MVC), aunque en Django se le conoce más como Modelo-Vista-Plantilla(MVT).
En este patrón, el modelo representa los datos y la lógica de la aplicación, la vista se encarga de la presentación y la plantilla maneja la representación de los datos. La filosofia de Django se basa en la simplicidad, la reutilización de código y el prinicpio de no te repitas.

Django está diseñado para ser rápido, seguro y escalable. Ofrece una serie de características que facilitan el desarrollo de aplicaciones complejas, como por ejemplo:
  
  - Un sistema de plantillas potente y flexible que permite crear interfaces de usuario atractuvas y fáciles de usar.
  - Un sistema de gestión de base de datos integrado que facilita el acceso a los datos.
  - Una serie de librerías y herramientas que facilitan el desarrollo de tareas comunes, como la autenticacióin de usuarios, la gestión de errores y la depuración.

Django es una buena opción para el desarrollo de aplicaciones web de cualquier tipo, pero es especialmente adeacuado para aplicaciones web controladas por datos, como sitios de comercio electrónico blogs y aplicaciones de gestión.



# Instalación Django
[Tabla de contenidos](#tabla-de-contenidos)

Para instalar Django, necesitarás cumplir con algunos requisitos previos. A continuación, se detallan los pasos básicos para instalar Django en un entorno de desarrollo.


- Requisitos para instalar Django.
  - Actualizar el sistema: para ello debemos abrir la terminal y escribir el siguiente fragmento de codigo en la terminal.
  ```console
    sudo apt update
    sudo apt upgrade
  ```

<div style="page-break-after: always;"></div>
  - Comprobamos la versión de python que tenemos.
  ```console
  python3 --version
  ```

  - Si no tenemos python instalado en nuestro equipo debemos escribir en la terminal el siguiente código:
  ```console
  sudo apt install python3
  ```
  Tenemos que tener en cuenta que la versión de python que tenemos instalada debe ser la 3.6 o superior.

  - Ahora empezaremos con la isntalación de django.
  
    - Primero crearemos una carpeta donde vamos a establecer nuestro entorno gráfico de django. En mi caso la creare en documentos.
    ```console
    mkdir django
    ```

    - Nos moveremos a dicha carpeta:
    ```console
    cd django
    ```

    - Crear un entorno virtual llamado "django":
    ```console
    python3 -m venv django
    ```

    - Si nos sale un error como este:
    ```console
    The virtual environment was not created successfully because ensurepip is not
    available.  On Debian/Ubuntu systems, you need to install the python3-venv
    package using the following command.

        apt install python3.10-venv

    You may need to use sudo with that command.  After installing the python3-venv
    package, recreate your virtual environment.

    Failing command: /home/javi/Documentos/django/django/bin/python3
    ```

  <div style="page-break-after: always;"></div>

  - La solución es la siguiente escribiremos el siguiente comando:
    ```console
    sudo apt install python3.10-venv
    ```

    Este comando instala el módulo venv para Python 3.10 en un sistema operativo basado en Debian, como Ubuntu. venv es un módulo que viene con Python 3.3 y versiones posteriores, y se utiliza para crear entornos virtuales.

    Este comando crea un entorno virtual de Python llamado "django". Un entorno virtual es un ambiente aislado donde puedes instalar paquetes de Python sin afectar a otros proyectos o al sistema Python global.

    - Crear nuevamente un entorno virtual llamado "django"
    ```console
    python3 -m venv django
    ```

    - Ahora debemos activar el entorno virtual:
    ```console
    source django/bin/activate
    ```

    Aquí, estás volviendo a crear el entorno virtual. Si ya creaste uno en el primer paso, este comando no es necesario. Puedes omitirlo si ya tienes un entorno virtual creado.

    - Instalar Django dentro del entorno virtual:
    ```console
    pip install Django // sudo apt install Django // sudo apt install python3-pip
    ```

    El comando pip install Django se utiliza para instalar Django, que es un marco de trabajo de desarrollo web de alto nivel en Python. pip es el gestor de paquetes de Python y se utiliza para instalar y administrar paquetes de software escritos en Python.

    - Comprobamos la versión de Django que tenemos 
    ```console
    python3 -m django --version
    ```

    <div style="page-break-after: always;"></div>

    ## Crear un proyecto de Django
    [Tabla de contenidos](#tabla-de-contenidos)
    
    - Crear un proyecto de Django llamado "hola_mundo":
    ```console
    django-admin startproject hola_mundo
    ```
    Este comando crea un proyecto de Django llamado "hola_mundo". Un proyecto de Django es una colección de configuraciones y aplicaciones para un sitio web específico. Django viene con un comando de administración que se utiliza para crear proyectos de Django.

    hola_mundo/
        manage.py
        hola_mundo/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py

  ## Explicamos que consiste cada archivo que se ha creado mediante comando
  [Tabla de contenidos](#tabla-de-contenidos)
    - Explicamos que consiste cada archivo que se ha creado mediante comando:

      - hola_munsdo/: es el directorio raíz del proyecto. Contiene el archivo manage.py y el paquete hola_mundo.
      - manage.py: es un script de utilidad que se utiliza para administrar el proyecto. Con manage.py, puedes iniciar un servidor de desarrollo, crear y aplicar migraciones de base de datos, crear usuarios, etc.
      - hola_mundo/: es un paquete de Python que contiene los archivos de configuración del proyecto.
      - __init__.py: es un archivo vacío que indica a Python que el directorio es un paquete de Python.
      - settings.py: contiene la configuración del proyecto.
      - urls.py: contiene las URL del proyecto.
      - asgi.py: contiene la configuración para el servidor ASGI.
      - wsgi.py: contiene la configuración para el servidor WSGI.

    - Moverse al directorio "hola_mundo":
    ```console
    cd hola_mundo
    ```
    Este comando te mueve al directorio "hola_mundo" que se creó en el paso anterior.
<div style="page-break-after: always;"></div>

## Ejecutar el servidor de desarrollo
[Tabla de contenidos](#tabla-de-contenidos)

    - Ejecutar el servidor de desarrollo:
    ```console
    python3 manage.py runserver
    ```

    Este comando ejecuta el servidor de desarrollo de Django. El servidor de desarrollo es un servidor web ligero que se utiliza para probar tu aplicación web durante el desarrollo. Por defecto, el servidor de desarrollo se ejecuta en el puerto 8000.

    - Abrir el navegador web y navegar a http://localhost:8000:
    ```console
    http://localhost:8000
    ``` 

    Este comando abre el navegador web y navega a http://localhost:8000. El servidor de desarrollo de Django se ejecuta en el puerto 8000 de forma predeterminada. Si el puerto 8000 está ocupado, puedes especificar un puerto diferente con el siguiente comando:
    ```console
    python3 manage.py runserver 8080
    ```
    Este comando ejecuta el servidor de desarrollo en el puerto 8080.

    - Detener el servidor de desarrollo:
    ```console
    Ctrl + C
    ```
    Este comando detiene el servidor de desarrollo de Django.

    - Podemos cambiar los puertos de escucha de nuestro servidor de desarrollo, para ello debemos escribir el siguiente comando:
    ```console
    python3 manage.py runserver 8080
    ```
    Este comando ejecuta el servidor de desarrollo en el puerto 8080.

<div style="page-break-after: always;"></div>

## Crear una aplicación de Django
[Tabla de contenidos](#tabla-de-contenidos)

Creando la aplicación hola mundo:

- Crear una aplicación de Django llamada "hola_mundo":
```console
python3 manage.py startapp hola_mundo
```

    Este comando crea una aplicación de Django llamada "hola_mundo". Una aplicación de Django es un conjunto de código que se utiliza para realizar una tarea específica. Por ejemplo, una aplicación de Django puede ser un blog, un sitio web de comercio electrónico, un sitio web de noticias, etc.

- Los archivos que se han creado son los siguientes:
    ```console
    hola_mundo/
        manage.py
        hola_mundo/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
        hola_mundo/
            __init__.py
            admin.py
            apps.py
            models.py
            tests.py
            views.py
    ``` 

    - Explicamos que consiste cada archivo que se ha creado mediante comando:

      - hola_mundo/: es el directorio raíz de la aplicación. Contiene el archivo models.py y el paquete hola_mundo.
      - __init__.py: es un archivo vacío que indica a Python que el directorio es un paquete de Python.
      - admin.py: contiene la configuración para la interfaz de administración.
      - apps.py: contiene la configuración de la aplicación.
      - models.py: contiene los modelos de la aplicación.
      - tests.py: contiene las pruebas de la aplicación.
      - views.py: contiene las vistas de la aplicación.
    
    - Abrir el archivo hola_mundo/settings.py:
    - Añadir 'hola_mundo' a la lista INSTALLED_APPS:
    ```console
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'hola_mundo',
    ]
    ```

    Este comando añade la aplicación "hola_mundo" a la lista INSTALLED_APPS en el archivo hola_mundo/settings.py. INSTALLED_APPS es una lista de aplicaciones de Django que se utilizan en el proyecto.

    - Abrir el archivo hola_mundo/urls.py:
    - Añadir la siguiente línea al archivo hola_mundo/urls.py:
    ```console
    path('', include('hola_mundo.urls')),
    ```
    Este comando añade la ruta de la aplicación "hola_mundo" al archivo hola_mundo/urls.py. La ruta de la aplicación "hola_mundo" se añade a la lista urlpatterns en el archivo hola_mundo/urls.py. urlpatterns es una lista de rutas de URL que se utilizan en el proyecto.

    - Crear un archivo llamado urls.py en el directorio hola_mundo:
    ```console
    touch hola_mundo/urls.py
    ```
    Este comando crea un archivo llamado urls.py en el directorio hola_mundo.

    - Abrir el archivo hola_mundo/urls.py:
    - Añadir el siguiente código al archivo hola_mundo/urls.py:
    ```console
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

    Este comando añade la ruta de la aplicación "hola_mundo" al archivo hola_mundo/urls.py. La ruta de la aplicación "hola_mundo" se añade a la lista urlpatterns en el archivo hola_mundo/urls.py. urlpatterns es una lista de rutas de URL que se utilizan en el proyecto.

    - Crear un archivo llamado views.py en el directorio hola_mundo:
    ```console
    touch hola_mundo/views.py
    ```

    Este comando crea un archivo llamado views.py en el directorio hola_mundo.

    - Abrir el archivo hola_mundo/views.py:
    - Añadir el siguiente código al archivo hola_mundo/views.py:
    ```console
    from django.http import HttpResponse
    
    def index(request):
        return HttpResponse("Hola Mundo!")
    ```
    Este comando añade una vista llamada index al archivo hola_mundo/views.py. Una vista es una función de Python que procesa una solicitud web y devuelve una respuesta web. En este caso, la vista index devuelve una respuesta web que dice "Hola Mundo!".

    - Ejecutar el servidor de desarrollo:
    ```console
    python3 manage.py runserver
    ```
    Este comando ejecuta el servidor de desarrollo de Django. El servidor de desarrollo es un servidor web ligero que se utiliza para probar tu aplicación web durante el desarrollo. Por defecto, el servidor de desarrollo se ejecuta en el puerto 8000.

    - Abrir el navegador web y navegar a http://localhost:8000:
    ```console
    http://localhost:8000
    ```

    Este comando abre el navegador web y navega a http://localhost:8000. El servidor de desarrollo de Django se ejecuta en el puerto 8000 de forma predeterminada. Si el puerto 8000 está ocupado, puedes especificar un puerto diferente con el siguiente comando:
    ```console

    python3 manage.py runserver 8080
    ```

    Este comando ejecuta el servidor de desarrollo en el puerto 8080.

    - Detener el servidor de desarrollo:
    ```console
    Ctrl + C
    ```
    Este comando detiene el servidor de desarrollo de Django.


# Instalación PyCharm
[Tabla de contenidos](#tabla-de-contenidos)

- Introducción sobre PyCharm:
  
  Es un entorno de desarrollo integrado (IDE) creado por JetBrains específicamente para el desarrollo de proyectos en Python. 

  - Características: 

    - Editor de código avanzado: ofrece un editor de código robusto con resaltado de sintaxis, completado automático, refactorización de código y navegación inteligente.
  
    - Gestión de Proyectos Eficiente: Facilita la creación y gestión de proyectos Python. Ofrece herramientas para la instalación y gestión de paquetes, y permite trabajar con entornos virtuales para aislar las dependencias de cada proyecto.

    - Depuración Integrada: permite establecer puntos de interrupción, inspeccionar variables.

    - Integración con Herramientas Externas: en este caso podríamos incluir un sistema de versión de controles como es git y base de datos como mysql.

- Instalación de PycCharm:
  - Para la instalación necesitamos acceder al siguiente sitio web https://www.jetbrains.com/es-es/pycharm/ y ahi descargar pycharm, una vez descargado escribiremos en consola la siguiente línea de comando:

  Descomprimir el Archivo de PyCharm:

  ```console
    tar -zxf pyCharm-professional-2023.3.1.tar.gz
  ```

  Ahora crearemos un alias para poder acceder a pyCharm más rapido
  

  ```console
    nano source ~/.bashrc
  ```
  
  [Tabla de contenidos](#tabla-de-contenidos)

  Una vez dentro al final del documento debemos escribir la siguiente línea para crear un alias:

  ```console
    alias pyCharm="la ruta donde se encuentra este archivo"pyCharm-2023.3.1/bin/pycharm.sh
  ```

  Actualizar la Configuración del Shell:
  ```console
    source ~/.bashrc
  ```

# Sintaxis de Django
[Tabla de contenidos](#tabla-de-contenidos)


Python utiliza la sangría para indicar bloques de código. Django utiliza llaves, corchetes y paréntesis para indicar bloques de código. Por ejemplo, las llaves se utilizan para indicar bloques de código en las plantillas de Django. Los corchetes se utilizan para indicar bloques de código en los archivos de configuración de Django. Los paréntesis se utilizan para indicar bloques de código en las vistas de Django.

Un ejemplo de de sangría en python:
```python
if 5 > 2:
  print("Cinco es mayor que dos!")
```

## Comentarios
[Tabla de contenidos](#tabla-de-contenidos)
- Comentarios:
  - Comentarios de una línea:
  ```console
  {# Este es un comentario de una línea #}
  ```
  - Comentarios de varias líneas:
  ```console
  {% comment %}
    Este es un comentario de varias líneas.
  {% endcomment %}
  ```

<div style="page-break-after: always;"></div>

## Variables
[Tabla de contenidos](#tabla-de-contenidos)
- Variables: Una variable se crea en el momento en que se le asigna un valor. Las variables se utilizan para almacenar datos, como cadenas de texto, números enteros, números de punto flotante, etc. En Django, las variables se utilizan para almacenar datos que se utilizan en las plantillas. Las variables de Django se crean utilizando la sintaxis {{variable}}. Por ejemplo, la variable {{nombre}} se utiliza para almacenar el nombre de un usuario.
  ```python
  x = 5 
  y = "Hola Mundo!"
  print(x)
  print(y)
  ```

  print se utiliza para imprimir en pantalla el valor de una variable en la consola.

    - Obtener el tipo de dato de una variable: Python tiene varios tipos de datos estándar, pero también podemos definir nuestros propios tipos de datos personalizados. Para obtener el tipo de dato de una variable, podemos usar la función type():
  ```python
  x = 5
  y = "Hola Mundo!"
  print(type(x))
  print(type(y))
  ```

    - Las variables de cadena de texto se pueden declarar de varias formas:
  ```python
  x = "Hola Mundo!"
  # es lo mismo que
  x = 'Hola Mundo!'
  ```

    - Las variables numéricas se declaran de la siguiente forma:
  ```python
  x = 1    # int
  y = 2.8  # float
  z = 1j   # complex
  ```

    <div style="page-break-after: always;"></div>

    - Python diferencia sus variables entre mayúsculas y minúsculas, por lo que las variables x y X son diferentes.
  Por ejemplo:
  ```python
  a = 4
  A = "Sally"
  #A es una variable diferente a a
  ```

    - Podemos nombrar las variables de diferente forma:
  ```python
  myvar = "John"
  my_var = "John"
  _my_var = "John"
  myVar = "John"
  MYVAR = "John"
  myvar2 = "John"
  ```

  - Las variables no pueden comenzar con un número:
  ```python
  2myvar = "John"
  ```

  - Las variables no pueden tener espacios:
  ```python
  my var = "John"
  ```

  - Booleanos: Las variables booleanas solo pueden tener dos valores: Verdadero o Falso.
  ```python
  x = True
  y = False
  ```

  <div style="page-break-after: always;"></div>

  - Las variables booleanas a menudo se utilizan para comparar valores:
  ```python
  print(10 > 9)
  print(10 == 9)
  print(10 < 9)
  ```
  - Las variables booleanas se devuelven como resultado de comparaciones:
  ```python
  print(10 > 9)
  print(10 == 9)
  print(10 < 9)
  ```


  ### Casting en variables
  [Tabla de contenidos](#tabla-de-contenidos)
  
  - Casting: Si queremos especificar el tipo de dato de una variable, podemos usar la función de casting:
  ```python
  x = str(3)    # x será '3'
  y = int(3)    # y será 3
  z = float(3)  # z será 3.0
  ```

  ### Obtención de tipo de datos de variables
  [Tabla de contenidos](#tabla-de-contenidos)

  - Obtener el tipo de dato de una variable: Python tiene varios tipos de datos estándar, pero también podemos definir nuestros propios tipos de datos personalizados. Para obtener el tipo de dato de una variable, podemos usar la función type():
  ```python
  x = 5
  y = "Hola Mundo!"
  print(type(x))
  print(type(y))
  ```

  <div style="page-break-after: always;"></div>

  ### Asignación de multiples variables
  [Tabla de contenidos](#tabla-de-contenidos)
  - Asignar múltiples valores a múltiples variables: Python le permite asignar valores a múltiples variables en una línea:
  ```python
  x, y, z = "Naranja", "Plátano", "Cereza"
  print(x)
  print(y)
  print(z)
  ```
  - Asignar el mismo valor a múltiples variables: Python le permite asignar el mismo valor a múltiples variables en una línea:
  ```python
  x = y = z = "Naranja"
  print(x)
  print(y)
  print(z)
  ```
  ### Concatenación de variables
  [Tabla de contenidos](#tabla-de-contenidos)
  - Podemos utilizar la función + para combinar variables de cadena de texto:
  ```python
  x = "Python es "
  y = "increíble"
  z =  x + y 
  print(z)
  ```
  También podemos utilizar la funcion + en el print para concatenar variables de cadena de texto:
  ```python
  x = "Python es "
  y = "increíble"
  print(x + y)
  ```
  
  - Para los números, el operador + funciona como una operación matemática:
  ```python
  x = 5
  y = 10
  print(x + y)
  ```

  - Si intentamos combinar una cadena de texto y un número, Python nos dará un error:
  ```python
  x = 5
  y = "John"
  print(x + y)
  ```
  ### Funciones globales y variables globales
  [Tabla de contenidos](#tabla-de-contenidos)
  - Podemos utilizar la función global() para crear una variable global, incluso si se crea dentro de una función:
  ```python
  x = "awesome"

  def myfunc():
  print("Python is " + x)

  myfunc()
  ```

  - Si se crea una variable con el mismo nombre dentro de una función, esta será local y solo se podrá utilizar dentro de la función. La variable global con el mismo nombre seguirá existiendo como variable global.
  ```python
  x = "awesome"

  def myfunc():
  x = "fantastic"
  print("Python is " + x)

  myfunc()
  
  print("Python is " + x)
  ```
  - Para crear una variable global podemos utilizar la palabra clave global:
  ```python
  def myfunc():
  global x
  x = "fantastic"
  
  myfunc()

  print("Python is " + x)
  ```
  - También podemos cambiar el valor de una variable global dentro de una función:
  ```python
  x = "awesome"

  def myfunc():
  global x
  x = "fantastic"

  myfunc()

  print("Python is " + x)
  ```

### Tipos de datos
[Tabla de contenidos](#tabla-de-contenidos)
- Tipos de datos en python:
  - Texto: str
  - Numérico: int, float, complex
  - Secuencia: list, tuple, range
  - Mapeo: dict
  - Set: set, frozenset
  - Booleano: bool
  - Binario: bytes, bytearray, memoryview
  
  - Tipos de datos: 
  
  | Tipo de Dato | Ejemplo                                        | Ejemplo con Constructor                       |
  | ---          | ---                                            | ---                                           |
  | str          | `x = "Hello World"`                            | `x = str("Hello World")`                      |
  | int          | `x = 20`                                       | `x = int(20)`                                 |
  | float        | `x = 20.5`                                     | `x = float(20.5)`                             |
  | complex      | `x = 1j`                                       | `x = complex(1j)`                             |
  | list         | `x = ["apple", "banana", "cherry"]`            | `x = list(("apple", "banana", "cherry"))`     |
  | tuple        | `x = ("apple", "banana", "cherry")`            | `x = tuple(("apple", "banana", "cherry"))`    |
  | range        | `x = range(6)`                                 | `x = range(6)`                                |
  | dict         | `x = {"name" : "John", "age" : 36}`            | `x = dict(name="John", age=36)`               |
  | set          | `x = {"apple", "banana", "cherry"}`            | `x = set(("apple", "banana", "cherry"))`      |
  | frozenset    | `x = frozenset({"apple", "banana", "cherry"})` | `x = frozenset(("apple", "banana", "cherry"))`|
  | bool         | `x = True`                                     | `x = bool(5)`                                 |
  | bytes        | `x = b"Hello"`                                 | `x = bytes(5)`                                |
  | bytearray    | `x = bytearray(5)`                             | `x = bytearray(5)`                            |
  | memoryview   | `x = memoryview(bytes(5))`                     | `x = memoryview(bytes(5))`                    |

 ### Operadores
 [Tabla de contenidos](#tabla-de-contenidos)
 - Tipos de operadores aritméticos en python:

    | Operador | Nombre | Ejemplo |
    | --- | --- | --- |
    | + | Addition | `x + y` |
    | - | Subtraction | `x - y` |
    | * | Multiplication | `x * y` |
    | / | Division | `x / y` |
    | % | Modulus | `x % y` |
    | ** | Exponentiation | `x ** y` |
    | // | Floor division | `x // y` |

  - Tipos de operadores de asignación en python:
  
    | Operador | Ejemplo | Equivalente | 
    | --- | --- | --- |
    | = | `x = 5` | `x = 5` |
    | += | `x += 3` | `x = x + 3` |
    | -= | `x -= 3` | `x = x - 3` |
    | *= | `x *= 3` | `x = x * 3` |
    | /= | `x /= 3` | `x = x / 3` |
    | %= | `x %= 3` | `x = x % 3` |
    | //= | `x //= 3` | `x = x // 3` |
    | **= | `x **= 3` | `x = x ** 3` |
    | &= | `x &= 3` | `x = x & 3` |
    | |= | `x |= 3` | `x = x | 3` |
    | ^= | `x ^= 3` | `x = x ^ 3` |
    | >>= | `x >>= 3` | `x = x >> 3` |
    | <<= | `x <<= 3` | `x = x << 3` |

  - Tipos de operadores de comparación en python:

    | Operador | Nombre | Ejemplo |
    | --- | --- | --- |
    | == | Equal | `x == y` |
    | != | Not equal | `x != y` |
    | > | Greater than | `x > y` |
    | < | Less than | `x < y` |
    | >= | Greater than or equal to | `x >= y` |
    | <= | Less than or equal to | `x <= y` |

  - Tipos de operadores lógicos en python:
  
    | Operador | Descripción | Ejemplo |
    | --- | --- | --- |
    | and | Devuelve True si ambos son ciertos | `x < 5 and  x < 10` |
    | or | Devuelve True si uno de los dos es cierto | `x < 5 or x < 4` |
    | not | Invierte el resultado, devuelve False si el resultado es cierto | `not(x < 5 and x < 10)` |

  - Tipos de operadores de identidad en python:
  
    | Operador | Descripción | Ejemplo |
    | --- | --- | --- |
    | is | Devuelve True si ambas variables son el mismo objeto | `x is y` |
    | is not | Devuelve True si ambas variables no son el mismo objeto | `x is not y` |

  <div style="page-break-after: always;"></div>

  - Tipos de operadores de bit a bit en Python:
  
    | Operador | Nombre | Descripción |
    | --- | --- | --- |
    | & | AND | Conjunto de bits |
    | \| | OR | Conjunto de bits |
    | ^ | XOR | Conjunto de bits |
    | ~ | NOT | Conjunto de bits |
    | << | Zero fill left shift | Desplazamiento de bits a la izquierda |
    | >> | Signed right shift | Desplazamiento de bits a la derecha |
  
  ### Diferencias entre listas, tuplas, sets y diccionarios
  [Tabla de contenidos](#tabla-de-contenidos)
  Las listas, tuplas, sets y diccionarios son estructuras de datos en Python que se utilizan para almacenar colecciones de datos. Aquí están las principales diferencias entre ellos:

  Listas: Son colecciones ordenadas y modificables que permiten duplicados. Se definen con corchetes []. Ejemplo: mi_lista = [1, 2, 3, 4, 5]

  Tuplas: Son colecciones ordenadas e inmutables que permiten duplicados. Se definen con paréntesis (). Ejemplo: mi_tupla = (1, 2, 3, 4, 5)

  Sets: Son colecciones no ordenadas, no indexadas y no permiten duplicados. Se definen con llaves {} o con la función set(). Ejemplo: mi_set = {1, 2, 3, 4, 5}

  Diccionarios: Son colecciones no ordenadas, modificables e indexadas. No permiten duplicados y se definen con llaves {}. Ejemplo: mi_diccionario = {"nombre": "Juan", "edad": 30}

  En resumen, las listas y tuplas son muy similares, pero las tuplas son inmutables. Los sets son útiles cuando quieres una colección que no permita duplicados. Los diccionarios son útiles cuando necesitas asociar valores con claves.


  #### Listas
  [Tabla de contenidos](#tabla-de-contenidos)

  - Listas: Las listas se utilizan para almacenar varios elementos en una sola variable. Las listas se crean utilizando corchetes:
  ```python
  lista = ["manzana", "plátano", "cereza"]
  print(lista)
  ```

  <div style="page-break-after: always;"></div>

  - Podemos acceder a los elementos de una lista haciendo referencia al número de índice:
  ```python
  lista = ["manzana", "plátano", "cereza"]
  print(lista[1])
  ```

  - Podemos saber la longitud de la lista utilizando la función len():
  ```python
  lista = ["manzana", "plátano", "cereza"]
  print(len(lista))
  ```

  - La lista puede contener diferentes tipos de datos:
  ```python
  lista = ["manzana", "plátano", "cereza", 1, 2, 3]
  print(lista)
  ```

  - Para saber el tipo de una lista se utiliza la función type():
  ```python 
  lista = ["manzana", "plátano", "cereza"]
  print(type(lista))
  ```

  - Puedes comprobar si un valor existe en una lista utilizando la palabra clave in:
  ```python
  lista = ["manzana", "plátano", "cereza"]
  if "manzana" in lista:
    print("Sí, 'manzana' está en la lista de frutas")
  ```
  - Insertar y añadir valores a una lista:
  ```python
  lista = ["manzana", "plátano", "cereza"]
  lista.append("naranja")
  lista.insert(1, "limón")
  print(lista)
  ```

  <div style="page-break-after: always;"></div>

  - Eliminar valores de una lista:
  ```python
  lista = ["manzana", "plátano", "cereza"]
  lista.remove("plátano")
  lista.pop()
  del lista[0]
  print(lista)
  ```

  - Eliminar la lista por completo:
  ```python
  lista = ["manzana", "plátano", "cereza"]
  del lista
  print(lista) #this will cause an error because "thislist" no longer exists.
  ```

  - Ampliar la lista con otra lista:
  ```python
  lista1 = ["a", "b" , "c"]
  lista2 = [1, 2, 3]
  lista1.extend(lista2)
  print(lista1)
  ```

  - Como recorer una lista:
  ```python
  lista = ["manzana", "plátano", "cereza"]
  for x in lista:
    print(x)
  ```

  - Ordenar una lista:
  ```python
  lista = ["manzana", "plátano", "cereza"]
  lista.sort()
  print(lista)
  ```

  <div style="page-break-after: always;"></div>

  #### Tuplas
  [Tabla de contenidos](#tabla-de-contenidos)

  - Tuplas: Las tuplas se utilizan para almacenar varios elementos en una sola variable. Una tupla es una colección ordenada y no cambiable. Las tuplas se crean utilizando paréntesis:
  ```python
  tupla = ("manzana", "plátano", "cereza")
  print(tupla)
  ```

  #### Sets
  [Tabla de contenidos](#tabla-de-contenidos)

  - Sets: Los sets se utilizan para almacenar varios elementos en una sola variable. Un set es una colección que no está ordenada ni indexada. En Python, los sets se escriben con llaves.
  ```python
  set = {"manzana", "plátano", "cereza"}
  print(set)
  ```

  #### Diccionarios
  [Tabla de contenidos](#tabla-de-contenidos)

  - Diccionarios: Los diccionarios se utilizan para almacenar varios elementos en una sola variable. Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se escriben con llaves y tienen claves y valores.
  ```python
  diccionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
  }
  print(diccionario)
  ```

  <div style="page-break-after: always;"></div>

  ### Estrucuturas de control
  [Tabla de contenidos](#tabla-de-contenidos)

  #### If
  - If: La declaración if se utiliza para tomar decisiones basadas en diferentes condiciones.
  ```python
  a = 33
  b = 200
  if b > a:
    print("b es mayor que a")
  ```

  - Elif: La declaración elif se utiliza para evitar que se ejecute el bloque if y el bloque else. Si la declaración elif es verdadera, se ejecutará el bloque elif, y el bloque else se omitirá.
  ```python
  a = 33
  b = 33
  if b > a:
    print("b es mayor que a")
  elif a == b:
    print("a y b son iguales")
  ```
  - Else: La declaración else se utiliza para ejecutar un bloque de código si ninguna de las condiciones es verdadera.
  ```python
  a = 200
  b = 33
  if b > a:
    print("b es mayor que a")
  elif a == b:
    print("a y b son iguales")
  else:
    print("a es mayor que b")
  ```
    <div style="page-break-after: always;"></div>

  - Short Hand If: Si solo hay una declaración a ejecutar, puede ponerla en la misma línea que la declaración if.
  ```python
  if a > b: print("a es mayor que b")
  ```
  - Short Hand If ... Else: Si solo hay una declaración a ejecutar para ambas condiciones, puede ponerlas en la misma línea:
  ```python
  a = 2
  b = 330
  print("A") if a > b else print("B")
  ```
  - And: La palabra clave and es un operador lógico, y se utiliza para combinar condiciones lógicas.
  ```python
  a = 200
  b = 33
  c = 500
  if a > b and c > a:
    print("Ambas condiciones son verdaderas")
  ```
  - Or: La palabra clave or es un operador lógico, y se utiliza para combinar condiciones lógicas.
  ```python
  a = 200
  b = 33
  c = 500
  if a > b or a > c:
    print("Al menos una de las condiciones es verdadera")
  ```
  - Not: La palabra clave not es un operador lógico, y se utiliza para invertir el valor de una condición lógica.
  ```python
  a = 200
  b = 33
  if not b > a:
    print("b no es mayor que a")
  ```
  - Nested If: Una declaración if dentro de otra declaración if.
  ```python
  x = 41

  if x > 10:
    print("Por encima de diez,")
    if x > 20:
      print("y también por encima de 20!")
    else:
      print("pero no por encima de 20.")
  ```

  #### While
  [Tabla de contenidos](#tabla-de-contenidos)
  - While: Con la instrucción while podemos ejecutar un conjunto de declaraciones siempre que se cumpla una condición especificada.
  ```python
  i = 1
  while i < 6:
    print(i)
    i += 1
  ```
  - Break: Con la instrucción break podemos detener el bucle aunque la condición while sea verdadera.
  ```python
  i = 1
  while i < 6:
    print(i)
    if i == 3:
      break
    i += 1
  ```
  - Continue: Con la instrucción continue podemos detener la iteración actual del bucle y continuar con la siguiente.
  ```python
  i = 0
  while i < 6:
    i += 1
    if i == 3:
      continue
    print(i)
  ```
  - Else: Con la instrucción else podemos ejecutar un bloque de código una vez cuando la condición ya no es verdadera.
  ```python
  i = 1
  while i < 6:
    print(i)
    i += 1
  else:
    print("i ya no es menor que 6")
  ```
  #### For
  [Tabla de contenidos](#tabla-de-contenidos)
  - For: Un bucle for se utiliza para iterar sobre una secuencia (que es una lista, una tupla, un diccionario, un conjunto o una cadena).
  ```python
  lista = ["manzana", "plátano", "cereza"]
  for x in lista:
    print(x)
  ```
  - Looping Through a String: Podemos recorrer una cadena de texto utilizando un bucle for.
  ```python
  for x in "banana":
    print(x)
  ```
  - Break: Con la instrucción break podemos detener el bucle aunque la condición while sea verdadera.
  ```python
  lista = ["manzana", "plátano", "cereza"]
  for x in lista:
    print(x)
    if x == "plátano":
      break
  ```
  - Continue: Con la instrucción continue podemos detener la iteración actual del bucle y continuar con la siguiente.
  ```python
  lista = ["manzana", "plátano", "cereza"]
  for x in lista:
    if x == "plátano":
      continue
    print(x)
  ```
  - Range: La función range() devuelve una secuencia de números, comenzando desde 0 de forma predeterminada, y se incrementa en 1 (de forma predeterminada), y termina en un número especificado.
  ```python
  for x in range(6):
    print(x)
  ```

  <div style="page-break-after: always;"></div>

  - Else: Con la instrucción else podemos ejecutar un bloque de código una vez cuando la condición ya no es verdadera.
  ```python
  for x in range(6):
    print(x)
  else:
    print("Finalmente terminó!")
  ```
  - Nested Loops: Un bucle anidado es un bucle dentro de un bucle. El "bucle interno" se ejecutará una vez por cada iteración del "bucle externo":
  ```python
  adj = ["rojo", "grande", "delicioso"]
  frutas = ["manzana", "plátano", "cereza"]

  for x in adj:
    for y in frutas:
      print(x, y)
  ```

  ### Funciones
  [Tabla de contenidos](#tabla-de-contenidos)

  - Funciones: Una función es un bloque de código que se ejecuta cuando se llama a la función. Puedes pasar datos, conocidos como parámetros, a una función. Una función puede devolver datos como resultado.
  ```python
  def my_function():
    print("Hola desde una función")
  ```
  - Llamar a una función: Para llamar a una función, utiliza el nombre de la función seguido de paréntesis:
  ```python
  def my_function():
    print("Hola desde una función")

  my_function()
  ```

  <div style="page-break-after: always;"></div>

  - Argumentos: La información se puede pasar a las funciones como argumentos. Los argumentos se especifican después del nombre de la función, entre paréntesis. Puedes agregar tantos argumentos como desees, solo sepáralos con una coma.
  ```python
  def my_function(nombre):
    print("Hola " + nombre)

  my_function("Juan")
  my_function("Carlos")
  my_function("Pedro")
  ```

  - Número de argumentos: Al definir una función, se puede especificar el número de argumentos que se espera que tenga la función. Esto se hace agregando un número al nombre de argumento.
  ```python
  def my_function(fname):
    print(fname + " Refsnes")

  my_function("Emil")
  my_function("Tobias")
  my_function("Linus")
  ```

  - Argumentos arbitrarios: Si no sabes cuántos argumentos se pasarán a tu función, agrega un * antes del nombre del parámetro en la definición de la función.
  ```python

  def my_function(*kids):
    print("El niño más joven es " + kids[2])

  my_function("Emil", "Tobias", "Linus")
  ```

  - Argumentos con palabras clave: También puedes enviar argumentos con la sintaxis clave = valor. De esta forma, el orden de los argumentos no importa.
  ```python
  def my_function(child3, child2, child1):
    print("El niño más joven es " + child3)

  my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
  ```

  <div style="page-break-after: always;"></div>

  - Argumentos arbitrarios, palabras clave: Si no sabes cuántos argumentos con palabras clave se pasarán a tu función, agrega dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
  ```python
  def my_function(**kid):
    print("Su apellido es " + kid["lname"])

  my_function(fname = "Tobias", lname = "Refsnes")
  ```

  - Valor de parámetro predeterminado: Si llamamos a la función sin argumentos, utiliza el valor predeterminado:
  ```python
  def my_function(pais = "Noruega"):
    print("Yo soy de " + pais)

  my_function("Suecia")
  my_function("India")
  my_function()
  my_function("Brasil")
  ```

  - Pasar una lista como argumento: Puedes enviar cualquier tipo de datos como argumento a una función (cadena, número, lista, diccionario, etc.), y se tratará como el mismo tipo de datos dentro de la función.
  ```python
  def my_function(comida):
    for x in comida:
      print(x)

  frutas = ["manzana", "plátano", "cereza"]

  my_function(frutas)
  ```

  - Devolver valores: Para permitir que una función devuelva un valor, utiliza la palabra clave return:
  ```python
  def my_function(x):
    return 5 * x

  print(my_function(3))
  print(my_function(5))
  print(my_function(9))
  ```

  <div style="page-break-after: always;"></div>

  ### Lambda
  [Tabla de contenidos](#tabla-de-contenidos)

  - Lambda: Una función lambda es una pequeña función anónima. Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.
  ```python
  x = lambda a : a + 10
  print(x(5))
  ```

  - Lambda con varios argumentos: Una función lambda puede tomar cualquier número de argumentos:
  ```python
  x = lambda a, b : a * b
  print(x(5, 6))
  ```

  - Lambda dentro de otra función: Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.
  ```python
  def myfunc(n):
    return lambda a : a * n

  mydoubler = myfunc(2)

  print(mydoubler(11))
  ```

  ### Arrays
  [Tabla de contenidos](#tabla-de-contenidos)

  - Arrays: Los arrays se utilizan para almacenar varios valores en una sola variable, a diferencia de las variables normales. Si tienes una lista de elementos (una lista de nombres, por ejemplo), almacenar los nombres en variables podría parecerse a esto:
  ```python
  nombre1 = "Juan"
  nombre2 = "Carlos"
  nombre3 = "Pedro"
  ```

  <div style="page-break-after: always;"></div>

  - Pero, ¿qué pasa si quieres recorrer los nombres y encontrar un nombre en particular? Y ¿qué pasa si no sabes cuántos nombres hay? La solución es un array. Un array puede contener muchos valores bajo un solo nombre, y puede acceder a los valores haciendo referencia a un número de índice.
  ```python
  nombres = ["Juan", "Carlos", "Pedro"]
  print(nombres[1])
  ```

  - Longitud de un array: Utiliza la función len() para determinar la longitud de un array.
  ```python
  nombres = ["Juan", "Carlos", "Pedro"]
  print(len(nombres))
  ```
  - Un array con datos de diferentes tipos: Un array puede contener diferentes tipos de datos:
  ```python
  array = ["Juan", 1, True]
  print(array)
  ```

### Iteradores
[Tabla de contenidos](#tabla-de-contenidos)

- Iteradores: Un iterador es un objeto que contiene un número contable de valores. Un iterador es un objeto que se puede iterar sobre, lo que significa que puede atravesar todos los valores. Los iteradores se pueden crear utilizando la función iter(). Para crear un objeto iterable, debe implementar el método __iter__() en la clase.
  ```python
  class MiClase:
    def __iter__(self):
      self.a = 1
      return self

  mi_clase = MiClase()
  mi_iterador = iter(mi_clase)

  print(next(mi_i))
  ```

  <div style="page-break-after: always;"></div>

  ### Polimorfismo
  [Tabla de contenidos](#tabla-de-contenidos)

  - Polimorfismo: Polimorfismo significa "muchas formas", y ocurre cuando tenemos muchas clases que están relacionadas entre sí por herencia.
  ```python
  class Perro:
    def sonido(self):
      print("Guau")

  class Gato:
    def sonido(self):
      print("Miau")

  def hacer_sonar(animal_type):
    animal_type.sonido()

  perro = Perro()
  gato = Gato()
  
  hacer_sonar(perro)
  hacer_sonar(gato)
  ```

  ### Módulos
  [Tabla de contenidos](#tabla-de-contenidos)

  - Módulos: Considere un módulo como una biblioteca de funciones para incluir en su aplicación.
  ```python
  import mi_modulo

  mi_modulo.saludar("Juan")
  ```

  - Variables en módulos: El módulo puede contener funciones, así como variables de todo tipo (listas, diccionarios, objetos, etc.):
  ```python
  import mi_modulo

  a = mi_modulo.personas1["nombre"]
  print(a)
  ```

  <div style="page-break-after: always;"></div>

  - Renombrar un módulo: Puede crear un alias cuando importa un módulo, al usar la palabra clave as:
  ```python
  import mi_modulo as mx
  
  a = mx.personas1["nombre"]
  print(a)
  ```

  - Importar solo partes de un módulo: Puede elegir importar solo partes de un módulo, al usar la palabra clave from.
  ```python
  from mi_modulo import personas1

  print(personas1["nombre"])
  ```

  - Variables integradas: Hay varios módulos integrados en Python, que se pueden importar en cualquier momento y en cualquier lugar, sin importar si se ha instalado el módulo:
  ```python
  import platform

  x = platform.system()
  print(x)
  ```

## POO en Python
[Tabla de contenidos](#tabla-de-contenidos)

### Clases y objetos

  - Clases y objetos: Python es un lenguaje orientado a objetos. Casi todo en Python es un objeto, con sus propiedades y métodos. Una clase es como un constructor de objetos, o un "plano" para crear objetos.
  ```python
  class MiClase:
    x = 5
    
  p1 = MiClase()
  print(p1.x)
  ```

  <div style="page-break-after: always;"></div>

  - Objetos: Una vez que tenga una clase creada, puede utilizar el objeto para acceder a sus atributos.
  ```python
  class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

  p1 = Persona("Juan", 36)

  print(p1.nombre)
  print(p1.edad)
  ```

  - Modificar propiedades de un objeto: Puede modificar las propiedades de un objeto de la siguiente manera:
  ```python
  p1.edad = 40
  ```

  - Eliminar propiedades de un objeto: Puede eliminar propiedades de objetos de la siguiente manera:
  ```python
  del p1.edad
  ```

  - Eliminar objetos: Puede eliminar objetos utilizando la palabra clave del:
  ```python
  del p1
  ```

  <div style="page-break-after: always;"></div>

  - Añadir propiedades: Puede añadir propiedades a clases y objetos existentes de la siguiente manera:
  ```python
  class Persona:
    def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

    def printname(self):
      print(self.firstname, self.lastname)

  class Estudiante(Persona):

    def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

    def bienvenida(self):
      print("Bienvenido", self.firstname, self.lastname, "a la clase de", self.graduationyear)

  x = Estudiante("Juan", "Perez", 2019)
  x.bienvenida()
  ```

  ### Métodos
  [Tabla de contenidos](#tabla-de-contenidos)

  - Métodos: Los métodos son funciones que pertenecen a los objetos.
  ```python
  class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    def mi_funcion(self):
      print("Hola mi nombre es " + self.nombre)

  p1 = Persona("Juan", 36)
  p1.mi_funcion()
  ```

  <div style="page-break-after: always;"></div>

  - El self parámetro: El self parámetro es una referencia a la instancia actual de la clase, y se utiliza para acceder a las variables que pertenecen a la clase.
  ```python
  class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    def mi_funcion(self):
      print("Hola mi nombre es " + self.nombre)

  p1 = Persona("Juan", 36)
  p1.mi_funcion()
  ```

  - Función super(): Python también tiene una función super() que hará que la clase hija herede todos los métodos y propiedades de su clase padre:
  ```python
  class Persona:
    def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

    def printname(self):
      print(self.firstname, self.lastname)

  class Estudiante(Persona):

    def __init__(self, fname, lname):
      super().__init__(fname, lname)

  x = Estudiante("Juan", "Perez")
  x.printname()
  ```

  <div style="page-break-after: always;"></div>

  ### Getter y Setter
  [Tabla de contenidos](#tabla-de-contenidos)

  - Getter y Setter: Los getters y setters se utilizan para proteger los datos, controlar el acceso a ellos, obtenerlos y establecerlos.
  ```python
  class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    def mi_funcion(self):
      print("Hola mi nombre es " + self.nombre)

  p1 = Persona("Juan", 36)
  p1.mi_funcion()
  ```

  ### Encapsulación
  [Tabla de contenidos](#tabla-de-contenidos)

  - Encapsulación: La encapsulación significa que los atributos y métodos internos de una clase no se pueden acceder desde el exterior de la clase.
  ```python
  class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    def mi_funcion(self):
      print("Hola mi nombre es " + self.nombre)

  p1 = Persona("Juan", 36)
  p1.mi_funcion()
  ```

  <div style="page-break-after: always;"></div>

  ### Herencia
  [Tabla de contenidos](#tabla-de-contenidos)

  - Herencia: La herencia nos permite definir una clase que hereda todos los métodos y propiedades de otra clase.
  ```python
  class Persona:
    def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

    def printname(self):
      print(self.firstname, self.lastname)

  class Estudiante(Persona):
      
      def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
  
      def bienvenida(self):
        print("Bienvenido", self.firstname, self.lastname, "a la clase de", self.graduationyear)

  x = Estudiante("Juan", "Perez", 2019)
  x.bienvenida()
  ```

  ### Métodos especiales de Python
  [Tabla de contenidos](#tabla-de-contenidos)

  - Métodos especiales de Python: Los métodos especiales de Python son métodos especiales que puede utilizar dentro de su clase para realizar tareas específicas, como la inicialización y la creación de objetos, etc. Los métodos especiales se definen con guiones bajos dobles __init__(), __del__(), __repr__(), etc.
  ```python
  class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    def __str__(self):
      return "Mi nombre es " + self.nombre

  p1 = Persona("Juan", 36)
  print(p1)
  ```

  ### Métodos estáticos
  [Tabla de contenidos](#tabla-de-contenidos)

  - Métodos estáticos: Los métodos estáticos en Python son métodos que se pueden llamar sin crear una instancia de una clase. Los métodos estáticos se definen con la palabra clave @staticmethod.
  ```python
  class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    @staticmethod
    def mi_funcion():
      print("Hola")

  Persona.mi_funcion()
  ```

  ### Métodos de clase
  [Tabla de contenidos](#tabla-de-contenidos)


  - Métodos de clase: Los métodos de clase en Python son métodos que se llaman con la clase como primer argumento. Los métodos de clase se definen con la palabra clave @classmethod.
  ```python
  class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    @classmethod
    def mi_funcion(cls):
      print("Hola")

  Persona.mi_funcion()
  ```

  <div style="page-break-after: always;"></div>

  ### Herencia múltiple
  [Tabla de contenidos](#tabla-de-contenidos)

  - Herencia múltiple: La herencia múltiple significa que una clase puede heredar de múltiples clases. Python admite una forma limitada de herencia múltiple en clases. Las clases derivadas pueden heredar de una o más clases base.
  ```python
  class Persona:
    def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

    def printname(self):
      print(self.firstname, self.lastname)

  class Estudiante(Persona):
    def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

    def bienvenida(self):
      print("Bienvenido", self.firstname, self.lastname, "a la clase de", self.graduationyear)

  class Estudiante2(Persona):

    def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

    def bienvenida(self):
      print("Bienvenido", self.firstname, self.lastname, "a la clase de", self.graduationyear)

  x = Estudiante("Juan", "Perez", 2019)
  x.bienvenida()
  ```

  <div style="page-break-after: always;"></div>

  ### Clases abstractas
  [Tabla de contenidos](#tabla-de-contenidos)

  - Clases abstractas: Las clases abstractas, que nunca están destinadas a ser instanciadas, pueden ser útiles para definir interfaces que deben ser implementadas por clases concretas.
  ```python
  from abc import ABC, abstractmethod

  class Persona(ABC):
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad
      super().__init__()

    @abstractmethod
    def mi_funcion(self):
      pass

  class Estudiante(Persona):
    def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

    def mi_funcion(self):
      print("Bienvenido", self.firstname, self.lastname, "a la clase de", self.graduationyear)
      
  x = Estudiante("Juan", "Perez", 2019)
  x.mi_funcion()
  ```

  ## Crud en Django
  [Tabla de contenidos](#tabla-de-contenidos)

  ### Preparación del entorno

  - Una vez que tengamos instalado el entorno con PyCharm, necesitamos descargarnos el paquete de MySQL para Python, para ello abrimos la consola de comandos y ejecutamos el siguiente comando:
  ```console
  pip3 install PyMySQL
  ```

  - Para comprobar que se ha instalado correctamente, escribimos el siguiente comando en la consola de comandos:
  ```console
  pip3 list
  ```
  - Nos deberia salir algo como esto:
  ```console
  | Package                 | Version                     |
  |-------------------------|-----------------------------|
  | asgiref                 | 3.5.0                       |
  | blinker                 | 1.4                         |
  | Brlapi                  | 0.8.3                       |
  | chardet                 | 4.0.0                       |
  | click                   | 8.0.3                       |
  | colorama                | 0.4.4                       |
  | command-not-found       | 0.3                         |
  | cryptography            | 3.4.8                       |
  | dbus-python             | 1.2.18                      |
  | defer                   | 1.0.6                       |
  | distro                  | 1.7.0                       |
  | distro-info             | 1.1+ubuntu0.2               |
  | Django                  | 3.2.12                      |
  | httplib2                | 0.20.2                      |
  | importlib-metadata      | 4.6.4                       |
  | jeepney                 | 0.7.1                       |
  | keyring                 | 23.5.0                      |
  | language-selector       | 0.1                         |
  | launchpadlib            | 1.10.16                     |
  | lazr.restfulclient      | 0.14.4                      |
  | lazr.uri                | 1.0.6                       |
  | louis                   | 3.20.0                      |
  | more-itertools          | 8.10.0                      |
  | netifaces               | 0.11.0                      |
  | oauthlib                | 3.2.0                       |
  | olefile                 | 0.46                        |
  | onboard                 | 1.4.1                       |
  | pexpect                 | 4.8.0                       |
  | Pillow                  | 9.0.1                       |
  | pip                     | 22.0.2                      |
  | ptyprocess              | 0.7.0                       |
  | pycairo                 | 1.20.1                      |
  | PyGObject               | 3.42.1                      |
  | PyJWT                   | 2.3.0                       |
  | PyMySQL                 | 1.1.0                       |
  | pyparsing               | 2.4.7                       |
  | python-apt              | 2.4.0-elementary9-ubuntu7.1 |
  | python-debian           | 0.1.43+ubuntu1.1            |
  | pytz                    | 2022.1                      |
  | pyxdg                   | 0.27                        |
  | PyYAML                  | 5.4.1                       |
  | reportlab               | 3.6.8                       |
  | screen-resolution-extra | 0.0.0                       |
  | SecretStorage           | 3.3.1                       |
  | setuptools              | 59.6.0                      |
  | six                     | 1.16.0                      |
  | sqlparse                | 0.4.2                       |
  | ubuntu-advantage-tools  | 8001                        |
  | ubuntu-drivers-common   | 0.0.0                       |
  | ufw                     | 0.36.1                      |
  | unattended-upgrades     | 0.1                         |
  | wadllib                 | 1.3.6                       |
  | wheel                   | 0.37.1                      |
  | xdg                     | 5                           |
  | xkit                    | 0.0.0                       |
  | zipp                    | 1.0.0                       |
  ```

  Django utiliza otro gestor de base de datos llamado SQLite, para este trabajo vamos a utilizar MySQL.

  ### Creación del proyecto

  - Para crear un proyecto en Django, abrimos la consola de comandos y nos situamos en la carpeta donde hemos instalado django anteriormente, y ejecutamos este comando:
  ```console
  django-admin startproject crud
  ```
  
  - Nos deberia salir algo como esto:
  ```console
  crud/
  ├── crud
  │   ├── asgi.py
  │   ├── __init__.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── manage.py
  ```

  - Una vez dentro de la carpeta crud, ejecutamos el siguiente comando para crear una aplicación:
  ```console
  python3 manage.py startapp contenido
  ```
  <div style="page-break-after: always;"></div>

  - Nos deberia salir algo como esto:
  ```console
  crud/
  ├── contenido
  │   ├── admin.py
  │   ├── apps.py
  │   ├── __init__.py
  │   ├── migrations
  │   │   └── __init__.py
  │   ├── models.py
  │   ├── tests.py
  │   └── views.py
  ├── crud
  │   ├── asgi.py
  │   ├── __init__.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── manage.py
  ```

  ### Creación del modelo
  [Tabla de contenidos](#tabla-de-contenidos)

  - Una vez creada la aplicación contenido, abrimos el archivo models.py y escribimos el siguiente código:
  ```python
  from django.db import models

  # Create your models here.
  class Contenido(models.Model):
      id = models.AutoField(primary_key=True)
      nombre = models.CharField(max_length=100, null=True, verbose_name="Nombre")
      apellido = models.CharField(max_length=100, null=True, verbose_name="apellido")
      email = models.EmailField(null=True, verbose_name="email")
      telefono = models.IntegerField(null=True, verbose_name="telefono")

      def __str__(self):
          fila = "Nombre: " + self.nombre + " - " + "Apellido: " + self.apellido
          return fila
  ```

  ### Configuración de la base de datos
  [Tabla de contenidos](#tabla-de-contenidos)

  - Debes crear primero una base de datos en MySQL, en la carpeta he pasado un archivo bbdd.sql con una base de datos ya creada con valores iniciales para que puedas probar el crud.
  
  - Una vez creada la base de datos, debemos configurarla en Django, para ello abrimos el archivo settings.py y buscamos la siguiente linea de código:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  ```
  - Y la cambiamos por esta:
  ```python
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',  # El motor de la base de datos
        'NAME': 'empleados',  # El nombre de la base de datos
        'USER': 'root',  # El nombre de usuario para la base de datos
        'PASSWORD': 'root',  # La contraseña para la base de datos
        'HOST': 'localhost',  # El host de la base de datos
        'PORT': '3306',  # El puerto de la base de datos
      }
    }
  ```
  - Una vez hecho esto, abrimos la consola de comandos y ejecutamos el siguiente comando:
  ```console
  python3 manage.py migrate
  ```
  <div style="page-break-after: always;"></div>

  - Nos deberia salir algo como esto:
  ```console
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
  Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying sessions.0001_initial... OK
  ```

  - Una vez ejecutado el comando, ya tendremos la base de datos configurada, si miras la base de datos ahora veras que se han creado unas tablas, como las siguientes:
  ```console
  +------------------------------------+
  | Tables_in_empleados                |
  +------------------------------------+
  | auth_group                         |
  | auth_group_permissions             |
  | auth_permission                    |
  | auth_user                          |
  | auth_user_groups                   |
  | auth_user_user_permissions         |
  | contenido_contenido                |
  | django_admin_log                   |
  | django_content_type                |
  | django_migrations                  |
  | django_session                     |      
  | empleados                          |
  +------------------------------------+
  ```

  Si no se crea la tabla contenido_contenido, ejecuta el siguiente comando:
  ```console
  python3 manage.py makemigrations contenido
  ```

  Así ya debería crearse la tabla contenido_contenido, en esa tabla es donde vamos a guardar los datos de los empleados.

  - Nos iremos crud > __init__.py y escribiremos el siguiente código:
  ```python
  import pymysql
  pymysql.install_as_MySQLdb()
  ```

  - Ejecutaremos este comando para reestructurar la base de datos:
  ```console
  python3 manage.py migrate
  ```
  - Nos deberia salir algo como esto:
  ```cponsole
  Operations to perform:
    Apply all migrations: admin, auth, contenido, contenttypes, sessions
  Running migrations:
    Applying contenido.0001_initial... OK
  ```
  - Y por último ejecutaremos este comando para crear un superusuario:
  ```python
  python3 manage.py createsuperuser
  ```
  - Nos deberia salir algo como esto:
  ```console
    Username (leave blank to use 'javi'): javi
    Email address: javinievas16@gmail.com
    Password: 
    Password (again): 
    The password is too similar to the username.
    This password is too short. It must contain at least 8 characters.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
  ```
  - Una vez hecho esto, ya tendremos la base de datos configurada.
  
  - Para comprobar que todo funciona correctamente, ejecutaremos el siguiente comando:
  ```console
  python3 manage.py runserver
  ```

  - Una vez cargado el servidor, abriremos el navegador y escribiremos la siguiente url:
  ```console
  http://http://127.0.0.1:8000/admin
  ```
  Una vez ahí escribiremos el usuario y la contraseña que hemos creado anteriormente.

  Se abrira una página donde podremos ver las tablas que hemos creado anteriormente, si pinchamos en contenido, podremos ver los datos que hemos creado anteriormente o bien crear nuevos datos.

  ### Pasos a seguir para crear el crud
  [Tabla de contenidos](#tabla-de-contenidos)

  #### Creacion de las rutas

  - Para crear las rutas, abriremos el archivo urls.py de la carpeta contenido y escribiremos el siguiente código:
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.principal, name='principal'),
        path('inicio', views.inicio, name='inicio'),
        path('empleados', views.empleados, name='empleados'),
        path('empleados/crear', views.crear, name='crear'),
        path('empleados/editar', views.editar, name='editar'),
        path('eliminar/<int:id>', views.eliminar, name='eliminar'),
        path('empleados/editar/<int:id>', views.editar, name='editar')

    ]
    ```

    - Una vez hecho esto, abriremos el archivo urls.py de la carpeta crud y escribiremos el siguiente código:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('contenido.urls'))
    ]
    ```

    Importante recalcar el name de las rutas que hemos creado, ya que lo utilizaremos más adelante. Para conectar las vistas con las rutas.

    #### Creación de las vistas
    [Tabla de contenidos](#tabla-de-contenidos)

    - Para crear las vistas, abriremos el archivo views.py de la carpeta contenido y escribiremos el siguiente código:
    ```python
    from django.shortcuts import render, redirect
    from django.http import HttpResponse, HttpResponseRedirect
    from .models import Contenido
    from .forms import ContenidoForm
    # Create your views here.

    def principal(request):
        return render(request, 'paginas/inicio.html')
    def inicio(request):
        return render(request, 'paginas/inicio.html')
    def empleados(request):
        contenidos = Contenido.objects.all()
        return render(request, 'empleados/index.html', {'contenidos': contenidos})
    def crear(request):
        formulario = ContenidoForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleados')
        return render(request, 'empleados/crear.html', {'formulario': formulario})
    def editar(request, id):
        empleado = Contenido.objects.get(id=id)
        formulario = ContenidoForm(request.POST or None, request.FILES or None, instance=empleado)
        if formulario.is_valid() and request.POST:
            formulario.save()
            return redirect('empleados')
        return render(request, 'empleados/editar.html', {'formulario':formulario})
    def eliminar(request, id):
        contenido = Contenido.objects.get(id=id)
        contenido.delete()
        return redirect('empleados')
    ```

    La función debe tener el mismo nombre que el name de la ruta, para que se conecten correctamente.

    La singularidad de las funciones empleados, crear, editar y eliminar, es que se conectan con la base de datos, para poder crear, editar y eliminar datos.

    La función empleados, se conecta con la base de datos y muestra todos los datos que hay en la base de datos.

    La función crear, se conecta con la base de datos y si el formulario es valido guarda el empleado en la base de datos y te redirigue a la pantalla de empleados.

    La función borrar, se conecta con la base de datos y borra el empleado que le hayas indicado y pasado por url el id y te redirigue a la pantalla de empleados.

    La función editar, se conecta con la base de datos y si el formulario es valido y se ha pasado correctamente el id del empleado se edita en la base de datos y te redirigue a la pantalla de empleados.

    #### Creación de los templates
    [Tabla de contenidos](#tabla-de-contenidos)

    - La creación de los templates es muy sencilla, simplemente debemos crear una carpeta llamada templates en la carpeta contenido, y dentro de la carpeta templates, crearemos otra carpeta llamada paginas y empleados, y dentro de la carpeta paginas crearemos los archivos html que necesitemos.
    - Crearemos una plantilla, que sera la base de todas las demás, para ello crearemos un archivo llamado base.html y escribiremos el siguiente código:
    ```html
    {% load static %}
    <!doctype html>
    <html lang="en">
        <head>
            <title> {% block titulo %} {% endblock %} </title>
            <!-- Required meta tags -->
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>

            <!-- Bootstrap CSS v5.2.1 -->
            <link
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                rel="stylesheet"
                integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                crossorigin="anonymous"
            />
        </head>

        <body>
            <nav class="navbar navbar-expand navbar-light bg-light">
                <div class="nav navbar-nav">
                    <a class="nav-item nav-link active" href="{% url 'inicio' %}" >Inicio</a>
                    <a class="nav-item nav-link active" href="{% url 'empleados' %}">Empleados</a>
                </div>
            </nav>


            <div class="container">
                <div class="row">
                    <div class="col-12">
                        {% block contenido %} {% endblock %}
                    </div>
                </div>
            </div>


            <script
                src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
                integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
                crossorigin="anonymous"
            ></script>

            <script
                src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
                integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+"
                crossorigin="anonymous"
            ></script>
        </body>
    </html>
    ```

    En este caso la plantilla es un navbar que nos ayudara a navegar por la aplicación más comodamente.

    La etiqueta {% load static %} en Django se utiliza para cargar el módulo de archivos estáticos. Esto es necesario cuando quieres acceder a tus archivos estáticos, como imágenes, CSS o JavaScript, en tus plantillas de Django.

    El código {% block titulo %} {% endblock %} en Django es una declaración de bloque en una plantilla. Este bloque puede ser sobreescrito por las plantillas que heredan de esta.
    Los bloques, como {% block titulo %}, son áreas en tu plantilla base que puedes definir para ser llenadas con contenido personalizado en las plantillas que heredan de la base. Por ejemplo, puedes tener un bloque para el título de la página, y cada plantilla que hereda de la base puede proporcionar su propio título.


  <div style="page-break-after: always;"></div>

  #### Creación de FORMS.py
  [Tabla de contenidos](#tabla-de-contenidos)

    - Para crear el archivo forms.py, abriremos la carpeta contenido y crearemos un archivo llamado forms.py y escribiremos el siguiente código:
    ```python
    class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = '__all__'
    ```
    Este archivo nos ayudara a crear los formularios de la aplicación.