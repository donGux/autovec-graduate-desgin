from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,EqualTo #验证数据不能为空，数据是否相同
from flask import render_template

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# from flask import  Flask
# app=Flask(__name__)
#
class register(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField(label='密码', validators=[DataRequired('密码不能为空'),EqualTo('password')])
    submit = SubmitField(label='提交')



