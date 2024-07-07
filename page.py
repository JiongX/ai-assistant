#1、引入streamlit
import streamlit as st
#2、streamlit开发的每一个网页一般建议都要有一个标题
st.header("我的第一个python网页")
#3、输入框
username = st.text_input("请输入你的用户名")
if username:
    st.write(username)

password = st.text_input("请输入你的密码",type='password')
if password:
    st.write(password)

flag = st.button("按钮")
if flag:
    st.write("按钮被点击了")

# 图片
st.image("logo.jpg",width=100)
# 音乐
st.audio("https://audio04.dmhmusic.com/71_53_T10064835782_128_4_1_0_sdk-cpm/cn/0513/M00/F2/34/ChAKFGZxeO6ALR8ZADO4_cdud4I886.mp3?xcode=cf9751adbd1d1a5be1e99fb3deb77d8c306fd8d")
# 视频
# st.video("")
# 表格
dict = {
    "name":["zs","ls","ww"],
    "age":[1,2,3]
}
st.table(dict)

st.text("文本")
code = '''
    <html></html>
'''
st.code(code,language='html')

d ={
    "数值":[10,9,8,7,6,5]
}
st.bar_chart(d)