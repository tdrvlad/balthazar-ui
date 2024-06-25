def apply_styles():
    import streamlit as st

    st.markdown(
        """
        <style>
        .css-1d391kg {padding-top: 4rem;}  /* Padding sus pentru a face loc header-ului */
        .css-1v3fvcr {padding-top: 2rem;}  /* Padding pentru secțiunea de întrebări */
        .stTextInput input {border: 2px solid #4CAF50;}  /* Bordura câmpului de text */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            transition-duration: 0.4s;
        }
        .stButton button:hover {
            background-color: white;
            color: black;
            border: 2px solid #4CAF50;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
