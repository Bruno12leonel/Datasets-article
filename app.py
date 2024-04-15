import streamlit as st
import page.credit_card_data  as credit_card_data
import page.new_page as new_page

PAGES = {
    "Credit Card Data": credit_card_data,
    "New Page": new_page
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
