from flask import Flask

'''
it creates an instance of the flask ckass, 
which will be your WSGI(web server gateway interface) application
'''
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to My First Flask Web Application"

@app.route("/demo")
def demo():
    return "hi all this is an demo page"

if __name__=="__main__":
    app.run(debug=True)