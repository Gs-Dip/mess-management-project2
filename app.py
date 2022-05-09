from flask import Flask,redirect,render_template,request,flash,session, url_for  



app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')    

@app.route('/usersignup')
def usersignup():
    return render_template('user_signup.html')    






if __name__=='__main__':
    app.run(debug=True,port=7800)