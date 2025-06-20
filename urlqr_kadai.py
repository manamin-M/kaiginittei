import streamlit as st

st.title("会議日程調査")
st.write("会議を行います。協力お願いします。")

with st.form(key = "nameinput"):
    name = st.text_input("名前：")
    keishiki = st. radio("選んで" ,["対面", "オンライン"])
    date = []
    for i in range(1,13):
        for v in range(1, 32):
            date.append(f"{i}月{v}日")
    multiselect = st.multiselect("希望日程を選択", options = date)
    button = st.form_submit_button("送信")

if button:
    st.write("名前：", name, "希望形式：", keishiki,"希望日程：", multiselect)
