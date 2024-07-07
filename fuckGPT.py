import time

import streamlit as st
import pymysql

st.title("FUCK GPT WELCOME YOU")
st.text("fucking mather")

def st_write(txt:str):
    #p = "response response333 response response response response response"
    for word in txt.split():
        yield word+" "
        time.sleep(0.1)


message = st.chat_input("please input your question mother fucker.")
if message:
    with st.chat_message("user"):
        st.write(message)
        #st.image("https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1pqWHc.img?w=768&h=873&m=6&x=1080&y=1080&s=147&d=147 ")

    with st.chat_message("assistant"):
        res = st_wokrite("I don't kown you say,please input your mather fucker question again.")
        #response = response()#st_write("response response response response response response")
        st.write_stream(res)

