from flask import Blueprint,render_template,jsonify,session,current_app
import json

admin_con=Blueprint('admin',__name__)

#写session测试
@admin_con.route('/set')
def temp_set():
    session['username']='刘德华' #用户名
    session['usermenu']='101010' #菜单权限，1表示有权限，0表示无权限
    return 'set ok'

@admin_con.route('/admin')
def admin():
    username = session.get('username')
    usermenu = str(session.get('usermenu'))
    #从menu.json文件读取所有菜单
    f = open(current_app.config['UPLOAD_FOLDER'] + 'menu.json', 'r')
    allmenu = json.loads(f.readline())
    menu = []
    #按照菜单权限生成用户菜单
    for item in allmenu:
        ii = item.get('id')
        if usermenu[ii] == '1':
            menu.append(item)
    return render_template('temp.html', username=username, menu=menu)