from flask import render_template, request, redirect, url_for
from app import app
from app.forms import LoginForm, register
from app import User, Book


@app.route('/')
@app.route('/home')
def index(): #request.form.get()获取前端数据
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

from flask import  flash, redirect


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are valid (you can implement your own validation logic here)
        if username == 'myusername' and password == 'mypassword':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def Register():
    #创建表单对象
    form = register()

    # if request.method=='GET':
    #     return render_template()
    # if request.method=='POST':
    #     return render_template()

    return render_template('register.html', title='Register', form=form)

@app.route('/recommend')
def recommend():

    return render_template('recommend.html')

@app.route('/hot')
def hot():

    return render_template('hotrecommend.html')

@app.route('/newbooks')
def new():

    return render_template('newbook.html')

@app.route('/categories')
def cat():
    # 获取 category 参数
    BookID = request.args.get('BookID')
    # 在这里编写代码，根据 category 参数查询相应的书籍
    books_list = Book.query.filter_by(BookID=BookID).all()
    return render_template('categories.html', books=books_list)

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('user.html', users=users)


