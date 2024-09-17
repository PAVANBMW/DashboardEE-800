import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(page_title ="Superstore!!!", page_icon = ":bar_chart:", layout = "wide")


# Setting the tittle ......

st.title(" :bar_chart: I_Steps Dashboard")
# st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html = True)


# Browse and upload the data 

fl = st.file_uploader(":file_folder: Upload a file", type =(["csv", "txt","xlsx","xls"]))

if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_excel(filename)

else:
    os.chdir(r"C:\data")
    df = pd.read_excel("New_Data_frame.xlsx")


# create the date picker 

col1, col2 = st.columns((2))
df["Date"] = pd.to_datetime(df["sab"])

# Now pick the start and end date 

startDate = pd.to_datetime(df["Date"]).min()
endDate = pd.to_datetime(df["Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))


# Updating the data as per given date 

df = df[(df["Date"] >= date1) & (df["Date"] <= date2)].copy()


#category_df = df.groupby(by = ["typ"], as_index = False)["istufe"].count()
result_1 = df.groupby("typ").size().reset_index(name ="Istufe")
result_2 = df.groupby("I_stuf_catagory").size().reset_index(name ="R_Istufe")



with col1:
    st.subheader(" Category wise I_STEPS in the given time line")
    fig = px.bar(result_1, x = "typ", y = "Istufe",text = "Istufe",  template = "seaborn")
    st.plotly_chart(fig, use_container_width =True, height = 200)

with col2:
    st.subheader(" Modified_I_STEPS in the given time line")
    fig = px.bar(result_2, x = "I_stuf_catagory", y = "R_Istufe",text = "R_Istufe",  template = "seaborn")
    st.plotly_chart(fig, use_container_width =True, height = 200)


