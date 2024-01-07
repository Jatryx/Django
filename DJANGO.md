---
attachments: [Clipboard_2023-10-24-13-35-42.png, Clipboard_2023-10-24-13-36-21.png, Clipboard_2023-10-24-13-37-51.png, Clipboard_2023-10-24-14-10-11.png]
favorited: true
title: DJANGO
created: '2024-1-07'
modified: '2024-1-07'
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
    - [Instalación PyCharm](#instalación-pycharm)
  - [Capitulo 2](#capitulo-2)
    - [Subapartado 2.1](#subapartado-21)
  - [Capitulo 3](#capitulo-3)
    - [Seccion1](#seccion1)
    - [Seccion2](#seccion2)
      - [Seccion2.1](#seccion21)
  - [Clases](#clases)
  - [Clase 01 - 24/10](#clase-01---2410)

<div style="page-break-after: always;"></div>




## Introducción
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



## Instalación Django
[Tabla de contenidos](#tabla-de-contenidos)

Para instalar Django, necesitarás cumplir con algunos requisitos previos. A continuación, se detallan los pasos básicos para instalar Django en un entorno de desarrollo.

- Requisitos para instalar Django.
  - Actualizar el sistema: para ello debemos abrir la terminal y escribir el siguiente fragmento de codigo en la terminal.
  ```console
    sudo apt update
    sudo apt upgrade
  ```

  - Comprobamos la versión de python que tenemos.
  ```console
  pythom3 --version
  ```

  - Si no tenemos python instalado en nuestro equipo debemos escribir en la terminal el siguiente código:
  ```console
  sudo apt install python3
  ```
  Tenemos que tener cuidado con la versión que instalamos porque no puede ser compatible con django y nos va a dar problemas.

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

    Este comando crea un entorno virtual en un directorio llamado "django" en el directorio actual. Un entorno virtual es útil para aislar las dependencias de un proyecto Django específico.

    - Instalar el paquete python3.10-venv:
    ```console
    sudo apt install python3.10-venv
    ```

    Este comando instala el módulo venv específico de Python 3.10, que es necesario para crear entornos virtuales.

    - Crear nuevamente un entorno virtual llamado "django"
    ```console
    python3 -m venv django
    ```

    Aquí, estás volviendo a crear el entorno virtual. Si ya creaste uno en el primer paso, este comando no es necesario. Puedes omitirlo si ya tienes un entorno virtual creado.

    - Instalar Django dentro del entorno virtual:
    ```console
    pip install Django
    ```

    Este comando utiliza el gestor de paquetes pip para instalar la versión más reciente de Django dentro del entorno virtual "django".

    - Comprobamos la versión de Django que tenemos 
    ```console
    python3 -m django --version
    ```
    

### Instalación PyCharm
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
  
  Una vez dentro al final del documento debemos escribir la siguiente línea para crear un alias:

  ```console
    alias pyCharm="la ruta donde se encuentra este archivo"pyCharm-2023.3.1/bin/pycharm.sh
  ```

  Actualizar la Configuración del Shell:
  ```console
    source ~/.bashrc
  ```

<div style="page-break-after: always;"></div>

## Capitulo 2
[Tabla de contenidos](#tabla-de-contenidos)

### Subapartado 2.1
[Tabla de contenidos](#tabla-de-contenidos)

<div style="page-break-after: always;"></div>


## Capitulo 3
[Tabla de contenidos](#tabla-de-contenidos)

- Recursos: 
  - 

```php
echo "Hola Mundo";
```

### Seccion1
[Tabla de contenidos](#tabla-de-contenidos)

```console
#...
```



### Seccion2
[Tabla de contenidos](#tabla-de-contenidos)

```console
#...
```


#### Seccion2.1
[Tabla de contenidos](#tabla-de-contenidos)

1. **negrita**

```console
sudo apt update
sudo apt upgrade
```

2. Hm^3^
    - H~2~O

- dfgdlfkgdlfkj
- dflgjdlfkj

- [X] Hm^3^
    - H~2~O


## Clases 
[Tabla de contenidos](#tabla-de-contenidos)


## Clase 01 - 24/10
[Tabla de contenidos](#tabla-de-contenidos)

- [Web Notable](https://notable.app/)
  - https://notable.app/static/pdfs/cheatsheet.pdf
- [ ] https://github.com/twbs/bootstrap
- [ ] https://github.com/mermaid-js/mermaid

---

- [Apuntes de Docker](Docker.md "Introducción")

> IMPORTANTE: Para hacer una captura de pantalla simplemente hazla y pegala!!

![](@attachment/Clipboard_2023-10-24-14-10-11.png)
:angel::angel::angel::angel:
```python
user = "fulano"
```

