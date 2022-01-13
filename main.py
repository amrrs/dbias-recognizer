import streamlit as st
import spacy 
from spacy_streamlit import visualize_parser

st.title("News Bias Words Recognizer")

# Importing as module.
import en_pipeline
nlp = en_pipeline.load()

input = st.text_area(label = "Enter your text to get biased words")

doc = nlp(input)

visualize_parser(doc)





# doc = nlp(input)

# for ent in doc.ents:
#     st.write(ent.text)
