import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

positive = '1\t'  # 상품에 대해 추천하면 1
negative = '0\t'  # 추천하지 않으면 0
document = []
labels = []

with open('movie_review.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.startswith(positive):
            labels.append(1)
            document.append(line[len(positive):])
        elif line.startswith(negative):
            labels.append(0)
            document.append(line[len(negative):])

count_vector = CountVectorizer()  # 단어 횟수 피처를 만드는 클래스
words_counts = count_vector.fit_transform(document)  # 리뷰에서 단어 횟수 세기
voca = count_vector.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# 단어 빈도(term frequency)가 생성

tf_transformer = TfidfTransformer(use_idf=False).fit(words_counts)
features = tf_transformer.transform(words_counts)

# 처리된 파일을 저장
with open('pre_movie_review.pickle', 'wb') as file_handle:
    pickle.dump((voca, features, labels), file_handle)
