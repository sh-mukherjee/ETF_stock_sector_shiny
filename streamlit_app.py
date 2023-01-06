import streamlit as st
import pandas as pd
import plotly.express as px

st.title("APAC MSCI Index Sectors")
st.subheader('Sector breakdown of the holdings of the MSCI index ETFs EWH, EWJ, EWY, EWS, EWT')
st.write('Source: Yahoo! Finance as of end December 2022')

df = pd.read_csv('APAC_sector_weight.csv')

country_list = df['Country'].unique().tolist()
countries = st.multiselect('Select one or more countries',country_list,default=['Hong Kong','Singapore'])

fig = px.bar(df[df['Country'].isin(countries)], x="Weight(%)", y="Sector_Name",
             color="Country", hover_data=['Country','Sector_Name','Weight(%)'],
             color_discrete_map={
                "Japan": "red",
                "Taiwan": "#00CC96",
                "Korea": "blue",
                "Hong Kong": "#FBE426",
                "Singapore": "magenta"},
             template="ggplot2",   
             barmode = 'group',
             height = 800)


st.plotly_chart(fig)
