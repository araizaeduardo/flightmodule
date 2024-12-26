# Buscador de Vuelos con Amadeus API

Este proyecto es un buscador de vuelos que utiliza la API de Amadeus para buscar vuelos de ida y vuelta. La aplicación está construida con Flask y proporciona una interfaz web moderna y fácil de usar.

## Requisitos Previos

- Python 3.x
- pip (gestor de paquetes de Python)
- Credenciales de API de Amadeus (Test Environment)

## Configuración del Entorno

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd amadeusai
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate  # En Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
   - Crear un archivo `.env` en la raíz del proyecto
   - Agregar las siguientes variables:
   ```env
   AMADEUS_API_KEY="tu_api_key_aquí"
   AMADEUS_API_SECRET="tu_api_secret_aquí"
   ```
   Puedes obtener estas credenciales registrándote en [Amadeus for Developers](https://developers.amadeus.com/)

## Ejecución

Para ejecutar la aplicación:

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5005`

## Características

- Búsqueda de vuelos de ida y vuelta
- Selección de fechas con calendario interactivo
- Visualización de precios y detalles de vuelos
- Interfaz responsiva y moderna
- Manejo de errores y validaciones
- Soporte para múltiples segmentos de vuelo

## Estructura del Proyecto

```
amadeusai/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias del proyecto
├── .env               # Variables de entorno (no incluido en git)
├── .gitignore         # Archivos ignorados por git
└── templates/         # Plantillas HTML
    └── index.html     # Página principal
```

## Notas de Seguridad

- Nunca comitear el archivo `.env` al repositorio
- Las credenciales de API están configuradas para el entorno de pruebas
- Para producción, actualizar las URLs de API a las de producción

## Contribuir

1. Fork el repositorio
2. Crear una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request
