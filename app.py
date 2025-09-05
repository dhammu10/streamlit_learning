import streamlit as st
# from PIL import Image

st.title("Streamlit Learning")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Wield Fox")

    st.markdown(
        """
        <style>
        .custom-img img {
            height: 300px !important;
            width:200px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="custom-img"><img src="https://images.unsplash.com/photo-1474511320723-9a56873867b5?w=600"></div>',
        unsafe_allow_html=True
    )

    st.write("This is a fox image take from unplash")



with col2:
    st.header("wild panchhi")

    st.markdown("""
                
            <style>
                .costom-img img{
                    height: 300px !important;
                    width: 200px !important;
                }
            </style>
                
                """,
               unsafe_allow_html=True 
            )
    

    st.markdown("""
            <div class = "costom-img"><img src="https://images.unsplash.com/photo-1497206365907-f5e630693df0?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8YW5pbWFsfGVufDB8fDB8fHww"> </div>
                
            """,
                unsafe_allow_html=True
                )
    st.write("We get wiled pancchi from unplash")


with col3:
    st.header("wild panchhi")

    st.markdown("""
                
            <style>
                .costom-img img{
                    height: 300px !important;
                    width: 200px !important;
                }
            </style>
                
                """,
               unsafe_allow_html=True 
            )
    

    st.markdown("""
            <div class = "costom-img"><img src="https://images.unsplash.com/photo-1497206365907-f5e630693df0?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8YW5pbWFsfGVufDB8fDB8fHww"> </div>
                
            """,
                unsafe_allow_html=True
                )
    st.write("We get wiled pancchi from unplash")



first_name = st.sidebar.text_input("Enter your first name")
last_name = st.sidebar.text_input("Enter your last name")
gender = st.sidebar.selectbox("Choose your gender", ["Gender", "Male", "Female", "Other"])


with st.expander("check Addmission Process"):
    st.write(""" 
             1. apply collages that you want <br>
             2. then check a allotment collage <br>
             3. then verify your document<br>
             4. verify your all document<br>
             5. Paid collage fees
             6. attend a letures """,
             
             unsafe_allow_html=True)



st.markdown("### Welcome chai app")
st.markdown(">are you tied")


 