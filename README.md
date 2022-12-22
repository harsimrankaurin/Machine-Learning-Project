## Customer Segmentation using Clustering to Scale Collaborative Filtering and Sentiment Classification to Recommend Niche Restaurants

Recommendation systems experience the curse of scalability. This project addresses the gap by using *K-Means* for clustering customers based on their food preferences that are uniquely gathered from their reviews.
The proposed recommender is based on *collaborative filtering* functioning on the respective previously assigned user clusters through K-Means. A sentiment classifier for reviews is developed to aid recommendations for niche restaurants using classification models. *Dimension reduction* was introduced through PCA and T-SVD to increase efficiency where T-SVD provided better variation ratio and runtimes.  

# Motivation
Recommendation systems also experience the ‘Matthew Effect’ where the popular restaurants become more popular while the less visited restaurants become more unpopular. Also most recommenders usually only focus on ratings and not the sentiment of reviews. This project addresses this gap by recommending niche or lesser reviewed restaurants with the help of the sentiment of reviews for them.

# About the Dataset
This project makes use of Yelp reviews of size 4 GB mainly for recommending restaurants to the user. The Yelp dataset present in Kaggle is a subset of Yelp business uploaded for analyzing the reviews and performing analysis. As a part of this research, restaurants that are highly rated but less visited by people are termed as ‘niche restaurants’. The project will analyze the reviews posted by the people, perform exploratory data analysis, data preprocessing , and prepare data for models which will help classify reviews as positive or negative. 

# Results
Based on the performance metrics SVC was observed to outperform other models with an accuracy of 84% after hypertuning.

# Deployment
The results of the collaborative filtering recommendation and recommendation using the deployed sentiment analyzer were integrated using an UI developed with Tkinter.
A sample of the UI is given below

![image](https://user-images.githubusercontent.com/38915458/209062554-2ec4f8d2-fc63-462e-9ad7-cbfbf153f32c.png)

![image](https://user-images.githubusercontent.com/38915458/209062569-6bae6840-013e-40f2-8dd3-1398c30ed203.png)

