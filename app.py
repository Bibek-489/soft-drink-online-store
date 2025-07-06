from flask import Flask, render_template, request, redirect, url_for, flash
from forms import SignupForm, LoginForm
from users import users, add_users

app = Flask(__name__)
app.config["SECRET_KEY"] = "1728fea11de1f2131857e082921c20ae"

products = {
    'cocktails': [
        {'id': 1, 'name': 'Mojito', 'description': 'Classic cocktail with rum, mint, lime, and soda water', 'price': 8.99, 'image': 'mojito.jpg'},
        {'id': 2, 'name': 'Piña Colada', 'description': 'Tropical cocktail with rum, coconut cream, and pineapple juice', 'price': 9.99, 'image': 'pina_colada.jpg'},
        {'id': 3, 'name': 'Margarita', 'description': 'Classic tequila cocktail with lime and triple sec', 'price': 7.99, 'image': 'margarita.jpg'}
    ],
    'freshjuices': [
        {'id': 4, 'name': 'Orange Fresh', 'description': 'Freshly squeezed orange juice', 'price': 4.99, 'image': 'orange_juice.jpg'},
        {'id': 5, 'name': 'Green Detox', 'description': 'Blend of spinach, apple, cucumber, and celery', 'price': 5.99, 'image': 'green_detox.jpg'},
        {'id': 6, 'name': 'Berry Blast', 'description': 'Mixed berry smoothie with strawberries, blueberries, and raspberries', 'price': 6.99, 'image': 'berry_blast.jpg'}
    ],
    'coffee': [
        {'id': 7, 'name': 'Espresso', 'description': 'Strong black coffee in small serving', 'price': 2.99, 'image': 'espresso.jpg'},
        {'id': 8, 'name': 'Cappuccino', 'description': 'Espresso with steamed milk and foam', 'price': 3.99, 'image': 'cappuccino.jpg'},
        {'id': 9, 'name': 'Latte', 'description': 'Espresso with steamed milk', 'price': 3.99, 'image': 'latte.jpg'}
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

@app.route('/alldrinks')
def alldrinks():
    all_drinks = {category: items for category, items in products.items()}
    return render_template('alldrinks.html', products=all_drinks)

@app.route('/cocktails')
def cocktails():
    return render_template('cocktails.html', cocktails=products['cocktails'])

@app.route('/freshjuices')
def freshjuices():  
    return render_template('freshjuices.html', freshjuices=products['freshjuices'])

@app.route('/coffee')
def coffee():
    return render_template('coffee.html', coffees=products['coffee'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        flash(f"Thanks for contacting us, {name}!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email in users:
            if password == users[email]["password"]:
                flash(f"Welcome back, {users[email]['name']}! 🎉", "success")
                return redirect(url_for("home"))
            else:
                flash("Wrong password!", "danger")
        else:
            flash("User not found!", "danger")

    return render_template("login.html", title="Login", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if request.method == "POST":
        email = form.email.data
        username = form.username.data

        if email in users:
            flash("Email already exists! Please use a different email.", "danger")
        else:
            add_users(email, username, form.password.data)
            flash(f"Welcome to Soft Drinks, {username}! 🎉 Account created successfully.", "success")
            return redirect(url_for("home"))

    return render_template("signup.html", title="SignUp", form=form)

if __name__ == '__main__':
    app.run(debug=True)
