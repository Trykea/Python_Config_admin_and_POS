from app import app, render_template, request, engine
from sqlalchemy import create_engine, text


connection = engine.connect()


@app.get('/admin/brand')
def brand():
    module = 'brand'
    return render_template('admin/brand.html', module=module)


@app.get('/admin/get-brand')
def getbrand():
    return getbrandList()


@app.post('/admin/create-brand')
def createbrand():
    form_date = request.get_json()
    name = form_date['name']
    description = form_date['description']

    result = connection.execute(text(f"INSERT INTO `brand` VALUES(null,'{name}','{description}')"))
    connection.commit()
    return [name, description]


@app.post('/admin/delete-brand')
def deletebrand():
    form_date = request.get_json()
    brand_id = form_date['brand_id']
    result = connection.execute(text(f"DELETE FROM `brand` WHERE id={brand_id}"))
    connection.commit()
    return [brand_id]


@app.post('/admin/update-brand')
def updatebrand():
    form_date = request.get_json()
    brand_id = form_date['id']
    name = form_date['name']
    description = form_date['description']
    result = connection.execute(text(f"  UPDATE brand SET name = '{name}', description = '{description}' WHERE id={brand_id}"))
    connection.commit()
    return [brand_id, name, description]


def getbrandList():
    result = connection.execute(text("SELECT * FROM brand"))
    recode = result.fetchall()
    data = []
    for item in recode:
        data.append({
            'id': item[0],
            'name': item[1],
            'description': item[2],
        })
    connection.commit()
    return data