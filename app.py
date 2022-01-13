import streamlit as st # web app
import spacy # named entity recognition 

# title 

st.title("News Bias Words Recognizer")

# wait until the model loads with a simple spinner - progress bar

with st.spinner("Please wait while the model is being loaded...."):
    nlp = spacy.load("en_pipeline")

# text box to get user input 

input = st.text_area(label = "Enter your text to get biased words recognized.....")

# create a doc object with named entities 

doc = nlp(input)

# get the html / markdown code for displaying the output 

output_html = spacy.displacy.render(doc, style='ent', jupyter=False, options = {"colors": {'bias':'#ff5a36'} })

# render the html code as a markdown with html rendering enabled 

st.markdown(output_html,    unsafe_allow_html=True)
