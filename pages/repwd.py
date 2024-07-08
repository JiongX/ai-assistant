import random
import re
import time

import streamlit as st

from dao.UserDao import query_user_exist, add_user, update_user
from util.style_util import main_bg

main_bg("pages/img_2.png")
st.title("修改密码")

#注册输入框

usr = st.text_input("输入账号")
pwd = st.text_input("输入密码")



pwd2 = st.text_input("请再次输入密码")
reg_flag = st.button("修改密码")
#login_flag = st.button("已有账号？点击登录")


def register(usr, pwd, pwd2):
    #数据过滤
    if usr and pwd and pwd2:
        if pwd != pwd2:
            st.error("密码和重复密码不一致");return
        elif not re.match("[13|15|17|18|19][0-9]{9}", usr):
            st.error("手机号格式错误");return
        elif not re.match("[0-9a-zA-Z_-]{8,20}", pwd):
            st.error("密码格式错误");return
        elif not query_user_exist(usr):
            st.error("用户不存在");return
        #add_user(usr, pwd)
        update_user(usr,pwd)
        st.success("修改密码成功")
        time.sleep(2)
        st.switch_page("login.py")


    else:
        st.error("用户名或者密码和重复密码为空")

#点击登录切换页面
#if login_flag:
#    st.switch_page("login.py")

#点击去尝试注册
if reg_flag:
    register(usr, pwd, pwd2)
