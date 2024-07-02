import bcrypt

__version__ = bcrypt.__version__

# Necesitamos esto para solucionar https://github.com/pyca/bcrypt/issues/684
# lo cual podría ser resuelto con una actualización de passlib[bcrypt] en el 
# futuro.

# Luego, en auth.py, importamos este módulo, y hasheamos y decodificamos
# manuelmente las contraseñas con los métodos de bcrypt "hashpw" y "checkpw".

# Se llegó a esta solución luego de evaluar la otra opción que era alterar
# la librearía bcrypt.py directamemte dentro del contenedor de Docker para
# obtener la la compatibilidad deseada con versiones previas de bcrypt. la
# cual no era una opción viable por la complejidad de alterar el 
# Dockerfile y la mantenibilidad del código a futuro, puesto a que una
# actualización de la librería podría sobreescribir los cambios realizados.