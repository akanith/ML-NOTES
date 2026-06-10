from flask import request
from flask import Flask,render_template

'''
it creates an instance of the flask ckass, 
which will be your WSGI(web server gateway interface) application
'''
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to My First Flask Web Application</h1></body></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/form",methods=["GET","POST"])
def form():
    if request.method =="POST" :
        name=request.form.get('name')
        email=request.form.get('email')
        result=f"Name: {name}, Email: {email}"
        return f'Hello {name} and {email} your data is submitted successfully'
    return render_template("form.html")

@app.route('/sumbit',methods=['GET','POST'])
def sumbit():
    if request.method=='POST':
        name =request.form.get("name")
        email =request.form.get("email")
        return f'Hello {name}!'
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)

# this is for learning get and post method
