import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG_350 jpeg",width=200)

st.title("33x , tapi , ini abadi")
st.header("aplikasi mengecek nilai ganjil/genap")
angka = st.number_input("tulis sebuah angka :",value=0,step=1
                        
if (angka % 2) == 0:
st.write(f"{angka}adalah bilangan genap")
st.write(f"{angka}adalah bilangan ganjil")
                        
