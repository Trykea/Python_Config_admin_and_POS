from app import app, render_template, request, engine
from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

connection = engine.connect()
@app.get('/admin/category')
def category():
    module ='category'
    return render_template('admin/category.html', module= module)

@app.get('/admin/get-category')
def getCategory():
    # result = connection.execute(text("SELECT * FROM category"))
    # record = result.fetchall()
    # data = []
    # for item in record:
    #     data.append(
    #         {
    #             'id' : item[0],
    #             'name': item[1],
    #             'description': item[2],
    #
    #
    #         }
    #     )
    # connection.commit()
    return getCategoryList()

@app.post('/admin/create-category')
def createCategory():
    form_date = request.get_json()
    category_id = form_date['id']
    name = form_date['name']
    description = form_date['description']
    result = connection.execute(text(f"INSERT INTO `category` VALUES (NULL,'{name}','{description}')"))
    connection.commit()
    return [name, description]


@app.post('/admin/delete-category')
def deleteCategory():
    form_date= request.get_json()
    category_id = form_date['category_id']
    result = connection.execute(
        text(f"DELETE FROM `category` WHERE id = '{category_id}'"))
    connection.commit()
    return [category_id]


@app.post('/admin/update-category')
def updateCategory():
    form_date = request.get_json()
    category_id = form_date['id']
    name = form_date['name']
    description = form_date['description']

    result = connection.execute(text(f"""
    UPDATE `category`
    SET `name` = '{name}',
    `description` = '{description}'
    WHERE
    id = '{category_id}'
    """))
    connection.commit()
    return [category_id, name, description]


def getCategoryList():
    result = connection.execute(text("SELECT * FROM category"))
    record = result.fetchall()
    data = []
    for item in record:
        data.append(
            {
                'id' : item[0],
                'name': item[1],
                'description': item[2],


            }
        )
    connection.commit()
    return data