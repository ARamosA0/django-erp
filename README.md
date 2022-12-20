# django-erp

## Como inicar el proyecto

Para iniciar el proyecto usar el comando:
- `docker compose up -d`
Esto correra el compose en segundo plano
Si se quiere ver los errores que salen en la terminal
- `docker compose up`

## Comandos de manage.py en doker

Para poder ejecutar un comando del proyecto es necesario:
    - `docker ps` -> Para ver los contenedores que estan corriendo
    - Copiar el **CONTAINER_ID**
    - `docker exec -it [CONTAINER_ID] python manage.py [comando que se quiera realizar]`