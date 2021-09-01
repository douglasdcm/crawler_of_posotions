import math
from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer
from src.helper.helper import remove_special_characters


class Similarity:

    def __init__(self):
        self.bow = CountVectorizer()

    def return_similarity_by_cossine(self, cv, positions):
        """
        Return a dictionary of message and similarity sorted by highter similarity
        """

        similarity = []

        for m in positions:
            m = str(m)
            new_msg_list = [remove_special_characters(cv), m]
            vector_bow = self.bow.fit_transform(new_msg_list)
            msg_bow = vector_bow.todense()[0]
            m_bow = vector_bow.todense()[1]

            d1_array = (1, 1)

            if m_bow.shape == d1_array and msg_bow.shape == d1_array:
                d = 1 - distance.euclidean(msg_bow, m_bow)
            else:
                d = 1 - distance.cosine(msg_bow, m_bow)

            if math.isnan(float(d)):
                similarity.append(0.0)
            else:
                similarity.append(d)
        result = dict(zip(positions, similarity))

        return {str(round(v * 100, 2)): k for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}