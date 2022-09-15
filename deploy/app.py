# importing libriraries
import pandas as pd
import numpy as np
np.random.BitGenerator = np.random.bit_generator.BitGenerator
import streamlit as st
from PIL import Image
import sklearn
import pickle

#sklearn
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

# Writing header of the application
st.title('Dhahabu Airbnb Recommender')
st.write("""
Airbnb was born in 2007 when two Hosts welcomed three guests to their San Francisco home, and has since grown to over 4 million Hosts who have welcomed more than 1 billion guest arrivals in almost every country across the globe. Every day, Hosts offer unique stays and experiences that make it possible for guests to connect with communities in a more authentic way.
""")

image1 = Image.open('Tswalu_Tarkuni.jpg')
st.image(image1, width=650)

# load pickle files
# listings cleaned
listings_df = pd.read_pickle('listings_cleaned_df.pkl')

# listings cleaned copy
listings_df_copy = pd.read_pickle('listings_cleaned_copy.pkl')

# vectorizer
# tfidf_rec = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Obtain input from the user
st.write('Below type in preferences for your ideal listing. **_GO WILD!!!_**')
user_preference = st.text_input('What are some features you are interested in? eg ocean overview, free parking, cape town', '')
number_of_guests = st.number_input('How many guests are to be expected:', min_value= 1, max_value= 16, step= 1)

# instantiate the vectorizer
tfidf_rec = TfidfVectorizer(ngram_range=(1, 3), lowercase = False)

st.markdown('These are the top listings you may like: ')
# introducing a cache
@st.cache

# recommender function
def final_recommender(question, df= listings_df):
    ''' This function asks the user a question and then takes in the answer to finds the top 5 similar listings '''
    

    # tfidf_rec = TfidfVectorizer(ngram_range=(1, 3), lowercase = False)
    tfidf_matrix = tfidf_rec.fit_transform(listings_df_copy['contents'])
    
    # count vectorize the question/User input
    inquiry = tfidf_rec.transform(np.array([question]))

    # Calculate cosine similarity of inquiry with the cv_matrix
    similarity = linear_kernel(inquiry, tfidf_matrix)
    
    # Obtain the index then sort, picking top 5
    nums = np.argsort(similarity[0])
    
    # Reorder the reference dataframe
    df = df.loc[nums]
    # Apply the subset condition
    df = df[df['accommodates'] == number_of_guests]
    # Pick out the top 5
    #return the top 5
    top_5 = df[['name', 'listing_url']].tail(5)
    return top_5



st.dataframe(final_recommender(user_preference))

# Goodluck message
st.markdown('**_Welcome to the Rainbow Nation_!!!** Enjoy your stay.')
image2 = Image.open('SA_flag.jpg')
st.image(image2)
