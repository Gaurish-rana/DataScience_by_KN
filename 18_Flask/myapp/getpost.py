from flask import Flask , render_template, request

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) Application.
'''

# WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask</H1></html"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name'] # It fetches the value entered in a form field named `name` from an HTTP POST request and stores it in the variable `name`.

        return f'Hello {name}!'
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True) # debug=True, automatically restart the server