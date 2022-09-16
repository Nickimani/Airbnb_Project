# importing libriraries
import pandas as pd
import numpy as np
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
user_input = st.text_input('What are some features you are interested in? eg ocean overview, free parking, pool, longterm stay', '')
# number_of_guests = st.number_input('How many guests are to be expected:', min_value= 1, max_value= 16, step= 1)


# Defining user input
st.sidebar.header('User Preferences')
st.sidebar.markdown('Tailor your preferences')
# Defining features
cities = st.sidebar.selectbox('City', ('Stellenbosch', 'Retreat', 'Sunset Beach', 'Noorder-Paarl',
                                       'Kraaifontein', 'Rosebank', 'Cape Town', 'Constantia', 'Grabouw',
                                       'Bergvliet', 'Claremont', 'Rondebosch', 'Lansdowne', 'Newlands', 'Atlantis'))

# define a function for the different cities
def city_prices(df, city):
    '''This function takes in city and assigns appropriate price points'''
    # subset df
    df = df[df['cities'] == city]
    # assigning limits to use on slider
    min_price = int(df['price'].min())
    max_price = int(df['price'].max())
    median_price = int(df['price'].median())
    
    return min_price, max_price, median_price

# using the function
prices = city_prices(listings_df_copy, cities)

price_range = st.sidebar.slider('Price', prices[0], prices[1], prices[2])
guests = st.sidebar.slider('Number of guests', 1, 16, 7)

# subsetting main dataframe
updated_df = listings_df_copy[
    (listings_df_copy['price'] <= price_range) & 
    (listings_df_copy['cities'] == cities) & 
    (listings_df_copy['accommodates'] <= guests)
]
updated_df.reset_index(inplace= True)

# instantiate the vectorizer
tfidf_rec = TfidfVectorizer(ngram_range=(1, 3), lowercase = False)

st.markdown('These are the top listings you may like: ')
# introducing a cache
@st.cache

# recommender function
def final_recommender(question, df):
    ''' This function asks the user a question and then takes in the answer to finds the top 5 similar listings '''
    
    # tfidf_rec = TfidfVectorizer(ngram_range=(1, 3), lowercase = False)
    tfidf_matrix = tfidf_rec.fit_transform(df['contents'])
    
    # count vectorize the question/User input
    inquiry = tfidf_rec.transform(np.array([question]))

    # Calculate cosine similarity of inquiry with the cv_matrix
    similarity = linear_kernel(inquiry, tfidf_matrix)
    
    # Obtain the index then sort, picking top 5
    nums = np.argsort(similarity[0])
    
    # Reorder the reference dataframe
    df = df.loc[nums]
    
    # Pick out the top 5
    #return the top 5
    top_5 = df[['name', 'listing_url', 'price', 'cities']].tail(5)
    return top_5



st.dataframe(final_recommender(user_input, updated_df))

# map
mapping = updated_df[['latitude', 'longitude']]
st.map(mapping)

# Goodluck message
st.markdown('**_Welcome to the Rainbow Nation_!!!** Enjoy your stay.')
image2 = Image.open('SA_flag.jpg')
st.image(image2)
