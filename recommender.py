#!/usr/bin/python3
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# read the data
df = pd.read_csv('genres_v2.csv', low_memory=False)

# remove duplicates
df = df.drop_duplicates(subset="song_name")

# drop null values
# df = df.dropna(axis=0)

# drop non-required columns
df = df[['duration_ms', 'genre', 'song_name']]

# combine all columns and assign as new column
df["data"] = df.apply(lambda value: " ".join(value.astype("str")), axis=1)

# print(df)

#  initialize CountVectorizer
vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df['data'])
similarities = cosine_similarity(vectorized)

# assign the new DataFrame with 'similarities' values
df_tmp = pd.DataFrame(
    similarities, columns=df['song_name'], index=df['song_name']).reset_index()

while True:
    print("Recommend a song based on liked songs")
    while True:
        input_song = input("Name of Song: ")

        if input_song in df_tmp.columns:
            recommendation = df_tmp.nlargest(11, input_song)["song_name"]
            break
        else:
            print("Sorry, song not in database")
    print("You should check out these songs: \n")
    for song in recommendation.values[1:]:
        print(song)

    print("\n")
    while True:
        next_cmd = input("Listen to next song? [yes, no]")

        if next_cmd == 'yes':
            break
        elif next_cmd == 'no':
            break
        else:
            print("Please type 'yes' or 'no'")
