#coding:utf-8
from flask import Flask,views,render_template,request,redirect
from exts import db
app=Flask(__name__,static_folder='static',template_folder='template')
#试图函数   以后会有视图类 更高端 

#连数据库
import config
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('bt.html')
#
class ViewClass(views.MethodView):
    """docstring for ViewClass"""
    def get(self):
        return 'hihhhhhhhhhh'
    def post(self):
        pass#定义getpost
app.add_url_rule('/luyoumingzi',view_func=ViewClass.as_view('qigeminzi'))#添加路由。指定路由和视图      
#默认get请求
@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username']!='admin' or request.form['password']!='pass':
            error='invalid pls try again!!!'
        else: return redirect(url_for('index'))
        #302重定向与模板经常使用，找到函数名找到路由地址跳转
    return render_template('index.html',error=error)
    # return '<h1>welcom to flask</h1>'

    # return render_template('index.html')
if __name__ == '__main__':
    # app.debug=True
    # app.run(host='0.0.0.0',port=5000)
    app.run(debug=True)