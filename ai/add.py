import random

import streamlit as st
import pymysql


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




username = st.text_input("请输入要添加的用户名")
password = st.text_input("请输入用户对应的密码",type="password")
flag = st.button("添加")
st.write(random.randint(1,100))

if flag:
    if username and password:
        conn = pymysql.connect(user="root", password="root", host="127.0.0.1", port=3306, charset="utf8",database="demo", cursorclass=pymysql.cursors.DictCursor)
        sql = "insert into demo_user(username,password) values(%s,%s)"
        conn.cursor().execute(sql,(username,password))
        conn.commit()
        st.write("添加成功")
        st.table(get_users())
    else:
        st.write("请输入要添加的信息！")
else:
    st.write("ppp")
    st.write("ppp")
    st.write("ppp")