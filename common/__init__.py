
from flask import session
from wtforms import StringField,PasswordField,SubmitField,Form,widgets
from wtforms.validators import DataRequired,Length,Email
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
import string

#获取验证码文本
def getKey():
    return ''.join(random.sample(string.digits, 4))

#生成自体颜色
def rndColor():
    return (random.randint(16, 128), random.randint(16, 128), random.randint(16, 128))

#生成图形验证码
def getVerifyCode(imgKey):
    width, height = 120, 50
    # 新图片对象
    im = Image.new('RGB', (width, height), 'white')
    # 字体
    font = ImageFont.truetype('app/static/arial.ttf', 40)
    # draw对象
    draw = ImageDraw.Draw(im)
    # 绘制字符串
    for item in range(4):
        draw.text((5 + random.randint(-3, 3) + 23 * item, 5 + random.randint(-3, 3)),text=imgKey[item], fill=rndColor(), font=font)
    return im

#验证用户名密码并向session注入权限
def userLogin(username,password):

    session['username']='刘德华' #用户名
    session['usermenu']='101010' #菜单权限，1表示有权限，0表示无权限
    return True

class LoginForm(Form):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    username = StringField(
        validators=[
            DataRequired(message='用户名不能为空'),
            Length(min=4, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',
                   "placeholder":"输入注册用户名"}
    )
    password = PasswordField(
        # label='用户密码：',
        validators=[
            DataRequired(message='密码不能为空'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',
                   "placeholder": "输入用户密码"}
    )
    verify_code = StringField('验证码', validators=[DataRequired(), Length(1, 4)],render_kw={'class': 'form-control',
                   "placeholder":"输入验证码"})
    submit = SubmitField('登录',render_kw={'class':'btn btn-block btn-info'})
