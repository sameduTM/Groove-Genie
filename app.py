#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)

# read the data
df = pd.read_csv('genres_v2.csv', low_memory=False)

# remove duplicates
df = df.drop_duplicates(subset="song_name")

# drop null values
# df = df.dropna(axis=0)

# drop non-required columns
df = df[['duration_ms', 'genre', 'song_name', 'song_id']]
df["data"] = df.apply(lambda value: " ".join(value.astype("str")), axis=1)

# Initialize vectorizer = CountVectorizer()
vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df['data'])
similarities = cosine_similarity(vectorized)

# Create DataFrame with similarities values
similarities_df = pd.DataFrame(
    similarities, columns=df['song_name'], index=df['song_name']).reset_index()

# to store likes
likes_dislikes = {'likes': set(), 'dislikes': set()}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    return render_template('recommend.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        query = request.form.get('query', '').lower()
        if not query:
            return render_template('search_results.html', query=query,
                                   results=None, error="Please enter a\
                                   song name")
        results = df[df.apply(
            lambda row: query in str(row['song_name']).lower(), axis=1)]
        return render_template('search_results.html', query=query,
                               results=results, likes_dislikes=likes_dislikes,
                               error=None)
    return render_template('search_results.html', query='', results=None,
                           likes_dislikes=likes_dislikes,
                           error=None)


@app.route('/song/<string:song_id>')
def song_detail(song_id):
    try:
        song = df[df['song_id'] == song_id].iloc[0]
        is_liked = song_id in likes_dislikes['likes']
        is_disliked = song_id in likes_dislikes['dislikes']
    except (IndexError, ValueError):
        return "Song not found!", 404
    return render_template('song_detail.html', song=song, is_liked=is_liked,
                           is_disliked=is_disliked)


@app.route('/like/<string:song_id>')
def like_song(song_id):
    likes_dislikes['likes'].add(song_id)
    return redirect(url_for('song_detail', song_id=song_id))


@app.route('/dislikes/<string:song_id>')
def dislike_song(song_id):
    likes_dislikes['dislikes'].add(song_id)
    return redirect(url_for('song_detail', song_id=song_id))


@app.route('/liked_songs')
def liked_songs():
    liked_songs_df = df[df['song_id'].isin(likes_dislikes['likes'])]
    return render_template('liked_songs.html', liked_songs=liked_songs_df)


@app.route('/recommendations')
def recommendations():
    if not likes_dislikes['likes']:
        return render_template('recommendations.html', recommended_songs=None,
                               error="No liked songs")
    liked_songs_df = df[df['song_id'].isin(likes_dislikes['likes'])]
    recommended_songs_df = get_recommendations(liked_songs_df)

    return render_template('recommendations.html',
                           recommended_songs=recommended_songs_df)


def get_recommendations(liked_songs_df):
    # generate recommendations based oon liked songs(
    liked_songs = liked_songs_df['song_name'].tolist()
    recommendations = set()

    for song in liked_songs:
        if song in similarities_df.columns:
            recommended_songs = similarities_df.nlargest(11, song)['song_name']
            recommendations.update(recommended_songs)

    # remove liked songs from recommendations
    recommendations.difference_update(liked_songs)

    # get recommended songs details
    recommended_songs_df = df[df['song_name'].isin(recommendations)]
    return recommended_songs_df


if __name__ == "__main__":
    app.run(debug=True)
