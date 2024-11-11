from sqlalchemy import create_engine, text
from flask import render_template, request, redirect, url_for
from app import app, engine

connection = engine.connect()
@app.route('/crud')
def crud():
    result = connection.execute(text("SELECT * FROM user"))
    data = result.fetchall()
    connection.commit()
    return render_template('crud.html', contacts=data)

@app.post('/create')
def create():
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    email = request.form.get('email')
    result = connection.execute(text(f"INSERT INTO user values (null,'{name}','{gender}','{phone}','{email}')"))
    # data = result.fetchall()
    # connection.commit()
    return redirect('/crud')

@app.get('/confirm_delete')
def confirm_delete():
    user_id = request.args.get('id')
    result = connection.execute(text(f"SELECT * FROM user WHERE id= {user_id}"))
    res = result.fetchall()
    connection.commit()
    data = []
    for user in res:
        data.append({
            'id': user[0],
            'name': user[1],
            'gender': user[2],
            'phone': user[3],
            'email': user[4]
        })
    return render_template('confirm_delete.html', data=data)



@app.get('/delete_user')
def delete_user():
    user_id = request.args.get('id')
    result = connection.execute(text(f"DELETE FROM user WHERE id= {user_id}"))
    connection.commit()
    return redirect('/delete')

@app.route('/delete')
def delete():
    result = connection.execute(text("SELECT * FROM user"))
    res = result.fetchall()
    connection.commit()
    return render_template('crud.html', contacts=res)

@app.get('/edit')
def edit():
    user_id = request.args.get('id')
    result = connection.execute(text(f"SELECT * FROM user WHERE id= {user_id}"))
    res = result.fetchall()
    connection.commit()
    data = []
    for user in res:
        data.append({
            'id': user[0],
            'name': user[1],
            'gender': user[2],
            'phone': user[3],
            'email': user[4]
        })
    # print(user[1])
    return render_template('edit.html', data=data)

@app.post('/update')
def update():
    id =request.args.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    email = request.form.get('email')
    result =  connection.execute(text(f"UPDATE user SET name = '{name}', gender = '{gender}', phone = '{phone}', email = '{email}' WHERE id = {id}"))
    connection.commit()
    # data = result.fetchall()
    # connection.commit()
    return redirect('/crud')
