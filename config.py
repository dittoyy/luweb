#coding:utf-8

HOSTNAME='mysql.xxx.com'
DB_PORT='3307'
DATABASE='zhihu'
USERNAME='root'
PASSWORD='test'
DB_URI='mysql+mysqldbL//{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,DB_PORT,DATABASE)

SQLALCHEMY_DATABASE_URI=DB_URI

SQLALCHEMY_TRACK_MODIFICSTIONS=False#关闭警告数据库信息