from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "llave super secreta"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session['num_strawberry'] = request.form['strawberry']
    session['num_raspberry'] = request.form['raspberry']
    session['num_apple'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    print(request.form)
    name = request.form['first_name']
    total_fruits = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f'Cobrando a {name} por {total_fruits} frutas')
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    