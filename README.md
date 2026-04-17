#  LLM Writing Assistant

Asistente de escritura impulsado por modelos de lenguaje de gran escala (LLM) utilizando la API de OpenAI. Este proyecto permite generar y mejorar textos de forma automática, enfocado en productividad y creación de contenido.

---

##  Funcionalidades

- Generación automática de correos profesionales
- Mejora de redacción y estilo de textos
- Integración directa con modelos de lenguaje (Google Gemini API)
- Arquitectura modular lista para escalar

---

##  Arquitectura del proyecto

app/
├── services/          # Integración con OpenAI
├── features/          # Lógica de negocio (writing assistant)
├── utils/             # Prompts reutilizables
├── config.py          # Configuración global
└── main.py            # Flujo principal

run.py                 # Entry point
tests/                 # Pruebas

---

##  Instalación

1. Clonar repositorio

git clone https://github.com/hybridgejosslyv/llm
cd llm-writing-assistant

2. Crear entorno virtual

python -m venv .venv

3. Activar entorno

Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

4. Instalar dependencias

pip install -r requirements.txt

---

##  Configuración

Crear archivo `.env` en la raíz:

OPENAI_API_KEY=tu_api_key_aqui

---

##  Ejecución

python run.py

---

##  Ejemplo de uso

1. Generar correo
2. Mejorar texto
Selecciona una opción:

---

## Tecnologías utilizadas

- Python 3
- Google Gemini API
- python-dotenv

---

##  Roadmap

- API REST con FastAPI
- Interfaz web
- Persistencia de historial
- Personalización de estilo de escritura
- SaaS multiusuario

---

##  Notas

- No subir el archivo `.env` (contiene credenciales)
- Proyecto enfocado en demostración de integración con LLM

---

##  Licencia

MIT License

---

##  Autor

Desarrollado como proyecto práctico de integración con modelos de lenguaje de gran escala. Ingenieria en Inteligencia Artificial Hybridge Education.