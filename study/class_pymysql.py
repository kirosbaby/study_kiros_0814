# -*- coding: utf-8 -*-
"""
@Time:2023/8/21 9:48
@Auth:kirosbaby
@QQ:308902181
"""
import pymysql, faker, time



'''
class Test_MySql():
    def __init__(self):
        try:
            self.ip = 'kiros2023.mysql.polardb.rds.aliyuncs.com'
            self.user = 'kiros_ysq'
            self.pwd = 'YSQysq1995'
            self.db = 'study_kiros_0814'
            self.port = 3306
            self.value = pymysql.Connect(host=self.ip, user=self.user, password=self.pwd, db=self.db, port=self.port)
            self.curses = self.value.cursor()
        except Exception as e:
            print(e)

    def select(self, sql_select):
        try:
            self.curses.execute(sql_select)
            return self.curses.fetchall()
        except Exception as e :
            print(e)

    def create(self):
        with open(r'D:\class_project\study_kiros_0814\file_test\test.sql', 'r', encoding='utf-8') as file_sql:
            value = file_sql.read()
            self.curses.execute(value)
            self.value.commit()  # 提交入库

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
    print(test_sql.select('select * from user_address_ysq'))
    # print(test_sql.create())
    # test_sql.insert("insert into user_address_ysq values('0001','ysq','ysq20189','18720705627','萧山区杜湖名庭') ")

    for i in range(5,500):
        faker_1 = faker.Faker('zh_CN')
        test_sql.insert(f"insert into user_address_ysq values({i},'{faker_1.name()}','{faker_1.password()}','{faker_1.phone_number()}','{faker_1.address()}') ")
    # test_sql.update("update user_address_ysq set name = '杨世钦' where address_id = '1' ")
    # test_sql.delete('delete from user_address_ysq where address_id = 2')
    # test_sql.delete('truncate user_address_ysq')  # 批量删除表数据

'''


'''把异常捕获写成装饰器'''
def try_ext(func):
    def inner(*args):
        try:
           return func(*args)
        except Exception as e:
            return e
    return inner

class Test_MySql():
    @try_ext
    def __init__(self):
        self.ip = 'kiros2023.mysql.polardb.rds.aliyuncs.com'
        self.user = 'kiros_ysq'
        self.pwd = 'YSQysq1995'
        self.db = 'study_kiros_0814'
        self.port = 3306
        self.value = pymysql.Connect(host=self.ip, user=self.user, password=self.pwd, db=self.db, port=self.port)
        self.curses = self.value.cursor()

    @try_ext
    def select(self, sql_select):
            self.curses.execute(sql_select)
            return self.curses.fetchall()

    def create(self):
        with open(r'D:\class_project\study_kiros_0814\file_test\test.sql', 'r', encoding='utf-8') as file_sql:
            value = file_sql.read()
            self.curses.execute(value)
            self.value.commit()  # 提交入库

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
    print(test_sql.select('select * from user_address_ysq'))
    # print(test_sql.create())
    # test_sql.insert("insert into user_address_ysq values('0001','ysq','ysq20189','18720705627','萧山区杜湖名庭') ")

    # for i in range(5,500):
        # faker_1 = faker.Faker('zh_CN')
        # test_sql.insert(f"insert into user_address_ysq values({i},'{faker_1.name()}','{faker_1.password()}','{faker_1.phone_number()}','{faker_1.address()}') ")
    # test_sql.update("update user_address_ysq set name = '杨世钦' where address_id = '1' ")
    # test_sql.delete('delete from user_address_ysq where address_id = 2')
    # test_sql.delete('truncate user_address_ysq')  # 批量删除表数据