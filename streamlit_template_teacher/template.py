# Code based on streamlit app.py example (provided by teachers of the course)

# Import all required packages
import streamlit as st
from random import random

# set/change show session state
def select_movie(id):  
  st.session_state['id'] = id

# Set a recommendation tile with a button (popcorn icon) to select
# that show, its image, and its title
def tile_item(column, item):
  with column:
    st.button('🍿', key=random(), on_click=select_movie, args=(item['id'], ))
    st.image(item['image_url'], use_column_width='always')
    st.caption(item['title'])

def get_n_recommendations(diversity_value, n_recommendations):
# Determine the number of most similar shows to display from the respective diversity list, 
# based on the set diversity value ('High', 'Medium', or 'Low'), with a minimum of 1 show and 
# as maximum the half of the number of recommendations n_recommendations to show. 
# If more than half n_recommendations would be returned, then n_recommendations could be exceeded when
# also a 'High' value for the other kind of diversity is set (could alternatively be compensated for with normalization).
# Make sure to check that n_recommendations is a positive value (as no negative number of recommendations can be shown)
  if diversity_value == 'High':
    n_diversity = n_recommendations//2 if n_recommendations > 0 else 0 # double // returns an integer as result
  elif diversity_value == 'Medium':
    n_diversity = n_recommendations//4 if n_recommendations > 0 else 0
  elif diversity_value == 'Low':
    n_diversity = 1 if n_recommendations>0 else 0

  return n_diversity

# Create a horizontal grid in which the selected number of recommendations is displayed 
def recommendations(df):

  # Check the number of items to display
  nbr_items = df.shape[0]

  if nbr_items != 0:    

    # Create columns with the corresponding number of items
    columns = st.columns(nbr_items)

    # Convert df rows to dict lists
    items = df.to_dict(orient='records')

    # Apply tile_item to each column-item tuple (created with python 'zip')
    any(tile_item(x[0], x[1]) for x in zip(columns, items))