import streamlit as st
import spacy 
# Importing as module.
import en_pipeline

st.title("News Bias Words Recognizer")

with st.spinner():
    nlp = en_pipeline.load()

input = st.text_area(label = "Enter your text to get biased words")

doc = nlp(input)

for ent in doc.ents:
    st.write(ent.text)
