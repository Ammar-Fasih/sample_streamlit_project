import streamlit as st

st.write('# Home Page 🌎')
st.link_button('Dashboard','/dashboard')

# streamlit run streamlit_exp/learn_01/home.py \
#   --browser.serverAddress=localhost \
#   --server.enableCORS=false \
#   --server.enableXsrfProtection=false \
# --server.port 8080