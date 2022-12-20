## Import block
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

import numpy as np
import pandas as pd

import math
from math import sqrt

from sklearn.metrics.pairwise import cosine_similarity

# function for calculating the weigted rating
def weighted_rating(data, m, C):
    wr = (data["members"]/(data["members"]+m))*data["rating"] + (m/(data["members"]+m))*C
    return wr

# recommendation function for content-based filtering
def recommend(anime, anime_index, anime_name, cos_sim):
    # get the index of the anime name
    ind = anime_index[anime_name]
    #print(ind)
    
    # calculate cosine similarity scores of all anime with that anime, enumerate it to match the index
    sim_scores = list(enumerate(cos_sim[ind]))
    #print(sim_scores)

    # sort the anime based on the similarity scores
    sim_scores = sorted(sim_scores, reverse=True, key=lambda x: x[1])
    #print(sim_scores)

    # get the scores of the 5 most similar anime
    sim_scores = sim_scores[0:6]
    #print(sim_scores)

    # get the anime indices
    anime_indices = []
    for i in sim_scores:
        anime_indices.append(i[0])
    #print(anime_indices)

    # return the top 5 most similar anime after the anime user types
    result = anime[["name", "genre", "weighted_rating", "episodes", "type"]].iloc[anime_indices]
    return result


# function for performing svd
def SVD(wide_data, binary_data):
    
    # 1. center the data by the average rating:
    # replace nan entries with the average rating of 5.0
    temp_wide_data = wide_data.fillna(5.0)
    x = np.tile(5.0, (temp_wide_data.shape[0],1))
    # get a centered utility matrix by subtracting 5.0 from all the elements
    utility_matrix = temp_wide_data - x

    # 2. compute singular value decomposition
    U,s,Vt = np.linalg.svd(utility_matrix, full_matrices=False)
    
    # 3. use svd to get a lower dimension approximation of data
    k=3
    low_d = np.dot(U[:,:k] * s[:k], Vt[:k,:])

    # 4. more refinement
    # restore original non-mean-centered numbers by adding 5
    low_d = low_d + 5
    # convert np to pd
    low_d = pd.DataFrame(low_d, index=wide_data.index, columns=wide_data.columns)
    # screen the dimension-reduced matrix with binary matrix
    # the rating for the anime that each user already rated will be 0
    low_final = low_d*binary_data
    
    return low_final


# recommender function for collaborative filtering
def recommend2(anime, rating_prediction, user_id):

    # get the rows for the selected users
    current_user = rating_prediction.loc[user_id]
    #print(current_user)
    
    # sort and take the index of three highest rating
    # note that argsort is in default ascending order, so we take the last three
    rec_ind = np.argsort(current_user)[-3:]
    # note that sort is in default ascending order, so we make it double negative to make it descending
    rec_max = -np.sort(-current_user)[0:3]
    # get the anime id for the three highest rating
    rec_anime_id = list(current_user.iloc[rec_ind].index)
    rec_anime_id.reverse()
    print(rec_anime_id)
    # show three anime
    recommendation = anime.loc[anime["anime_id"].isin(rec_anime_id)]
    for i in range(len(rec_anime_id)):
        print("{}. For anime: {} , the predicted rating from this user is: {:.2f}.".format(i+1,anime.loc[anime["anime_id"] == rec_anime_id[i]].name.iloc[0], rec_max[i]))
    
    return recommendation


# function that returns the user's ratings on the anime by descending order when we input the user_id
def user_rating(user_id):
    # drop non-rated elements
    user_rating_previous = wide_user_anime.loc[user_id]
    s = user_rating_previous.dropna()
    s = s.to_frame()
    #print(s.shape)
    
    # joint the table
    join = s.join(anime.set_index("anime_id"), on="anime_id")
    #print(join.shape)
    user_r = join.sort_values(by=[user_id], ascending = False)
    return user_r.head(15)
