# 把数据库中的表数据以表格的形式展示到界面中
# 使用pymysql+streamlit技术
# 在界面中有一个点击按钮，当点击按钮之后再进行数据的展示
import streamlit as st
import pymysql
# 按钮的返回值是一个boolean类型的值，如果为true代表点击了按钮
flag = st.button("展示")
#查询数据库的数据，并且把数据封装为表格所需要的形式
#{
#    "列名":[],
#}
def get_users():
    conn = pymysql.connect(user="root",password="root",host="127.0.0.1",port=3306,charset="utf8",database="demo",cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from demo_user"
    cursor = conn.cursor()
    cursor.execute(sql)
    #[{"user_id":1,"username":"",""},{}]
    result = cursor.fetchall()
    a=[]
    b=[]
    c=[]
    for user in result:
        a.append(user['user_id'])
        b.append(user['username'])
        c.append(user['password'])
    dict = {
        "user_id":a,
        "username":b,
        "password":c
    }
    return dict

if flag:
    st.table(get_users())
