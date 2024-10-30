from flask import render_template
import dao
from app import app


@app.route("/")
def index():
    categories = dao.load_categories();
    products = dao.load_products()
    return render_template('index.html', category=categories, product=products)


if __name__ == '__main__':
    app.run(debug=True)

