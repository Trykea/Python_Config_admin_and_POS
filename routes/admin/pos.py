from app import app, render_template, request,engine
from sqlalchemy import create_engine, text
from routes.admin import category
from routes.admin import product

from sqlalchemy import create_engine, text

connection = engine.connect()


@app.get('/admin/pos')
def pos():
    module = 'pos'
    return render_template('admin/pos.html', module=module)

@app.get('/admin/get-by-category')
def getByCategory():
    category_id = request.args.get('category_id')
    filter_product = product.getproductByCategoryID(category_id)
    return filter_product
