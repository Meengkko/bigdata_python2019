from gensim.models import word2vec

# model = word2vec.Word2Vec.load("hong.model")
model = word2vec.Word2Vec.load("park.model")
# model = word2vec.Word2Vec.load("moon.model")

print('\nStep2] 단어 빈도가 높은 어휘를 대상으로 유의어 분석')
similar_words = model.most_similar(positive=["북한"])
for word_set in similar_words:
    print(f'{word_set[0]:<10}: {word_set[1]}')
print(model.most_similar(positive=["북한"]))
# most_similar: 키워드와 유사한 또는 같이 많이 언급된 단어
