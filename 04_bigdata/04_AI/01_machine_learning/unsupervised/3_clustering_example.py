# K-중심 군집화 (K-centroid clustering, K-medoid clustering)
import time
from scipy import stats
from collections import Counter
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_score

user_product_dic = {}
product_user_dic = {}
product_id_name_dic = {}


def analyze_clusters_keywords(labels, product_id_name_dic, user_product_dic, id_user_dic):
    print(Counter(labels))
    cluster_item = {}

    for i in range(len(labels)):
        cluster_item.setdefault(labels[i], [])
        for x in user_product_dic[id_user_dic[i]]:
            cluster_item[labels[i]].extend([product_id_name_dic[x]])

    for cluster_id, product_name in cluster_item.items():
        product_name_keyword = " ".join(product_name).split()
        print("cluster_id:", cluster_id)
        print(Counter(product_name_keyword).most_common(20))


def analyze_clusters_keywords_bigram(labels, product_id_name_dic, user_product_dic, id_user_dic):
    print(Counter(labels))
    cluster_item = {}

    for i in range(len(labels)):
        cluster_item.setdefault(labels[i], [])
        for x in user_product_dic[id_user_dic[i]]:
            cluster_item[labels[i]].extend([product_id_name_dic[x]])

    for cluster_id, product_name in cluster_item.items():
        bigram = []
        product_name_keyword = " ".join(product_name).replace(' OF ', ' ').split()
        for i in range(0, len(product_name_keyword) - 1):
            bigram.append(' '.join(product_name_keyword[i: i + 2]))
        print('cluster_id:', cluster_id)
        print(Counter(bigram).most_common(20))


def analyze_clusters_product_count(labels, user_product_dic, id_user_dic):
    product_len_dic = {}
    for i in range(0, len(labels)):
        product_len_dic.setdefault(labels[i], [])
        product_len_dic[labels[i]].append(len(user_product_dic[id_user_dic[i]]))
    for k, v in product_len_dic.items():
        print('cluster:', k)
        print(stats.describe(v))


for line in open('online_retail_utf.txt'):
    line_items = line.strip().split('\t')
    user_code = line_items[6]
    product_id = line_items[1]
    product_name = line_items[2]

    if len(user_code) == 0:
        continue

    country = line_items[7]
    if country != 'United Kingdom':
        continue

    try:
        invoice_year = time.strptime(line_items[4], '%m/%d/%y %H:%M').tm_year
    except ValueError:
        continue

    if invoice_year != 2011:
        continue

    user_product_dic.setdefault(user_code, set())
    user_product_dic[user_code].add(product_id)
    product_user_dic.setdefault(product_id, set())
    product_user_dic[product_id].add(user_code)
    product_id_name_dic[product_id] = product_name

product_per_user_li = [len(x) for x in user_product_dic.values()]

print("Step1] 빅데이터 로딩 완료")
print('# of users:', len(user_product_dic))
print('# of products:', len(product_user_dic))
print(stats.describe(product_per_user_li))

min_product_user_li = [k for k, v in user_product_dic.items() if len(v)==1]
max_product_user_li = [k for k, v in user_product_dic.items() if len(v)>=600]
print("# of users purchased one product: %d" % len(min_product_user_li))
print("# of users purchased more than 600 product: %d" % len(max_product_user_li))
user_product_dic = {k: v for k, v in user_product_dic.items() if len(v) in range(1, 600)}
print("# of left user: %d" % len(user_product_dic))

id_product_dic = {}
for product_set_li in user_product_dic.values():
    for x in product_set_li:
        if x in id_product_dic:
            product_id = id_product_dic[x]
        else:
            id_product_dic.setdefault(x, len(id_product_dic))
print("# of left items: %d" % len(id_product_dic))

id_user_dic = {}

user_product_vec_li = []

all_product_count = len(id_product_dic)

for user_code, product_per_user_set in user_product_dic.items():
    user_product_vec = [0] * all_product_count
    id_user_dic[len(id_user_dic)] = user_code
    for product_name in product_per_user_set:
        user_product_vec[id_product_dic[product_name]] = 1

    user_product_vec_li.append(user_product_vec)

print("\n Strp2] K-평균 군집화 기법을 적용하여 실루엣 계수 구하기")
test_data = np.array(user_product_vec_li)

for k in range(2, 9):
    km = KMeans(n_clusters=k).fit(test_data)
    print("score for %d clusters: %.3f" % (k, silhouette_score(test_data, km.labels_)))

print("\n Step3] 상품 키워드 구하기")
km = KMeans(n_clusters=2, n_init=10)
km.fit(test_data)
analyze_clusters_keywords(km.labels_, product_id_name_dic, user_product_dic, id_user_dic)

print("\n Step4] 의미있는 키워드로 변환하기")
km = KMeans(n_clusters=2, n_init=10)
km.fit(user_product_vec_li)
analyze_clusters_keywords_bigram(km.labels_, product_id_name_dic, user_product_dic, id_user_dic)

print("\n Step5] 기초통계량 추가 확인")
analyze_clusters_product_count(km.labels_, user_product_dic, id_user_dic)

print("\n Step6] 분석결과에 대하여 해석하고 발표하기")
