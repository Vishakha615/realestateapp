import streamlit as st
import numpy as np
import pandas as pd
import pickle


# Page config must be first
st.set_page_config(
    page_title="Real Estate Price Estimation",
    page_icon="🏠",
    layout="wide"
)


# ================= CSS DESIGN =================

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg,#FFF8E7,#E8F5E9);
}

/* Main container */
.block-container {
    padding: 40px;
}


/* Title */
.title {
    font-size: 60px;
    font-weight: 900;
    text-align:center;
    color:#14532d;
    margin-bottom:20px;
}


/* Banner */
.banner {
    background-image:url("https://tse4.mm.bing.net/th/id/OIP.e8XJSVxjIzAu2ne52552_wHaEJ?w=1000&h=560&rs=1&pid=ImgDetMain&o=7&rm=3");
    background-size:cover;
    background-position:center;
    height:600px;
    border-radius:25px;
    box-shadow:0px 15px 35px rgba(0,0,0,.25);
    margin-bottom:35px;
}


/* Heading */
h2 {
    color:#1B5E20 !important;
    font-size:40px !important;
    text-align:center;
}


/* Labels */

div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label          
 {
    
    font-size:22px !important;
    font-weight:bold;
    color:#1B5E20;
    outline: none !important;
}

div[data-testid="stNumberInput"] > div {
    
    
    min-height: 56px !important;
}           


/* Selectbox */

div[data-baseweb="select"] > div {

    font-size:22px !important;
    border-radius:15px !important;
    border:2px solid #43A047 !important;
    min-height:55px;

}


/* Dropdown items */

div[data-baseweb="popover"] li {

    font-size:20px !important;

}


/* Number input */

.stNumberInput input {

    font-size:22px !important;
    border-radius:15px;
    border:2px solid #43A047;

}


/* Button */

.stButton button {

    width:300px !important;
    background:#2E7D32;
    color:white;
    font-size:40px;
    font-weight:bold;
    border-radius:15px;
    padding:15px;
    height: 70px;

}




.stButton button:hover {

    background:#1B5E20;
    transform:scale(1.03);

}



/* Result */

.result {

    background:#E8F5E9;
    border-radius:20px;
    padding:25px;
    margin-top:30px;
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#1B5E20;
    border-left:10px solid #2E7D32;

}

div.stButton {
    display: flex;
    justify-content: center;
}

div.stButton > button {
    width: 350px !important;
    height: 65px !important;
    border-radius: 15px !important;
    font-size: 40px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

 div.stButton > button p {
        font-size: 20px !important;
        font-weight: bold;
        color: white;
    }
</style>
""", unsafe_allow_html=True)



# ================= HEADER =================


st.markdown("""
<div class="title">
🏠 Real Estate Price Estimation
</div>

<div class="banner"></div>

""", unsafe_allow_html=True)

st.header("Property Details")



# ================= LOAD MODEL =================


pipe = pickle.load(open("pipe11.pkl","rb"))

df = pd.read_csv("Cleaned_data.csv")



# ================= DATA =================


areatype = sorted(df["area_type"].unique())


availability1 = sorted(df["availability"].unique())

location1 = sorted(df["location"].unique())

society1 = sorted(df["society"].unique())


size1 = range(1,8)

bath1 = range(1,8)

balcony1 = range(0,8)



# ================= INPUTS =================


col1,col2 = st.columns(2,vertical_alignment="top")



with col1:

    area1 = st.selectbox(
        "Select Area Type",
        areatype
    )


    avail = st.selectbox(
        "Select Availability",
        availability1
    )


    loc = st.selectbox(
        "Select Location",
        location1
    )


    siz = st.selectbox(
        "Select BHK Size",
        size1
    )



with col2:


    soci = st.selectbox(
        "Select Society",
        society1
    )




    bath2 = st.selectbox(
        "Select Bathrooms",
        bath1
    )


    balcony2 = st.selectbox(
        "Select Balcony",
        balcony1
    )

    total = st.number_input("Enter total sqft", value=2500, min_value=1000, max_value=5000, step=100)




# ================= PREDICTION =================

left, center, right = st.columns([3, 4, 1])

with center:
    if st.button("₹ Predict Price"):
        user_input = [[
        area1,
        avail,
        loc,
        siz,
        soci,
        total,
        bath2,
        balcony2
        ]]


columns = [

        'area_type',
        'availability',
        'location',
        'size',
        'society',
        'total_sqft',
        'bath',
        'balcony'

    ]


user_input = pd.DataFrame(
        user_input,
        columns=columns
    )


result = pipe.predict(user_input)



st.markdown(
    f"""
    <div class="result" style="font-size: 22px; font-weight: bold; border: 10px; border: 2px solid #4CAF50;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);">

    🏡 Estimated Property Price


    ₹ {result[0,0]:,.0f} Lakhs

    </div>

    """,
    unsafe_allow_html=True
    )