from app import app, render_template, request
from datetime import date
import requests
from helpers import helpers
@app.route('/')
@app.route('/home')
def home():
    student_list = [{'id': 'st001', 'name': 'vuthy', 'gender': 'male', 'profile': 'pic.jpg', },
                    {'id': 'st002', 'name': 'dara', 'gender': 'male', 'profile': 'pic.jpg', }

                    ]
    # print(arr)
    res = requests.get('https://fakestoreapi.com/products')
    res_json = res.json()
    return render_template('home.html', product_list=res_json)
@app.get('/shop_now')
def shopNow():
    id = request.args.get('id')
    res = requests.get(f"https://fakestoreapi.com/products/ {id}")
    json = res.json()
    return render_template('shop_now.html', product=json)


@app.get('/check_out')
def checkOut():
    id = request.args.get('id')
    res = requests.get(f"https://fakestoreapi.com/products/ {id}")
    json = res.json()
    return render_template('check_out.html', product=json)


@app.post('/confirmBooking')
def confirmBooking():
    product_id = request.form.get('product_id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    res = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    product = res.json()
    # return json

    bot_token = "7007744504:AAGuWNHDDXiIYjmypXovRU32WwLIa4m85Kk"
    chat_id = "@st89_message"
    msg = ("<strong>🔔 New Confirm Booking 🔔</strong>\n"
           "<code>Customer Name: {name}</code>\n"
           "<code>Customer Name: {phone}</code>\n"
           "<code>Customer Email: {email}</code>\n"
           "<code>Customer Address: {address}</code>\n"
           "<code>Booking Date📆: {date}</code>\n"
           "<code>=======================</code>\n"
           "<code>1 {product_name} 1*{product_price}</code>\n"
           ).format(name=name,
                    phone=phone,
                    email=email,
                    address=address,
                    date=date.today(),
                    product_name=product['title'],
                    product_price=product['price']
                    )
    notify_res = helpers.sendnotify(msg)
    return render_template('Order_Confirmation.html')

@app.post('/submit_contact')
def submitContact():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    bot_token = "7007744504:AAGuWNHDDXiIYjmypXovRU32WwLIa4m85Kk"
    chat_id = "@st89_message"
    msg = ("<strong>New Notification</strong>\n"
           "<code>Customer Name: {name}</code>\n"
           "<code>Customer Email: {email}</code>\n"
           "<code>Customer Address: {address}</code>\n"
           "<code>📆 {date}</code>\n"
           ).format(name=name, email=email, address=address, date=date.today(), )
    helpers.sendnotify(msg)
# @app.route('/product')
# def product():
#     return render_template('product card.html')
@app.route('/calc')
def calc():
    return render_template('calculator.html')

@app.route('/add-update__user')
def appUpdateUser():
    return render_template('add-update__user.html')