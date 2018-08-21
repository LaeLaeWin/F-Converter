from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def cvstyle():
    return render_template('cvstyle.html')

@app.route('/dropdown')
def dropdown():
    return render_template('dropdown.html')

@app.route('/dropdown2')
def dropdown2():
    return render_template('dropdown2.html')

@app.route('/dropdown3')
def dropdown3():
    return render_template('dropdown3.html')

@app.route('/dropdown4')
def dropdown4():
    return render_template('dropdown4.html')

@app.route('/dropdown5')
def dropdown5():
    return render_template('dropdown5.html')

@app.route('/dropdown6')
def dropdown6():
    return render_template('dropdown6.html')

@app.route('/signup1')
def signup1():
    return render_template('signup1.html')

@app.route('/signin1')
def signin1():
    return render_template('signin1.html')

if __name__ == '__main__':
    app.run(debug=True)
