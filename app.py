import streamlit as st
import page.credit_card_data  as credit_card_data
import page.reaction_network as reaction_network
import page.gtconedset as gtconedset

PAGES = {
    "Credit Card Data": credit_card_data,
    "KEGG Metabolic Reaction Network (Undirected)": reaction_network,
    "Gas Turbine CO and NOx Emission Data Set": gtconedset
}


def main():
    st.sidebar.title('Menu')
    selection = st.sidebar.radio("Choose the dataset", list(PAGES.keys()))
    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        page.main()  

    # Add enough space to push the text to the bottom
    st.sidebar.markdown("<br>"*25, unsafe_allow_html=True)

    # Add your text
    st.sidebar.markdown('Made by: **Bruno Leonel**')


if __name__ == '__main__': 
    main()
