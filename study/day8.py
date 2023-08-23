# -*- coding: utf-8 -*-
"""
@Time:2023/8/19 17:58
@Auth:kirosbaby
@QQ:308902181
"""
import pymysql, faker

'''
ip = '192.168.31.44'
user = 'root'
pwd = '123456'
db = 'class_20'
port = 3306
value = pymysql.Connect(host=ip, user=user, password=pwd, db=db, port=port)
curses = value.cursor()  # 游标
curses.execute('select * from score')  # 游标执行sql语句
# print(curses.fetchall())  # 返回所有数据---元组
print(curses.fetchone())
print(curses.fetchmany(2))

'''


class Test_MySql():
    def __init__(self):
        try:
            self.ip = '192.168.31.44'
            self.user = 'root'
            self.pwd = '123456'
            self.db = 'class_20'
            self.port = 3306
            self.value = pymysql.Connect(host=self.ip, user=self.user, password=self.pwd, db=self.db, port=self.port)
            self.curses = self.value.cursor()
        except Exception as e:
            print(e)

    def select(self, sql_select):
        try:
            self.curses.execute(sql_select)
            return self.curses.fetchall()
        except Exception as e:
            print(e)
    # def create(self):
    #     with open(r'D:\class_project\study_kiros_0814\file_test\test.sql', 'r', encoding='utf-8') as file_sql:
    #         value = file_sql.read()
    #         self.curses.execute(value)
    #         self.value.commit()  # 提交入库

    def insert(self, sql_insert):
        self.curses.execute(sql_insert)
        self.value.commit()

    def update(self, sql_update):
        self.curses.execute(sql_update)
        self.value.commit()

    def delete(self, sql_delete):
        self.curses.execute(sql_delete)
        self.value.commit()


if __name__ == '__main__':
    test_sql = Test_MySql()
    # print(test_sql.select('select * from user_address_ysq'))
    # test_sql.insert("insert into user_address_ysq values('0001','ysq','ysq20189','18720705627','萧山区杜湖名庭') ")
    # fak = faker.Faker('zh_CN')
    # for i in range(5,500):
    #     test_sql.insert(f"insert into user_address_ysq values({i},'{fak.name()}','{fak.password()}','{fak.phone_number()}','{fak.address()}')")
    #     print(i)
    test_sql.update("update user_address_ysq set name = '杨世钦' where address_id = '1' ")
    test_sql.delete('delete from user_address_ysq where address_id = 2')
