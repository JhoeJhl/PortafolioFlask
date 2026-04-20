from flask import Flask, render_template

app = Flask(__name__)

#Proyectos y Tecnologias
proyectos_data = [
    {
        "titulo": "E-Learning Platform",
        "descripcion": "Sistema tipo Udemy con Laravel y Vue.js.",
        "tecnologias": ["Laravel", "Vue", "Inertia"],
        "link": "#"
    },
    {
        "titulo": "Pharmacy Web",
        "descripcion": "Gestión de inventarios para farmacias locales.",
        "tecnologias": ["PHP", "MySQL", "JavaScript"],
        "link": "#"
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