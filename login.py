import time

import streamlit as st

from dao.UserDao import query_user_by_username
from util.style_util import main_bg


st.set_page_config(
    page_title="ABCDEFG",
    page_icon="😀"
)
main_bg("pages/img_2.png")
st.title("登录")

#输入用户数据
usr = st.text_input("请输入用户名")
pwd = st.text_input("请输入密码",type="password")
loginFlag = st.button("登录")
registerFlag = st.button("注册")
repwdFlag = st.button("修改密码")

#点击注册按钮转到注册页面
if registerFlag:
    st.switch_page("./pages/register.py")

if repwdFlag:
    st.switch_page("./pages/repwd.py")

#点击登录尝试登录
if loginFlag:
    #if st.session_state.username:
    #    st.switch_page("./pages/GPT.py")
    if not (usr and pwd):
        st.error("密码或账户为空")
    elif user_info := query_user_by_username(usr):
        tb_name = user_info["username"]
        tb_uid = user_info["user_id"]
        tb_pwd = user_info["password"]
        if tb_name == usr and tb_pwd == pwd:
            st.session_state.username = usr
            st.session_state.uid = tb_uid
            st.success("登录成功")
            time.sleep(1)
            st.switch_page("./pages/GPT.py")
        else:
            st.error("密码错误")

    else:
        st.error("账户不存在")
