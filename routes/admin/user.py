from app import app, render_template, request, engine
from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

connection = engine.connect()
@app.get('/admin/user')
def user():
    module ='user'
    return render_template('admin/user.html', module= module)

@app.get('/admin/get-user')
def getUser():
    result = connection.execute(text("SELECT * FROM user"))
    record = result.fetchall()
    data = []
    for item in record:
        data.append(
            {
                'id' : item[0],
                'name': item[1],
                'gender': item[2],
                'password':"",
                # we dont need to show password for seccurity
                'phone': item[4],
                'email':item[5],
                'address': item[6]

            }
        )
    connection.commit()
    return data

@app.post('/admin/create-user')
def createUser():
    form_date= request.get_json()
    name = form_date['name']
    gender = form_date['gender']
    phone = form_date['phone']
    email = form_date['email']
    address = form_date['address']
    password = form_date['password']
    result = connection.execute(text(f"INSERT INTO `user` VALUES (NULL,'{name}','{gender}','{phone}','{email}','{address}','{password}')"))
    connection.commit()
    return [name, gender, phone, email, address, password]


@app.post('/admin/delete-user')
def deleteUser():
    form_date= request.get_json()
    user_id = form_date['user_id']
    result = connection.execute(
        text(f"DELETE FROM `user` WHERE id = '{user_id}'"))
    connection.commit()
    return [user_id]


@app.post('/admin/update-user')
def updateUser():
    form_date= request.get_json()
    user_id=form_date['id']
    name = form_date['name']
    gender = form_date['gender']
    phone = form_date['phone']
    email = form_date['email']
    address = form_date['address']
    password = form_date['password']

    result = connection.execute(text(f"""
    UPDATE `user`
    SET `name` = '{name}',
    gender = '{gender}', 
    `password` = '{password}',
    `phone` = '{phone}',
    `email`='{email}',
    `address` = '{address}'
    WHERE
    id = '{user_id}'
    """))
    connection.commit()
    return [user_id, name, gender, phone, email, address, password]
