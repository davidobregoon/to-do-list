# 📝 To-Do List CLI

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Tests](https://img.shields.io/badge/tests-7%20passed-success.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Aplicación de línea de comandos desarrollada en **Python** para administrar tareas mediante un sistema CRUD completo con persistencia de datos en JSON.

El proyecto fue construido aplicando buenas prácticas de desarrollo:

- Arquitectura modular.
- Separación de responsabilidades.
- Programación orientada a objetos.
- Pruebas automatizadas.
- Formateo y análisis estático de código.

---

## 🚀 Características

- Crear tareas.
- Listar tareas.
- Editar tareas.
- Completar y descompletar tareas.
- Eliminar tareas.
- Persistencia automática en JSON.
- Validación de entradas.
- Tests automatizados.

---

## 📂 Estructura del proyecto

```text
to-list-cli/

├── src/
│   ├── models.py
│   ├── storage.py
│   ├── task_manager.py
│   ├── menu.py
│   └── utils.py
│
├── tests/
│   ├── test_storage.py
│   ├── test_task_manager.py
│   └── test_utils.py
│
├── data/
│   └── tareas.example.json
│
├── docs/
│   └── architecture.md
│
├── main.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## ⚙️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/davidobregoon/to-do-list.git
```

Entra al proyecto:

```bash
cd to-list-cli
```

Instala dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar aplicación

```bash
python main.py
```

Ejemplo:

```text
===== LISTA DE TAREAS =====

1. Agregar tarea
2. Ver tareas
3. Completar/descompletar tarea
4. Editar tarea
5. Eliminar tarea
6. Salir
```

---

## 🧪 Ejecutar pruebas

Ejecutar tests:

```bash
python -m pytest
```

Resultado esperado:

```text
7 passed
```

---

## 🛠️ Herramientas de desarrollo

### Formatear código

```bash
python -m black .
```

### Analizar código

```bash
python -m ruff check .
```

---

## 🏗️ Arquitectura

El proyecto utiliza una separación por capas:

```
Usuario
  |
  v
menu.py
  |
  v
task_manager.py
  |
  v
storage.py
  |
  v
JSON
```

Más información:

```
docs/architecture.md
```

---

## 📌 Próximas mejoras

- [ ] Buscar tareas.
- [ ] Filtrar tareas completadas.
- [ ] Base de datos SQLite.
- [ ] API REST.
- [ ] Interfaz gráfica.

---

## 📄 Licencia

Este proyecto está bajo licencia MIT.

---

## 👨‍💻 Autor

David Obregón

GitHub:
https://github.com/davidobregoon