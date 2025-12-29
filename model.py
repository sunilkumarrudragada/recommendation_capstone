import os
import pickle
import pandas as pd
import hashlib
import sklearn


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'sentiment_model.pkl'), 'rb') as f:
    sentiment_model = pickle.load(f)


with open(os.path.join(BASE_DIR, 'tfidf_vectorizer.pkl'), 'rb') as f:
    tfidf_vectorizer = pickle.load(f)


with open(os.path.join(BASE_DIR, 'user_item_pivot.pkl'), 'rb') as f:
    df_pivot = pickle.load(f)

with open(os.path.join(BASE_DIR, 'item_similarity.pkl'), 'rb') as f:
    item_similarity_df = pickle.load(f)

with open(os.path.join(BASE_DIR, 'reviews_df.pkl'), 'rb') as f:
    reviews_df = pickle.load(f)


def item_based_recommendations(username, n_recommendations=20):
    if username not in df_pivot.index:
        return []

    user_ratings = df_pivot.loc[username].dropna()
    if user_ratings.empty:
        return []

    scores = item_similarity_df[user_ratings.index].dot(user_ratings)
    scores = scores.drop(user_ratings.index, errors='ignore')
    scores = scores[scores > 0]

    return scores.sort_values(ascending=False).head(n_recommendations).index.tolist()


def get_top_5_recommendations(username):
    top_20_products = item_based_recommendations(username, 20)
    if not top_20_products:
        return []

    filtered_reviews = reviews_df[
        reviews_df['name'].isin(top_20_products)
    ].copy()

    if filtered_reviews.empty:
        return []

    review_tfidf = tfidf_vectorizer.transform(filtered_reviews['clean_review'])
    filtered_reviews['predicted_sentiment'] = sentiment_model.predict(review_tfidf)

    sentiment_summary = (
        filtered_reviews
        .groupby('name')['predicted_sentiment']
        .value_counts(normalize=True)
        .rename('percentage')
        .reset_index()
    )

    positive_sentiment = sentiment_summary[
        sentiment_summary['predicted_sentiment'] == 'positive'
    ]

    if positive_sentiment.empty:
        return []

    return (
        positive_sentiment
        .sort_values(by='percentage', ascending=False)
        .head(5)['name']
        .tolist()
    )
