from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, redirect, url_for

from wtforms_fields import *





app = Flask(__name__)
app.secret_key = 'replace'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://karvmctpptpfsj:35f4c4a84695185a2f2372357eeb6540daf3c22e28b6e6cfa87dfde4f916c03b@ec2-52-44-166-58.compute-1.amazonaws.com:5432/d28ff46qf0u724"
db = SQLAlchemy(app)

db.create_all()
db.session.commit()





@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = Registeration()
    
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        
    # else:
    #     username = reg_form.username.data
    #     password = reg_form.password.data
    #     print('didnt validate')

        #for checking if someone has taken the username already
        
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return 'The username has been taken'
        
        #registering in the database and commiting and etc 
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))   
    return render_template('chatpage.html', form=reg_form)
        
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return 'Logged in!'

    return render_template('login.html', form=login_form)

        # return render_template('chatpage.html', form=reg_form)




    db.create_all()




if __name__ == '__main__':
    app.run(debug=True)
