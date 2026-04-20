from flask import Flask, render_template

app = Flask(__name__)

#Proyectos y Tecnologias
proyectos_data = [
    {
        "titulo": "Plataforma de Gestión Académica",
        "descripcion": "Sistema integral para instituciones: control de notas, asistencia, inscripciones y perfiles para docentes y alumnos.",
        "tecnologias": ["Laravel", "PostgreSQL", "Vue.js"],
        "nivel": "Avanzado"
    },
    {
        "titulo": "Dashboard de Métricas Empresariales",
        "descripcion": "Panel interactivo para la visualización de KPIs, reportes automáticos y análisis de datos en tiempo real.",
        "tecnologias": ["Inertia.js", "MySQL", "Tailwind"],
        "nivel": "Intermedio"
    },
    {
        "titulo": "E-commerce de Consumo Masivo",
        "descripcion": "Tienda virtual con carrito de compras, gestión de inventario y pasarela de pagos integrada.",
        "tecnologias": ["PHP", "JavaScript", "MySQL"],
        "nivel": "Intermedio"
    },
    {
        "titulo": "Sistema de Inventario para Pymes",
        "descripcion": "Control de stock, registro de ventas diarias y generación de recibos para negocios locales.",
        "tecnologias": ["Laravel", "Alpine.js"],
        "nivel": "Básico"
    },
    {
        "titulo": "Landing Page Corporativa",
        "descripcion": "Sitio web de alto rendimiento optimizado para SEO y conversión de clientes potenciales.",
        "tecnologias": ["HTML5", "Tailwind CSS", "JS"],
        "nivel": "Básico"
    },
    {
        "titulo": "Gestor de Tareas Colaborativo",
        "descripcion": "Aplicación para la organización de equipos con recordatorios y prioridades personalizables.",
        "tecnologias": ["PHP", "SQLite", "CSS3"],
        "nivel": "Básico"
    }
]

@app.route('/')
def index():
    return render_template('index.html', proyectos=proyectos_data)


@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html', proyectos=proyectos_data)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)