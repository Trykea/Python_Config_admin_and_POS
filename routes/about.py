from app import app, render_template

@app.route('/about')
def about():
    return render_template('about.html')
