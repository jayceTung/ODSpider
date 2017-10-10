#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
from scrapy.utils.project import get_project_settings  # 导入seetings配置


class DBHelper:

    def __init__(self):
        self.settings = get_project_settings()
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.pwd = self.settings['MYSQL_PWD']
        self.db = self.settings['MYSQL_NAME']
        # self.host = '127.0.0.1'
        # self.port = 3306
        # self.user = 'root'
        # self.pwd = '123456'
        # self.db = 'spider'

    # 连接mysql
    def connect_mysql_database(self):
        conn = MySQLdb.connect(host=self.host,
                               user=self.user,
                               passwd=self.pwd,
                               db=self.db,
                               charset='utf8')
        # conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='test', charset='utf8')
        return conn

    # 只是连接mysql
    def connect_mysql(self):
        conn = MySQLdb.connect(host=self.host,
                               user=self.user,
                               passwd=self.pwd,
                               charset='utf8')
        # conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='test', charset='utf8')
        return conn

    # 创建数据库
    def create_database(self):
        conn = self.connect_mysql()

        sql = "create database if not exists " + self.db
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    # 创建表
    def create_table(self, sql):
        conn = self.connect_mysql_database()

        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    # 插入数据
    def insert(self, sql, *params):  # 注意这里params要加*,因为传递过来的是元组，*表示参数个数不定
        conn = self.connect_mysql_database()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()

        # 更新数据

    def update(self, sql, *params):
        conn = self.connect_mysql_database()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()

        # 删除数据

    def delete(self, sql, *params):
        conn = self.connect_mysql_database()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()


class Example:

    def __init__(self):
        self.dbHelper = DBHelper()

    def test_create_database(self):
        self.dbHelper.create_database()

    def test_create_table(self):
        sql = "create table test_table(id int primary key auto_increment, name varchar(50), url varchar(200))"
        self.dbHelper.create_table(sql)

    def test_insert(self):
        sql = "insert into test_table(name, url) values(%s, %s)"
        param = ("test", "test1")
        self.dbHelper.insert(sql, *param)


if __name__ == '__main__':
    exam = Example()
    # test.test_create_database()
    exam.test_create_table()
    # exam.test_insert()
