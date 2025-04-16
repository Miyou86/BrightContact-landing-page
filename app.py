from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para mostrar la página principal
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    #Verificar si hay campos vacíos
    if not name or not email or not message:
        return render_template('home.html', error="Todos los campos son obligatorios.", name=name, email=email, message=message)

    if '@' not in email:
        return render_template('home.html', error="Email inválido", name=name, email=email, message=message)
    
    #Guardar en archivo si todo está bien
    with open('submissions.txt', 'a') as file:
        file.write(f"Nombre: {name} - Email: {email} - Mensaje: {message}\n")

    return render_template('home.html', name=name, email=email, message=message)
    
if __name__ == '__main__':
    app.run(debug=True)
