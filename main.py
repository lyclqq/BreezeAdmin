#coding=utf-8
from flask import Flask,render_template,request,make_response,session,jsonify,current_app,redirect,flash,url_for

from io import BytesIO
from common import LoginForm,getKey,getVerifyCode,userLogin

app=Flask(__name__,static_url_path='/',template_folder='templates')
app.config.from_pyfile("config.py")


#自定义出错页
@app.errorhandler(404)
def page_not_found(e):
    return 'there is not'

#验证是否登陆
@app.before_request
def islogin():
    url = request.path
    #不验证页面与文件
    pass_list = ['/login','/code','/','/imgCode','/css','/fonts','/img','/static/js','/ueditor']
    suffix=url.endswith('.png') or url.endswith('.jpg') or url.endswith('.css')
    if request.path in pass_list or suffix:
        return None
    if not session.get("username"):
        return redirect("/login")


@app.route('/imgCode')
def imgCode():
    return getImgCode()

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        captcha = request.form.get('verify_code')
        username=request.form.get('username')
        password=request.form.get('password')
        if session.get('imageCode')==captcha:
            if userLogin(username=username,password=password):
                #验证成功，跳转
                return redirect(url_for('admin.admin'))
            else:
                flash('用户名或密码错误')
                return render_template('login.html', form=form)
        else:
            flash('验证码错误')
            return render_template('login.html',form=form)
    else:
        return render_template('login.html',form=form)

#生成验证码图片
def getImgCode():
    imgKey=getKey()
    image=getVerifyCode(imgKey)
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['imageCode'] = imgKey
    return response

if __name__=='__main__':
    #引用蓝图
    from controller.admin import *
    app.register_blueprint(admin_con)

    app.run('0.0.0.0', port=80, debug=True)