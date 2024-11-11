from app import app, render_template

@app.route('/contact')
def contact():
    return render_template('contact.html')