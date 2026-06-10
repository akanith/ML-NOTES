from flask import Flask,render_template,request,redirect,url_for

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

@app.route('/sumbit',methods=['GET','POST'])
def sumbit():
    if request.method=='POST':
        name =request.form.get("name")
        email =request.form.get("email")
        return f'Hello {name}!'
    return render_template('form.html')

## Variable rule
@app.route('/success/<int:score>')
def success(score):
    return render_template("result.html", score=score)

## Variable rule
@app.route('/successresult/<int:score>')
def successresult(score):
    res=""
    if int(score)>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score,'result':res}
    return render_template("result1.html",res=exp)

## if condition in jinja template
@app.route('/successif/<int:score>')
def successif(score):
    return render_template("result.html", score=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template("result.html", score=score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science =float(request.form.get("Science", 0))
        maths =float(request.form.get("Maths", 0))
        english =float(request.form.get("English", 0))
        c =float(request.form.get("c", 0))
        total_score=(science+maths+english+c)/4
        return redirect(url_for("successresult",score=int(total_score)))
    return render_template("getresult.html")

if __name__=="__main__":
    app.run(debug=True)