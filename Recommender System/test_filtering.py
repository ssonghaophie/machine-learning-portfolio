import pytest
import pandas as pd
import numpy as np
import project1
from sklearn.metrics.pairwise import cosine_similarity

# preprocessing the data
anime = pd.read_csv("anime.csv", sep = ",")
rating = pd.read_csv("rating.csv", sep = ",")
anime = anime.dropna()
index = anime["episodes"] == "Unknown"
anime = anime[-index]
# change the type of rating and members to a numeric value
anime["rating"] = anime["rating"].astype(float)
anime["members"] = anime["members"].astype(float)
anime["episodes"] = anime["episodes"].astype(float)

# preprocessed anime
anime = anime.reset_index(drop=True)
anime_concat = pd.concat([anime, anime["genre"].str.get_dummies(sep=','), 
                     anime["type"].str.get_dummies()], axis=1)
anime_features = anime_concat.iloc[:, 4:].copy()

cos_sim = cosine_similarity(anime_features.values, anime_features.values)
anime_index = pd.Series(anime.index, index=anime.name)

anime_merged = anime.merge(rating,on="anime_id",suffixes= ["", "_user"]).dropna(axis=0)
wide_user_anime = anime_merged.pivot_table(index="user_id", columns="anime_id", values="rating_user")

# wide data for svd
new_wide = wide_user_anime.iloc[0:10,0:10]

# binary wide for svd
binary_matrix = new_wide.copy()
nan_inds = new_wide.isna()
rating_inds = new_wide.notna()
nan_inds = nan_inds.to_numpy()
rating_inds = rating_inds.to_numpy()
binary_matrix[nan_inds] = 1
binary_matrix[rating_inds] = 0


# shape check for weighted_rating
def test_weighted_rating_shape():
    weighted = project1.weighted_rating(anime, 10000, anime.rating.mean())
    expected = (11830,)
    return weighted.shape == expected

# type check for weighted_rating
def test_weighted_rating_type():
    weighted = project1.weighted_rating(anime, 10000, anime.rating.mean())
    assert isinstance(weighted, pd.core.series.Series)


# shape check for weighted_rating
def test_recommend_shape():
    anime["weighted_rating"] = anime.apply(project1.weighted_rating, axis=1, args=(10000,anime.rating.mean()))
    anime.drop(["rating", "members"], axis=1, inplace=True)
    result = project1.recommend(anime, anime_index,"Kimi no Na wa.", cos_sim)
    expected = (6, 5)
    return result.shape == expected

# type check for recommendation function for content-based filtering
def test_recommend_type():
#     anime["weighted_rating"] = anime.apply(project1.weighted_rating, axis=1, args=(10000,anime.rating.mean()))
#     anime.drop(["rating", "members"], axis=1, inplace=True)
    result = project1.recommend(anime, anime_index,"Kimi no Na wa.", cos_sim)
    assert isinstance(result, pd.core.frame.DataFrame)
    
# shape check for svd
def test_SVD_shape():
    data = project1.SVD(new_wide, binary_matrix)
    expected = (10,10)
    return data.shape == expected  

# type check for svd
def test_SVD_type():
    data = project1.SVD(new_wide, binary_matrix)
    assert isinstance(data, pd.core.frame.DataFrame)

data = project1.SVD(new_wide, binary_matrix)
    
def test_recommend2_already_rated():
    yes_already_rated = False;
    # get the recommendation
    recom = project1.recommend2(anime, data, 5)
    # get the row for user_id = 5
    y = data[data.index == 5]
    
    # mark yes_alread_rated as True if the predicted rating is 0 (means that the user already rated that anime)
    for i in y[recom["anime_id"]]:
        if i == 0:
            yes_already_rated = True;

    expected = False;
    assert yes_already_rated == expected
    
