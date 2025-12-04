import streamlit as st

st.title("form data diri")
st.write("silahkan isi data diri anda")
st.write("made by royyan")

with st.form("form_data_diri"):
    nama = st.text_input("nama")
    alamat = st.text_input("alamat")
    usia = st.text_input("usia")
    submit = st.form_submit_button("submit")

if submit :
    st.success(f"terima kasih {nama} telah mengisi form data diri")
    st.write(f"nama : {nama}")
    st.write(f"alamat : {alamat}")
    st.write(f"usia : {usia}")