import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def recommend_feed_based_previous_question(qna, mapping, similarity_matrix, question_input):
    question_index = mapping[question_input]

    # Get similarity values with other questions
    # Similarity_score is the list of index and similarity matrix

    similarity_score = list(enumerate(similarity_matrix[question_index]))

    # Sort in descending order the similarity score of question inputted with all the other questions
    
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    
    # Get the scores of the 6 most similar questions. Ignore the first question since it 'll be same as the one given as input.
    
    similarity_score = similarity_score[1:6]
    
    # Return question titles using the mapping series
    
    question_indices = [i[0] for i in similarity_score]
    
    return (qna['title'].iloc[question_indices])    

if __name__ == '__main__':
    qna = pd.read_csv('qna.csv')

    tfidfVector = TfidfVectorizer(stop_words='english')

    # If there are empty content fill it with ''
    qna['content'] = qna['content'].fillna('')

    content_matrix = tfidfVector.fit_transform(qna['content'])

    # print(content_matrix.shape)

    similarity_matrix = linear_kernel(content_matrix, content_matrix)

    # print(similarity_matrix)

    # QNA Index mapping

    mapping = pd.Series(qna.index, index= qna['title'])

    # print(mapping)

    question_input = input("Enter Your Question : ")

    matches = recommend_feed_based_previous_question(qna, mapping, similarity_matrix, question_input)

    for match in matches:
        print(match)