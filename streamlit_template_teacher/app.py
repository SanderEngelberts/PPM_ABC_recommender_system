# Bones of code inspired by streamlit app.py example (provided by teachers of the course),
# but a lot of code has been adjusted and added, as well as the code documentation

# Import all required packages and template.py with code functions
import streamlit as st
import os
import pandas as pd
from random import shuffle
import template as t

# Set page layout to wide, and change icon and name of application in the webbrowser tabs
st.set_page_config(layout='wide', page_title='ABC iview recommendations', page_icon='https://static.wikia.nocookie.net/logopedia/images/f/f8/IView_2011-icon.svg')
# Changing theme to dark or light mode (now default is system settings) can be done using streamlits own settings in the menue bar on the right

# Set show with id=10 as selected show if no other one is selected already 
# (id=0 is a bit bloody image to start with, and other movies starting with numbers often also display more violence)
if 'id' not in st.session_state:
  st.session_state['id'] = 10 

# Set paths to files with information about shows and the recommendations for each show
data_path = os.path.join(os.getcwd(), 'data', 'clustered_shows.csv') 
close_shows_folder = os.path.join(os.getcwd(), 'recommendations')

# Load the data and recommendation files from disk
df_shows = pd.read_csv(data_path, sep=',')
df_closest_within_cluster = pd.read_csv(os.path.join(close_shows_folder, 'closest_within_cluster.csv'), sep=',') # For personalised content
df_closest_outside_cluster = pd.read_csv(os.path.join(close_shows_folder, 'closest_outside_cluster.csv'), sep=',') # For content diversity
df_closest_representation = pd.read_csv(os.path.join(close_shows_folder, 'closest_representation.csv'), sep=',') # For representation diversity

# Retrieve information about the currently selected show
df_show = df_shows[df_shows['id'] == st.session_state['id']].iloc[0] 

# Add ABC iview logo (its logos are from https://logos.fandom.com/wiki/ABC_iview) and title of application at top of page
logo, page_header = st.columns([2,10]) 
with logo:
  # Add these manual adjustments such that the logo visually aligns with page header 
  # (streamlit doesn't offer the functionality yet to vertically align within columns)
  st.write("")   
  st.write("")
  st.image('https://static.wikia.nocookie.net/logopedia/images/7/74/Iview-2018.svg', width=125)
with page_header:
  st.title('ABC iview shows recommender system')

# Create two columns to display the information of the currently selected show
col1, col2 = st.columns(2)

# Display image of the currently selected show on the left of page
poster = df_show['image_url']
with col1: 
  st.image(poster)

# Display title, description, and genre label(s) of currently selected show on the right of page
with col2:
  st.header(df_show['title'])
  st.markdown(df_show['description']) # Puts show description over multiple lines instead of using a horizontal scroll bar like st.text()
  st.caption(df_show['genre'])

# Add sidebar where user can have some autonomy settings for which recommendations are shown
# One option for content- and one for representation diversity
# Index=1 sets Medium as the default option, sidebar puts it in left sidebar, else just in text
st.sidebar.header('Recommendation settings')
content_diversity = st.sidebar.selectbox(
     'How content diverse do you want your recommendations to be?',
     ('High', 'Medium', 'Low'), index=1, help='help') 
# TODO: add useful help information where a definition is given for this type of diversity

representation_diversity = st.sidebar.selectbox(
     'How diverse in representation of minority and oppressed groups do you want your recommendations to be?',
     ('High', 'Medium', 'Low'), index=1, help='help')
# TODO: add useful help information where a definition is given for this type of diversity

# Be transparant about what the recommendations are based on: the currently selected show, and the content- and representation
# diversity settings
st.subheader('Recommendations based on ' + df_show['title'] + ', and ' + content_diversity.lower() + ' content diversity plus ' + representation_diversity.lower() + ' representation diversity')

# Determine number of shows to select from each dataframe (depending on how much each public value is valued)
n_recommendations = 10 
n_content_diversity = t.get_n_recommendations(diversity_value=content_diversity, n_recommendations=n_recommendations)
n_representation_diversity = t.get_n_recommendations(diversity_value=representation_diversity, n_recommendations=n_recommendations)
n_personalisation = n_recommendations - n_content_diversity - n_representation_diversity

# Retrieve list with the ids of shows that are recommended for the selected show based on the public value balance
personalisation_ids = list(df_closest_within_cluster[df_closest_within_cluster.id_a == df_show['id']].head(n_personalisation)['id_b']) 
content_diversity_ids = list(df_closest_outside_cluster[df_closest_outside_cluster.id_a == df_show['id']].head(n_content_diversity)['id_b']) 
recommendation_ids = personalisation_ids + content_diversity_ids # Merge the lists with recommended show ids from same and different K-means clusters

# Add n_representation_diversity ids of similar representation diverse shows to the recommendation_ids list
# Do this one by one because such an id may already be included in recommendation_ids, which would otherwise result in duplicates
# There are currently 10 closest representation diverse shows included in the dataframe for each show, so with the maximum of 5 (n_recommendations//2) 
# of such shows to include for a `High' representation diversity setting, it is unlikely that not enough unique ids are contained in this dataframe 
# that were not already selected for personalisation or content diversity purposes. However, if it occurs, then less shows than n_recommendations 
# will be displayed
representation_diversity_ids = list(df_closest_representation[df_closest_representation.id_a == df_show['id']]['id_b'])
n_included = 0
for id_b in representation_diversity_ids:
  if id_b not in recommendation_ids:
    recommendation_ids.append(id_b)
    n_included += 1

  # Early stopping condition for if enough unique ids are added
  if(n_included >= n_representation_diversity):
    break

# Randomize the recommendation id order of displaying recommendations (performs this operation in place)
shuffle(recommendation_ids) 

# Retrieve information about the recommended shows and display this top 10 recommendations
df_recommendations = df_shows[df_shows['id'].isin(recommendation_ids)]
t.recommendations(df_recommendations)