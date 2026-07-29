# 📝 Python To-Do List

Una aplicación de consola desarrollada en **Python** para gestionar tareas de forma sencilla y eficiente.

El proyecto implementa un sistema CRUD (Create, Read, Update, Delete) con persistencia de datos mediante archivos JSON, siguiendo buenas prácticas de programación y una arquitectura modular.

---

## ✨ Características

- ➕ Agregar tareas
- 📋 Listar tareas
- ✏️ Editar tareas
- ✅ Marcar y desmarcar tareas como completadas
- 🗑️ Eliminar tareas
- 💾 Guardado automático en JSON
- 🛡️ Validación de entradas
- 🧩 Código modular y fácil de mantener

---

## 📂 Estructura del proyecto

```text
to-do-list/
│
├── data/
│   └── tareas.json
│
├── docs/
│   ├── architecture.md
│   └── screenshots/
│
├── src/
│   ├── menu.py
│   ├── models.py
│   ├── storage.py
│   ├── task_manager.py
│   └── utils.py
│
├── tests/
│   ├── test_storage.py
│   ├── test_task_manager.py
│   └── test_utils.py
│
├── .github/
│   └── workflows/
│       └── python.yml
│
├── main.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## 🚀 Instalación

Clona el repositorio:

```bash
git clone https://github.com/davidobregoon/to-do-list.git
```

Entra al proyecto:

```bash
cd to-do-list
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta la aplicación:

```bash
python main.py
```

---

## 🛠️ Tecnologías

- Python 3
- JSON
- Dataclasses
- Pytest
- Git
- GitHub

---

## 📸 Capturas

Cuando el proyecto esté terminado puedes agregar imágenes aquí.

```text
docs/screenshots/menu.png
docs/screenshots/agregar.png
docs/screenshots/listar.png
docs/screenshots/editar.png
```

---

## 🧪 Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

---

## 📈 Próximas mejoras

- [ ] Buscar tareas
- [ ] Ordenar tareas
- [ ] Filtrar tareas completadas
- [ ] Exportar tareas a CSV
- [ ] Interfaz gráfica con Tkinter
- [ ] Base de datos SQLite

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.

Consulta el archivo `LICENSE` para más información.

---

## 👨‍💻 Autor

**David Obregón**

GitHub: https://github.com/davidobregoon