from os import write
from requests.models import Response
import streamlit as st
import requests

endpoint = st.sidebar.selectbox("Endpoints",["Assets", "Events", "Rarity", "Floor Price"])

st.header(f"Open Sea explorer - {endpoint}")
st.sidebar.subheader("Filters")

collections = st.sidebar.text_input("Collection")
owner_address = st.sidebar.text_input("Owner Address")
project_address =  st.sidebar.text_input("Project Address")
token_id = st.sidebar.text_input("Token ID(s)")


my_address= '0x90f14e3282977416286085e0d90210A400bEFD22'
stoner_cats = '0xd4d871419714b778ebec2e22c7c53572b573706e'

# st.sidebar.subheader()

if endpoint == "Assets":

    params_assets ={} #params for asset retreival
    params_orders ={} # params for order retrieval

    #add parameters for a valid input. Need to add the validation part
    if collections:
        params_assets['collection'] = collections
    if owner_address:
        params_assets['owner'] = owner_address
    if project_address:
        params_orders['asset_contract_address'] = project_address
    if token_id:
        params_orders['token_id'] = token_id
    

    r = requests.get('https://api.opensea.io/api/v1/assets', params = params_assets)
    o = requests.get('https://api.opensea.io/wyvern/v1/orders', params= params_orders)
    response_assets = r.json()
    response_orders = o.json()

    if len(params_orders)==0:
        for asset in response_assets['assets']:
            if asset['name']:
                st.write(asset['name'])
            else:
                st.write(f"{asset['collection']['name']} # {asset['token_id']}")
            if asset['image_url'].endswith('mp4'):
                st.video(asset['image_url'])
            else:
                st.image(asset['image_url'])
    else:
        # created_date = []
        # for order in response_orders['orders']:
        #     created_date.append(response_orders['orders']['created_date'])

        st.write(response_orders)
        for order in response_orders['orders']:
            if order['asset']['name']:
                st.write(order['asset']['name'])
            else:
                st.write(f"{order['asset']['name']} # {order['asset']['token_id']}")
           
            #checking for current price            
            if order['current_price']:
                current_price = float(order['current_price'])/(10**18)
                st.write(current_price)
            else:
                st.write("No current Price")

            if order['asset']['image_url'].endswith('mp4'):
                st.video(order['asset']['image_url'])
            else:
                st.image(order['asset']['image_url'])


    st.write(r.json())