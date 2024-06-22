

import os
import streamlit as st
import pickle
import time
from langchain.llms import google_palm
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.prompts import PromptTemplate

from langchain.chains import RetrievalQA

import os
import streamlit as st
from langchain.llms import google_palm

import streamlit as st
from streamlit_option_menu import option_menu
import os
from langchain.llms import GooglePalm 

# Set up Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCeTe213mlNQVOe4iWq09OIrNjlO6F5n48"
api_key = os.environ.get("GOOGLE_API_KEY")
llm = GooglePalm(google_api_key=api_key, temperature=0.9)

# Set up the styling for the app
st.markdown(
    '''
    <style>
    .title {
        font-size: 48px;
        color: #8A2BE2;
    }
    .sidebar-title {
        font-size: 20px;
        color: black;
    }
    .content {
        font-size: 14px;
    }
    .main {
        
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Page title
st.markdown('<h1 class="title">Welcome You Movie Buddy..!</h1>', unsafe_allow_html=True)

# Center content div
st.markdown('<div class="center-content">', unsafe_allow_html=True)

# Input for user's question
selected_movie = st.text_input('What is your question?')
if st.button('Search'):
    with st.spinner('Loading your result...'):
        result = llm(selected_movie)
        st.write(f'ANSWER: {result}')

# Sidebar with URL inputs
with st.sidebar:
    st.markdown('<h2 class="sidebar-title">URLS</h2>', unsafe_allow_html=True)
    st.markdown('<div class="content">From any websites you can fetch data</div>', unsafe_allow_html=True)
    url1 = st.text_input('URL 1', 'Enter your url')
    url2 = st.text_input('URL 2', 'Enter your url')
    url3 = st.text_input('URL 3', 'Enter your url')
    
    if st.button('Fetch URL'):
        with st.spinner('Fetching URL from server...'):
            # Function to fetch and display content from a URL
  
            
            # Display fetched data from URLs
            if url1 != 'Enter your url':
                st.write(f'Data from {url1}: {(url1)}')
            if url2 != 'Enter your url':
                st.write(f'Data from {url2}: {(url2)}')
            if url3 != 'Enter your url':
                st.write(f'Data from {url3}: {(url3)}')

