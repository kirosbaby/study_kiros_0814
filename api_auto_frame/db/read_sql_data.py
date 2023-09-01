# -*- coding: utf-8 -*-
"""
@Time:2023/9/1 14:30
@Auth:kirosbaby
@QQ:308902181
"""
import pymysql
from utils.read_yaml import Read_Yaml
class Test_MySql():
    def __init__(self):
        read_y = Read_Yaml('data','login_mysql_data.yaml')
        dic = read_y.read_dict()
        try:
            self.value = pymysql.Connect(host=dic['host'], user=dic['user'], password=dic['password'], db=dic['db'], port=dic['port'])
            self.curses = self.value.cursor()
        except Exception as e:
            print(e)
    def select_user_id(self):
        try:
            self.curses.execute('select max(id) from sys_user')
            return self.curses.fetchall()[0][0]
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
    print(test_sql.select_user_id())
    # print(test_sql.select('select max(id) from sys_user')[0][0])
    # test_sql.insert("insert into user_address_ysq values('0001','ysq','ysq20189','18720705627','萧山区杜湖名庭') ")
    # fak = faker.Faker('zh_CN')
    # for i in range(5,500):
    #     test_sql.insert(f"insert into user_address_ysq values({i},'{fak.name()}','{fak.password()}','{fak.phone_number()}','{fak.address()}')")
    #     print(i)
    # test_sql.update("update user_address_ysq set name = '杨世钦' where address_id = '1' ")
    # test_sql.delete('delete from user_address_ysq where address_id = 2')