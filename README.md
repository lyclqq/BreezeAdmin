# BreezeAdmin
这是一个基于flask的后端管理模板。他实现了用户登陆验证与菜单权限管理。他的优势是结构简单，没有数据库，菜单是存在json中。用户可以根据自己的需要对接其他用户管理系统，只要传session过来就可以。

在 static/files/menu.json 中有json文件，用于保存菜单。

session['username']保存用户名，用于验证是否登陆
session['usermenu']该用户的菜单,以'01010'形式，对应菜单的id，0表示无权限，1表示有权限
