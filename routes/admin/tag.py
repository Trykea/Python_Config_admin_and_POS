from app import app, render_template, request, engine
from sqlalchemy import create_engine, text


connection = engine.connect()


@app.get('/admin/tag')
def tag():
    module = 'tag'
    return render_template('admin/tag.html', module=module)


@app.get('/admin/get-tag')
def gettag():
    return gettagList()


@app.post('/admin/create-tag')
def createtag():
    form_date = request.get_json()
    name = form_date['name']
    description = form_date['description']

    result = connection.execute(text(f"INSERT INTO `tag` VALUES(null,'{name}','{description}')"))
    connection.commit()
    return [name, description]


@app.post('/admin/delete-tag')
def deletetag():
    form_date = request.get_json()
    tag_id = form_date['tag_id']
    result = connection.execute(text(f"DELETE FROM `tag` WHERE id={tag_id}"))
    connection.commit()
    return [tag_id]


@app.post('/admin/update-tag')
def updatetag():
    form_date = request.get_json()
    tag_id = form_date['id']
    name = form_date['name']
    description = form_date['description']
    result = connection.execute(text(f"  UPDATE tag SET name = '{name}', description = '{description}' WHERE id={tag_id}"))
    connection.commit()
    return [tag_id, name, description]


def gettagList():
    result = connection.execute(text("SELECT * FROM tag"))
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