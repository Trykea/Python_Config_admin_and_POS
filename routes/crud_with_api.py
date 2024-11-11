from sqlalchemy import create_engine, text
from flask import render_template, request, redirect, url_for
from app import app, engine


connection = engine.connect()
# @app.route('/crud')
# def crud():
#     result = connection.execute(text("SELECT * FROM user"))
#     data = result.fetchall()
#     connection.commit()
#     return render_template('crud.html', contacts=data)

# @app.get('/getUser')
# def getUser():
#     result = connection.execute(text("SELECT * FROM user"))
#     record = result.fetchall()
#     data = []
#     for item in record:
#         data.append(
#             {
#                 'id' : item[0],
#                 'name': item[1],
#                 'gender': item[2],
#                 'phone': item[3],
#                 'email':item[4]
#
#             }
#         )
#     connection.commit()
#     return data


# @app.post('/createUser')
# def createUser():
#     data = request.get_json()
#     name = data.get('name')
#     gender = data.get('gender')
#     phone = data.get('phone')
#     email = data.get('email')
#     result = connection.execute(text(f"INSERT INTO user values (null,'{name}','{gender}','{phone}','{email}')"))
#     connection.commit()
#     return ""


# @app.post('/deleteUser')
# def deleteUser():
#     data = request.get_json()
#     user_id = data.get('user_id')
#     result = connection.execute(text(f"DELETE FROM user WHERE id= {user_id}"))
#     connection.commit()
#     return f"{user_id}"

# @app.post('/updateUser')
# def updateUser():
#     data = request.get_json()
#     user_id = data.get('user_id')
#     name = data.get('name')
#     gender = data.get('gender')
#     phone = data.get('phone')
#     email = data.get('email')
#     result =  connection.execute(text(f"UPDATE user SET name = '{name}', gender = '{gender}', phone = '{phone}', email = '{email}' WHERE id = {user_id}"))
#     connection.commit()
#     return f"{name}"
