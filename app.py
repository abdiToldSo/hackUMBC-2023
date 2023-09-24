import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

st.title("Netflix Watchparty Selector")
image_url = 'https://rustedrailgolf.com/wp-content/uploads/2020/09/Watch-Party-Rectangle-1210x423.png'

st.image(image_url, use_column_width=True, output_format='JPEG', width=25)

df = pd.read_csv('/content/netflix_titles.csv')
movie_list = df["title"].values.tolist()
#Number of Users
users = int(
  st.selectbox('How many people are watching?', ('1', '2', '3', '4', '5')))
#class movie:

#ABDI'S CODEBLOCK
#Dummy Code
#test = [
  #"Good People",
  #"Stonehearst Asylum",
  #"Love",
  #"ATM",
  #"Def Comedy Jam 25"
#]

test = [
  "Norm of the North: King Sized Adventure",
  "Spider-Man: Into the Spider-Verse",
  "The End of Evangelion",
  "EVANGELION: DEATH (TRUE)²"
]

x = "Good People"
#Initialize Empty List & Dataframe
testdf = pd.DataFrame()
testH = []
common_genre = []
#Append empty testdf with inputted values
for i in test:
  testdf = testdf.append(df.query('title == @i'))

#Converts dataframe to list with
testG = testdf["title"].values.tolist()

#Convert 2D list into 1D List
for i in range(len(testG)):
  testH.append(testG[i].split(", "))
final_genres = [i for sublist in testH for i in sublist]

#Finds 5 Most Common Genres
for i in range(5):
  if len(final_genres) > 0:
    x = max(final_genres, key=final_genres.count)
    common_genre.append(x)
    final_genres.remove(x)


#Parse df movies with final_genres list
genre_df = pd.DataFrame()

for i in final_genres:
  #df = df.query('"@i" is in listed_in')
  print('hello')

genre_df.append(df.query("listed_in == @final_genres"))

#Minimum: randommized 5 results
#Goal: add score rating to dataframe, then
#First Step: Find overlap with other dataframe

#df2.head()

#test_df = pd.DataFrame()
#for i in df2:
    #test_df.append(df2.query("title == "))
df = df.sample(frac = 1)
#df1 = pd.DataFrame()
#df1['TEST'] = np.where(df['title'] == df1['TITLE'],'True','False')
genre_df.head()
df.head()


#Parse df movies with final_genres list
genre_df = pd.DataFrame()

for i in final_genres:
  #df = df.query('"@i" is in listed_in')
  print('hello')

genre_df.append(df.query("listed_in == @final_genres"))

#Minimum: randommized 5 results
#Goal: add score rating to dataframe, then
#First Step: Find overlap with other dataframe

#df2.head()

#test_df = pd.DataFrame()
#for i in df2:
    #test_df.append(df2.query("title == "))
genre_df = df.sample(frac = 1)
#df1 = pd.DataFrame()
#df1['TEST'] = np.where(df['title'] == df1['TITLE'],'True','False')

df = genre_df.head()


def combine():
  global finalList
  finalList = user1 + user2 + user3 + user4 + user5
  st.write(finalList)

def output_movies():
  global movie1
  global movie2
  global movie3
  global movie4
  global movie5
  movie1 = movie2 = movie3 = movie4 = movie5 = {}

  movie1 = {
    'title': df.iloc[0].values[2],
    'audience': df.iloc[0].values[8],
    'genre': df.iloc[0].values[10],
    'description': df.iloc[0].values[11]
  }

  movie2 = {
    'title': df.iloc[1].values[2],
    'audience': df.iloc[1].values[8],
    'genre': df.iloc[1].values[10],
    'description': df.iloc[1].values[11]
  }

  movie3 = {
    'title': df.iloc[2].values[2],
    'audience': df.iloc[2].values[8],
    'genre': df.iloc[2].values[10],
    'description': df.iloc[2].values[11]
  }

  movie4 = {
    'title': df.iloc[3].values[2],
    'audience': df.iloc[3].values[8],
    'genre': df.iloc[3].values[10],
    'description': df.iloc[3].values[11]
  }

  movie5 = {
    'title': df.iloc[4].values[2],
    'audience': df.iloc[4].values[8],
    'genre': df.iloc[4].values[10],
    'description': df.iloc[4].values[11]
  }


  #TITLE
  #df.iloc[1].values[2]

  #AUDIENCE
  #df.iloc[1].values[8]

  #GENRE
  #df.iloc[1].values[10]

  #DESCRIPTION
  #df.iloc[1].values[11]

movie4

def Generate():
  combine()
  output_movies()



if users >= 1:
  user1 = st.multiselect('Person 1 What movies? (Max. 5)',
                         movie_list,
                         max_selections=5)
if users >= 2:
  user2 = st.multiselect('Person 2 What movies? (Max. 5)',
                         movie_list,
                         max_selections=5)
if users >= 3:
  user3 = st.multiselect('Person 3 What movies? (Max. 5)',
                         movie_list,
                         max_selections=5)
if users >= 4:
  user4 = st.multiselect('Person 4 What movies? (Max. 5)',
                         movie_list,
                         max_selections=5)
if users >= 5:
  user5 = st.multiselect('Person 5 What movies? (Max. 5)',
                         movie_list,
                         max_selections=5)

st.button("Generate", help="Generate Movie Output", on_click=Generate())