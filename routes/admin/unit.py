from app import app, render_template, request, engine
from sqlalchemy import create_engine, text


connection = engine.connect()


@app.get('/admin/unit')
def unit():
    module = 'unit'
    return render_template('admin/unit.html', module=module)


@app.get('/admin/get-unit')
def getunit():
    return getunitList()


@app.post('/admin/create-unit')
def createunit():
    form_date = request.get_json()
    name = form_date['name']
    description = form_date['description']

    result = connection.execute(text(f"INSERT INTO `unit` VALUES(null,'{name}','{description}')"))
    connection.commit()
    return [name, description]


@app.post('/admin/delete-unit')
def deleteunit():
    form_date = request.get_json()
    unit_id = form_date['unit_id']
    result = connection.execute(text(f"DELETE FROM `unit` WHERE id={unit_id}"))
    connection.commit()
    return [unit_id]


@app.post('/admin/update-unit')
def updateunit():
    form_date = request.get_json()
    unit_id = form_date['id']
    name = form_date['name']
    description = form_date['description']
    result = connection.execute(text(f"  UPDATE unit SET name = '{name}', description = '{description}' WHERE id={unit_id}"))
    connection.commit()
    return [unit_id, name, description]


def getunitList():
    result = connection.execute(text("SELECT * FROM unit"))
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