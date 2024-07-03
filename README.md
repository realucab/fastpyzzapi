# Proyecto: fastpyzzapi (Gestión de restaurantes con fastAPI)

Este proyecto utiliza el enfoque de Desarrollo Orientado al Dominio (DDD) para desarrollar el backend de un sistema de gestión para una pizzería. El sistema podrá ser utilizado por administradores, chefs y clientes de la pizzería para gestionar inventarios de ingredientes, elaborar menús, procesar pedidos de clientes y generar reportes diversos.

En nuestro enfoque, determinamos que el mejor punto de comienzo fue la elaboración de un diagrama de dominio que siga al pie de la letra lo que hace un buen Diseño Orientado al Dominio (DDD), incluyendo agregados, entidades, objetos de valor, enums, servicios de dominio, eventos de dominio, así como interfaces para los repositorios de acceso a estas entidades. Cabe notar que se procuró mantener el dominio puro, libre de detalles de infraestructura; justo para eso es que usamos patrones de diseño, para colaborar con las entidades. Algunos de estos patrones son: Repositorio, Observador (para los eventos publicados), Factory (para la creación de agregados).

Mediante el uso de la interfaz Swagger UI de FastAPI, interactuamos con las distintas rutas, algunas con acceso a la base de datos PostgreSQL, y otras no... Todas las rutas están protegidas por autorización y autenticación usando librerías de hashing para almacenar las contraseñas junto a sus usuarios en la BD, y usando tokens JWT para las sesiones verificadas del usuario, con un plazo de expiración predefinido.

Todos los datos de entrada y salida de los endpoints se validan usando Pydantic, y el Decorador @as_pydantic_model transforma dinámicamente los objetos del dominio en sus respectivos modelos para salida del endpoint.

Los diferentes servicios permiten al usuario, dependiendo de su tipo de usuario, insertar datos para la administración de la pizzería, así como servicio de órdenes del menú para los clientes.

![alt text](<Diagrama Dominio Python.drawio.png>)


# Instrucciones para Arrancar y Ejecutar el Proyecto

Este documento proporciona una guía paso a paso para arrancar y ejecutar el proyecto de gestión de restaurantes con FastAPI.

## Requisitos Previos

Se deben tener instalados los siguientes programas:

1. **Docker** - Se puede descargar e instalar desde [aquí](https://www.docker.com/get-started).
2. **Docker Compose** - Normalmente viene incluido con la instalación de Docker.

## Construir y Ejecutar el Proyecto con Docker Compose

### Paso 1: Copiar y renombrar el archivo .env_template
Cambiar el nombre del archivo .env_template a .env

### Paso 2: Construir las Imágenes de Docker
Abrir un terminal y construir las imágenes de Docker especificadas en el archivo `docker-compose.yml` utilizando el siguiente comando:
```bash
docker compose build
```
### Paso 3: Iniciar los Servicios
Iniciar los servicios definidos en el archivo `docker-compose.yml` con el comando:
```bash
docker compose up
```
Este comando levantará los contenedores de la aplicación web y la base de datos. La aplicación web estará disponible en http://localhost:8000.

## Probar la Aplicación
Una vez que los contenedores estén en funcionamiento, se puede probar la aplicación utilizando un navegador web o herramientas como `curl` o `Postman`, o directamente con `Swagger`, que viene integrado en la aplicación, este último se puede revisar en la dirección:
```bash
http://localhost:8000/docs
```

## Integrantes:
* Andueza Ricardo
* Ascanio Paola
* Brito Angely
