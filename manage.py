#coding:utf-8

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from question import app
from exts import db
from models import UserModel

migrate=Migrate(app,db)

manager2=Manager()

@manager2.command
def abcd():
    print 'hello dito'


manager=Manager(app)#主命令管理工具
manager.add_command('db',MigrateCommand)#类似django，数据迁移
manager.add_command('abcd',manager2)
#python manager.py db migrate
# 3个命令init migrate upgrade
#python manager.py abcd abcd
#migrations 里的versions


if __name__ == '__main__':
    manager.run()
    #relevant to mysql---model