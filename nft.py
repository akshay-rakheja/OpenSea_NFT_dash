import streamlit as st
import requests

endpoint = st.sidebar.selectbox("Endpoints",["Assets", "Events", "Rarity", "Floor Price"])
st.header(f"Open Sea explorer - {endpoint}")
if endpoint == "Assets":
    params = {
    'collection':'stoner-cats-official',
    # 'limit': 1
    }
    r = requests.get('https://api.opensea.io/api/v1/assets', params=params)
    st.write(r.json())