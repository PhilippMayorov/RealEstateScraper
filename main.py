import streamlit as st 
from scrape import scrape_website, split_Dom_Content, clean_bdoy, extract_body
from parse import parse_with_ollama


st.title("Real-Estate Webscraper")
url = st.text_input("Enter the URL of the Real-Estate Website you want to scrape:")

if(st.button("Scrape site: ")):
    st.write(f"Scraping data from {url}")
    # scrape the website    
    result = scrape_website(url)
    # extract the body content from the website
    body_content = extract_body(result)
    # clean the body content
    cleaned_content = clean_bdoy(body_content)

    st.session_state.dom_content = cleaned_content

    # A button that will expand to show the cleaned content
    with st.expander("View DOM Content:"):
        st.text_area("DOM Content:", cleaned_content, height = 300)

    # print(result)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Enter a description of the Real-Estate information you want to extract:")

    if st.button("Parse content"):
        if parse_description:
            st.write(f"Parsing content with the following description: {parse_description}")
       
            # splits the content into chunks of 6000 characters
            dom_chunks = split_Dom_Content(st.session_state.dom_content)

            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)