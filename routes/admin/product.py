from app import app, render_template, request,engine
from sqlalchemy import create_engine, text
from routes.admin import category
from routes.admin import unit
from routes.admin import brand
from routes.admin import tag
from sqlalchemy import create_engine, text

connection = engine.connect()


@app.get('/admin/product')
def product():
    module = 'product'
    return render_template('admin/product.html', module=module)


@app.get('/admin/get-product')
def getProduct():
    product_list = getProductList()
    category_list = category.getCategoryList()
    unit_list = unit.getunitList()
    brand_list = brand.getbrandList()
    tag_list = tag.gettagList()
    return {
        'product_list': product_list,
        'category_list': category_list,
        'unit_list': unit_list,
        'brand_list': brand_list,
        'tag_list': tag_list,
    }


@app.post('/admin/create-product')
def createProduct():
    form_date = request.get_json()
    name = form_date['name']
    cost = form_date['cost']
    price = form_date['price']
    category_id = form_date['category_id']
    unit_id = form_date['unit_id']
    brand_id = form_date['brand_id']
    tag_id = form_date['tag_id']
    description = form_date['description']

    result = connection.execute(text(f"INSERT INTO `product` VALUES(null,'{name}','{cost}','{price}','{category_id}','{unit_id}','{brand_id}','{tag_id}','{description}')"))
    connection.commit()
    return [name, cost, price, category_id, unit_id, brand_id, tag_id, description]


@app.post('/admin/delete-product')
def deleteProduct():
    form_date = request.get_json()
    product_id = form_date['product_id']
    result = connection.execute(text(f"DELETE FROM `product` WHERE id={product_id}"))
    connection.commit()
    return [product_id]


@app.post('/admin/update-product')
def updateProduct():
    form_date = request.get_json()
    product_id = form_date['id']
    name = form_date['name']
    cost = form_date['cost']
    price = form_date['price']
    category_id = form_date['category_id']
    unit_id = form_date['unit_id']
    brand_id = form_date['brand_id']
    tag_id = form_date['tag_id']
    description = form_date['description']
    # result = connection.execute(text(f"  UPDATE product SET name = '{name}', cost = '{cost}', '{price}','{category_id}','{unit_id}', '{brand_id}', '{tag_id}', '{description}' WHERE id={product_id}"))
    result = connection.execute(text(f"""
            UPDATE `product`
            SET 
                `name` = '{name}', 
                cost =  '{cost}', 
                price = '{price}',
                category_id = '{category_id}',
                unit_id = '{unit_id}',
                brand_id = '{brand_id}',
                tag_id = '{tag_id}',
                description = '{description}'
            WHERE id = {product_id}
    """))
    connection.commit()
    return [product_id, name, cost, price, category_id, unit_id, brand_id, tag_id, description]


def getProductList():
    result = connection.execute(text("""
            SELECT
              product.id,
              product.name,
              product.cost,
              product.price,
              category.`name` as category,
              unit.`name` as unit,
              brand.`name` as brand,
              tag.`name` as tag,
              product.description,
              category.`id` as category_id,
              unit.`id` as unit_id,
              brand.`id` as brand_id,
              tag.`id` as tag_id
          FROM
              product
                INNER JOIN category ON product.category_id = category.id
                INNER JOIN unit ON product.unit_id = unit.id
                INNER JOIN brand ON product.brand_id = brand.id
                INNER JOIN tag ON product.tag_id = tag.id;

      """))
    recode = result.fetchall()
    data = []
    for item in recode:
        data.append({
            'id': item[0],
            'name': item[1],
            'cost': item[2],
            'price': item[3],
            'category': item[4],
            'unit': item[5],
            'brand': item[6],
            'tag': item[7],
            'description': item[8],
            'category_id': item[9],
            'unit_id': item[10],
            'brand_id': item[11],
            'tag_id': item[12],
            'image': f"https://picsum.photos/id/2{item[0]}/150/150"
        })
    connection.commit()
    return data

def getproductByCategoryID(category_id):
    result = connection.execute(text(f"""
            SELECT
              product.id,
              product.name,
              product.cost,
              product.price,
              category.`name` as category,
              product.description,
              category.`id` as category_id
          FROM
              product
                INNER JOIN category ON product.category_id = category.id
        where category.`id` ={category_id}
        """))
    recode = result.fetchall()
    data = []
    for item in recode:
        data.append({
            'id': item[0],
            'name': item[1],
            'cost': item[2],
            'price': item[3],
            'category': item[4],
            'description': item[5],
            'category_id': item[6],
            'image': f"https://picsum.photos/id/2{item[0]}/150/150"

        })
    connection.commit()
    return data
