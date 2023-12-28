import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def recommendations(title):
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    cv = TfidfVectorizer()
    tfidf_matrix = cv.fit_transform(movies['genres'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    genres = []
    indices = pd.Series(movies.index, index=movies['title'])
    titles = movies['title']
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]
def rating():
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    df = pd.merge(ratings, movies, how='left', on='movieId')
    df1 = df.groupby(['title'])[['rating']].sum()
    high_rated = df1.nlargest(20, 'rating')
    return  (high_rated.to_string())

