# Recommendation System

## Introduction

My goal for this project is to build and compare two different recommendation system that recommends the anime based on how much the anime is similar to the other anime, and how much the users rated each anime. The former is done by content-based filtering, and the latter is done by collaborative-filtering.

## Approaches

For content-based filtering, I used the cosine similarity metric to calculate how similar each anime was to one another. Since the metric requires two vectors to be the set of numbers, I had to change all the categorical variables including genre and type into numeric representations by using the binary labeling of 0 and 1. This allowed me to apply cosine similarity, which yields 1 when the two vectors compared are identical to each other and -1 when they are the complete opposite of each other. After calculating it, I built an algorithm that takes and returns 5 anime that have the highest cosine similarity values when compared to the anime that the user searches.

For collaborative filtering, I preprocessed the data to be a user by anime matrix, so that it contains the information on the ratings of different users on different anime. Since none of the users watched all the anime, there were a lot of missing fields, which I had to store the information of so that I don’t end up recommending the anime that the user already rated and thus watched.

Then, I had to decide on which dimension reduction method I will use from PCA and SVD. Because my data was very large, I had some problems regarding the computation speed when running the dimension reduction algorithm. It was also very sparse with a lot of missing values. Therefore, I went with truncated SVD which works better on sparse data and can reduce the running time significantly. SVD also doesn’t require the data to be normalized, making it more accessible. After performing SVD, I built an algorithm that takes the id of the user and returns 3 anime that have the highest predicted rating.  

## Conclusion

According to the recommendation results, it looked like the recommendation from the content-based filtering model is a lot more explicitly similar in the genre, the number of episodes, and the types of anime that are recommended. It is almost the same as going through the list of anime and searching for the anime with all the tags matching with the one we are comparing to because the recommendations were very straightforward with almost all of the tags being identical. 

However, the recommendations using collaborative filtering were less straightforward, having some anime different genres from the ones that the user rated the highest (rate of 10). This is because all of the rates are considered, so although one genre can be rated high, the anime with the same genre could also be rated low by the user depending on the quality of the anime and other aspects. The recommendations are still very reasonable because although there is more diversity, the key genres from the high-rated anime from the user were still considered. This algorithm might be better because it is more realistic. In the real life, not a lot of anime watchers would like to watch hundreds of anime of a fixed genre, type, and number of episodes. It makes more sense that the user will explore different anime with diverse genres, and like one anime and doesn’t like another from the same genre depending on other aspects of them. Therefore, I like the idea of introducing more diversity using collaborative filtering.

However, because there are not many variables stored in this data, the relationship or similarity of collaborative filtering can also be seen quite explicitly just by looking at the columns of the data. Later, I wish I can explore a more complex dataset with more information including the overview, production company, author, voice actors, etc so that the recommendation can be less obvious in our eyes. I also want to explore other recommendation algorithms that have more strength in the real life, possibly using deep learning.

