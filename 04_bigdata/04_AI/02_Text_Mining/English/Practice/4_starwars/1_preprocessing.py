import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

protagonist_header = ' LUKE'
documents = []
labels = []

with open('sw_ep', 'r', encoding='utf-8') as file_handle:
    for line in file_handle:
        if line.startswith(protagonist_header):
            labels.append(1)
            documents.append(line[len(protagonist_header) + 1:])
        else:
            cnt = 0
            for line2 in line:
                cnt += 1
                if line2 == ',':
                    break
            labels.append(0)
            documents.append(line[cnt:])

# 텍스트 문장을 벡터로 구성(단어 추출)
vectorizer = CountVectorizer()
term_counts = vectorizer.fit_transform(documents)
vocabulary = vectorizer.get_feature_names()

tf_transformer = TfidfTransformer(use_idf=False).fit(term_counts)
features = tf_transformer.transform(term_counts)
with open('processed.pickle', 'wb') as file_handle:
    pickle.dump((vocabulary, features, labels), file_handle)
