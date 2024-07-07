import time

import streamlit as st
import pymysql

from dao.UserDao import query_userchat_by_username, add_userchat
from util.style_util import main_bg

main_bg("pages/img_4.png")

username = st.session_state.username
uid = st.session_state.uid
st.title("GPT ASSISTANT FOR AI")
st.text(f"AI assistant welcome {username}!")

def st_write(txt:str):
    #p = "response response333 response response response response response"
    for word in txt.split():
        yield word+" "
        time.sleep(0.1)





message = st.chat_input("please input your question mother fucker.")
if message:
    add_userchat(uid,"user",message)
    message = (message.replace("?","!")
                      .replace("？","")
                      .replace("吗","")
                      .replace("呢","")
                      .replace("你","我"))
    add_userchat(uid, "assistant", message)

    if False:
        with st.chat_message("user"):
            st.write(message)

        with st.chat_message("assistant"):
            res = st_write("I don't kown you say,please input your mather fucker question again.")
            #response = response()#st_write("response response response response response response")
            st.write_stream(res)




chats = query_userchat_by_username(username)
if len(chats) != 0:
    for chat in chats:
        with st.chat_message(chat["role"]):
            st.write(chat["message"])
else:
    st.write("我是你的智能助手，你有什么问题？")

