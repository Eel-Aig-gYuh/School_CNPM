from app import app
from app.models import Category, Product


def load_categories():
    return Category.query.order_by("id").all()


def load_products(kw=None, cate_id=None, page=1):
    products = Product.query

    # tim kiem
    if kw:
        products = products.filter(Product.name.__contains__(kw))

    # phan trang
    if cate_id:
        products = products.filter(Product.category_id == cate_id)

    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    products = products.slice(start, start + page_size)

    # kiem tra loi
    # import pdb
    # pdb.set_trace()

    return products.all()


def count_products():
    return Product.query.count()