from flask import Flask, redirect, url_for, render_template
from forms import registerForm

app = Flask(__name__)
app.secret_key = 'sekretnyklucz'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def form():
    form = registerForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template('form-full.html', form=form)

@app.route("/success")
def success():
    return "Zalogowano!"

if __name__ == '__main__':
    app.run(debug=True)