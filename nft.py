from requests.models import Response
import streamlit as st
import requests

endpoint = st.sidebar.selectbox("Endpoints",["Assets", "Events", "Rarity", "Floor Price"])

st.header(f"Open Sea explorer - {endpoint}")
st.sidebar.subheader("Filters")

collections = st.sidebar.text_input("Collection")
owner_address = st.sidebar.text_input("Owner Address")

my_address= '0x90f14e3282977416286085e0d90210A400bEFD22'

# st.sidebar.subheader()

if endpoint == "Assets":

    params ={}

    if collections:
        params['collection'] = collections
    if owner_address:
        params['owner'] = owner_address

    # params = {
    # 'collection':collections,
    # 'owner': owner_address
    # # 'limit': 1
    # }

    r = requests.get('https://api.opensea.io/api/v1/assets', params=params)
    response = r.json()

    for asset in response['assets']:
        if asset['name']:
            st.write(asset['name'])
        else:
            st.write(f"{asset['collection']['name']} # {asset['token_id']}")
        if asset['image_url'].endswith('mp4'):
            st.video(asset['image_url'])
        else:
            st.image(asset['image_url'])


    st.write(r.json())