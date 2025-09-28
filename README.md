# App Recetas (Proyecto Django)

Aplicación web desarrollada en **Django** como parte de un proyecto de aprendizaje.  
Permite registrar, listar y visualizar recetas de cocina.

---

## ⚙️ Requisitos
- Python 3.x
- Django 5.x (o la versión que uses)
- pip

---

## Instalación y uso

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/usuario/App_recetas.git
   cd App_recetas
   ```
2. Crear entorno virtual
```bash
python -m venv env
```
3. Activar entorno virtual
Windows (PowerShell):
```bash
.\env\Scripts\activate
```
Linux/Mac:
```bash
source env/bin/activate
```
4. Instalar dependencias
```bash
pip install -r requirements.txt
```
5. Migraciones iniciales
```bash
python manage.py migrate
```
6. Levantar servidor
```bash
python manage.py runserver
```
Abrir en el navegador:
👉 http://127.0.0.1:8000

📂 Estructura del proyecto
```bash
App_recetas/
│── manage.py
│── db.sqlite3
│── .gitignore
│── Recetas/        # Aplicación principal
│    ├── mi_app/    # Código de la app (models, views, templates, etc.)
│    └── media/     # Archivos estáticos/subidos
└── env/            # Entorno virtual (ignorado por Git)
```
📝 Notas
- El entorno virtual env/ está excluido con .gitignore.
- Puedes extender este proyecto agregando autenticación de usuarios, subida de imágenes de recetas o una API con Django REST Framework.
