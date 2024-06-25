import streamlit as st
import base64
import aiohttp
import asyncio
from streamlit_style import apply_styles

ICON_PATH = 'icon-assistant.png'
API_HOST = "184.105.238.239"
API_PORT = "7000"

# Convert the image to base64 format
with open(ICON_PATH, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Application title with icon
st.markdown(
    f"""
    <h1 style='display: flex; align-items: center;'>
        <img src='data:image/png;base64,{encoded_string}' style='margin-right: 10px;' width='150' height='150'/>
         Balthazar
    </h1>
    """,
    unsafe_allow_html=True
)

# Apply custom styles
apply_styles()


async def get_answer_from_api(query, threshold, num_results):
    url = f"http://{API_HOST}:{API_PORT}/getInfo"
    payload = {
        "query": query,
        "threshold": threshold,
        "num_results": num_results
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"API call failed with status code {response.status}")

# Section for questions
st.subheader("Salut, sunt Balthazar, asistentul tău AI.")
user_query = st.text_input("Descriere:", placeholder="O speță în care acuzatul...")

# # Sidebar for setting parameters
# with st.sidebar:
#     st.header("Setări")
#     threshold = st.slider("Acuratețe Căutare", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
#     num_results = st.slider("Număr de Rezultate", min_value=1, max_value=10, value=3, step=1)

if st.button("Caută", key="ask_question"):
    if user_query:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            # Show spinner while waiting for the response
            with st.spinner("Caut..."):
                response = loop.run_until_complete(get_answer_from_api(user_query, threshold=0.2, num_results=4))

            answer = response["text"]
            source_documents = response["source_documents"]

            # Use st.markdown to properly format the response containing markdown or HTML
            st.markdown(f"""
                <div style="border: 2px solid #4CAF50; padding: 10px; border-radius: 10px; margin-top: 20px; margin-bottom: 20px;">
                    <h3 style="color: #4CAF50;">Răspuns:</h3>
                    <div style="font-size: 18px;">{answer}</div>
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Eroare la generarea răspunsului: {str(e)}")
    else:
        st.warning("Scrie o descriere pentru căutare.")
