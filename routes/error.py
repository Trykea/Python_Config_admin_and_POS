from app import app, render_template

@app.errorhandler(404)
def error404(e):
    return render_template('Error/404.html')

@app.errorhandler(500)
def error500(e):
    return render_template('Error/500.html')
