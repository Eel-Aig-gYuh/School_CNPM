import math

from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    categories = dao.load_categories();

    kw = request.args.get('kw')

    page = request.args.get('page', 1)
    cate_id = request.args.get('category_id')
    prods = dao.load_products(cate_id=cate_id, kw=kw, page=int(page))

    page_size = app.config['PAGE_SIZE']
    total = dao.count_products()

    return render_template('index.html', category=categories, product=prods, page=math.ceil(total/page_size))


@app.route("/register")
def register_view():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)

