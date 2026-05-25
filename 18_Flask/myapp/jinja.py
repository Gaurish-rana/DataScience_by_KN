# Building URL Dynamically
# Jinja 2 Template Engine

'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''


from flask import Flask , render_template, request,redirect,url_for

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

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name'] # It fetches the value entered in a form field named `name` from an HTTP POST request and stores it in the variable `name`.

        return f'Hello {name}!'
    return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',results=res)


# Variable Rule
@app.route('/success_res/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score,"res":res}
    return render_template('result1.html',results=exp)


# If Condition 
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html',results=score)


@app.route('/successres/<int:score>')
def successresult(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score,"res":res}
    return render_template('result3.html',results=exp)
 
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result3.html',results=score)

@app.route('/submit_form/',methods=['POST','GET'])
def submit_form():
    total=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total=(science+maths+c+data_science)/4

    else:
        return render_template('result3.html')

    return redirect(url_for('successres',score=total))



if __name__=="__main__":
    app.run(debug=True) # debug=True, automatically restart the server