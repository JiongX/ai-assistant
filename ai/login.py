import time

import streamlit as st

from dao.UserDao import query_user_by_username

st.set_page_config(
    page_title="ABCDEFG",
    page_icon="😀"
)

st.title("登录")

usr = st.text_input("请输入用户名")
pwd = st.text_input("请输入密码")
loginFlag = st.button("登录")
registerFlag = st.button("注册")


if registerFlag:
    st.switch_page("./pages/register.py")

if loginFlag:
    #if st.session_state.username:
    #    st.switch_page("./pages/GPT.py")
    if not (usr and pwd):
        st.error("密码或账户为空")
    elif user_info := query_user_by_username(usr):
        tb_name = user_info["username"]
        tb_pwd = user_info["password"]
        if tb_name == usr and tb_pwd == pwd:
            st.session_state.username = usr
            st.success("登录成功")
            time.sleep(1)
            st.switch_page("./pages/GPT.py")
        else:
            st.error("密码错误")

    else:
        st.error("账户不存在")
