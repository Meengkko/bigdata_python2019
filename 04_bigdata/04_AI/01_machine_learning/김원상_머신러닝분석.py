'''
데이터 셋 :
Statistics for a large number of US Colleges from the 1995 issue of US News and World Report.
(1995년 미국 기사와 월드 리포트에 따른 미국 대학에 관한 통계자료)

출처 :
R패키지의 ISLR
(College.csv는 https://www.kaggle.com/flyingwombat/us-news-and-world-reports-college-data/download
링크를 따라 다운가능하다)

각 변수 설명 :
Private => (범주형) 사립학교 또는 국립(주립)
Apps => 입학신청 수
Accept => 합격인원 수
Enroll => 등록인원 수
Top10perc => 고등학교에서 상위 10%이내 학생수 비율
Top25perc => 고등학교에서 상위 25%이내 학생수 비율
F.Undergrad => Fulltime 학부생 수
P.Undergrad => Parttime 학부생 수
Outstate => 타주 출신 학생 학비
Room.Board => 기숙사비 & 식비
Books => 책값 추정치
Personal => 사비로 지출
PhD => 일반 박사학위를 받은 교수 비율
Terminal => 전문 박사학위를 받은 교수 비율
S.F.Ratio => 학생 대비 교수 수
perc.alumni => 졸업생 기부자 비율
Expend => 학생당 수업료
Grad.Rate => 졸업률
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

College_data = pd.read_csv('./College.csv', header=0, index_col=0)

# 사립학교 유무는 카테고리로 바꾸어 숫자형으로 처리한다
College_data['Private'] = College_data['Private'].astype('category')
College_data['Private_cat'] = College_data['Private'].cat.codes

private_cat = College_data['Private_cat']
College_data.drop(['Private', 'Private_cat'], axis=1, inplace=True)

# 컬럼과 인덱스 명 저장
all_variables = list(College_data.columns)
numeric_variables = list(College_data.columns)[:-2]
all_index = list(College_data.index)

# 박스 플롯을 그려본 결과 꼬리가 긴(치우쳐있는) 데이터 명을 추출할 수 있다.
sns.boxplot(x="variable", y="value", data=pd.melt(College_data[numeric_variables]))
plt.show()

# 표본이 비교적 적고 각 대학마다 조사를 통해 얻은 데이터라는 점을 미루어
# 아웃라이어라고 판정될 만한 데이터도 삭제하지 않고 치우쳐진 데이터를 로그처리한다.
skewed_data = ['Apps', 'Accept', 'Enroll', 'F.Undergrad', 'P.Undergrad', 'Expend']
College_data[skewed_data] = np.log(College_data[skewed_data])

# 다시 데이터를 표준화 한다 (관측치 - 평균)/표본편차
scaler = StandardScaler()
College_data = scaler.fit_transform(College_data)
College_data = pd.DataFrame(College_data)
College_data.columns = all_variables

# 박스플롯을 통해 표준화된 데이터의 분포를 확인해 볼 수 있다.
sns.boxplot(x="variable", y="value", data=pd.melt(College_data))
plt.show()

# 변수의 개수를 축약하여 설명을 단순화하기위해 주성분 분석을 활용한다.
# 주성분 분석의 결과로 2차원으로 축약된 변수는 전체 데이터의 분산을 설명한다.
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(College_data)
principalDataframe = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])

# 주성분 분석의 결과
# 주성분에 따르는 고유벡터에서 각 변수에 해당하는 가중치를 보고 분석한다.
# 첫번째 주성분(principle1) : 낮은 접근성(학비 등), 교육품질이 높음
# 두번째 주성분(principle2) : 높은 접근성, 교육적 성과는 개인적 역량에 의존
variables = pd.DataFrame(pca.components_.T)
variables.index = list(College_data.columns)
variables.columns = ['principle_1', 'principle_2']
variables.to_csv('eigenvalue_PCA.csv', encoding='utf-8')

# Scree Plot의 결과에 따르면 두 개의 주성분이 전체 분산의 60% 이상(각각 30%)을 설명하는 것으로 나온다.
percent_variance = np.round(pca.explained_variance_ratio_ * 100, decimals=2)
columns = ['PC1', 'PC2']
plt.bar(x=range(1, 3), height=percent_variance, tick_label=columns)
plt.ylabel('Percentate of Variance Explained')
plt.xlabel('Principal Component')
plt.title('PCA Scree Plot')
plt.show()

diminished_df = principalDataframe
diminished_df.index = all_index
diminished_df.columns = ['principle_1', 'principle_2']

# 실루엣 분석에 의해 K평균 방식으로 군집을 3개로 나누는 것이 가장 좋을 것으로 판단한다.
# 실루엣 점수 : 클러스터 3개일때 0.43
for n_clusters in range(2, 10):
    clusterer = KMeans(n_clusters=n_clusters)
    preds = clusterer.fit_predict(diminished_df)
    centers = clusterer.cluster_centers_

    score = silhouette_score(diminished_df, preds, metric='euclidean')
    print("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))

# k평균 군집분석을 활용하여 전체 대학을 3가지 카테고리로 분류하고 분류한 결과를 데이터 프레임에 저장한다.
# 저장된 데이터 셋을 확인하여 분석한 결과 (뚜렷한 특성 없음, 높은 접근성과 방임형, 낮은 접근성과 고급형)으로 나누었다.
kmeans = KMeans(n_clusters=3, algorithm='auto')
kmeans.fit(diminished_df)
predict = pd.DataFrame(kmeans.predict(diminished_df))
predict.index = diminished_df.index
predict.columns = ['predict']
result = pd.concat([diminished_df, predict], axis=1)

# 사립대학 여부를 데이터프레임에 저장한다.
result = pd.concat([result, private_cat], axis=1)

# 군집분석 결과 산점도 시각화
plt.scatter(result['principle_1'], result['principle_2'], c=result['predict'], alpha=0.5)
plt.show()

# 사립대학 유무 산점도 시각화
plt.scatter(result['principle_1'], result['principle_2'], c=result['Private_cat'], alpha=0.5)
plt.show()

# 군집과 사립대 유무에 관한 범주를 활용하여 교차표를 작성한다.
data_crosstab = pd.crosstab(result['predict'], result['Private_cat'], margins=False)
print(data_crosstab)

# 두 가지 범주를 합쳐 시각화를 하기위해 새로운 변수(vis_category)를 만들어 시각화한다.
result['vis_category'] = (result['predict'] * 2 + 1) + result['Private_cat']
plt.scatter(result['principle_1'], result['principle_2'], c=result['vis_category'], alpha=0.5)
plt.show()

# 결과를 엑셀파일로 저장한다.
result.to_excel("clustered_college.xlsx", encoding='utf-8')

# 이하 비지도학습 분석 서술
'''
1. 뚜렷한 특성이나 강점이 없는 대학교 중에는 사립학교 비중이 높다.
2. 접근성이 낮으나 높은 수준의 교육기회를 주는 대학교 중에는 사립학교 비중이 높다.
    - 아이비리그 대학, 시카고 대학, 펜실베이니아 대학, MIT 등 흔히 명문 사립대로 알려진
    대학은 대부분 이 범주에 속한다.
3. 높은 접근성이 있지만 교육성과가 개인적 역량에 따르는 대학은 국공립,주립대학 비중이 높다.
    - 아이오와 주립대, 캘리포니아 대학, 택사스 대학 등 한국에서도 유명한 국공립, 주립 대학이
    이 범주에 속한다.
4. 클러스터링 범주와 사립유무 범주가 앞서 서술한 경향을 따르지 않는 대학도 있다.
    - 높은 접근성을 제공하며 사립대학인 경우
        델라웨어 대학, 마셜 대학, 세인트 루이스 대학 등 33개 대학
    - 교육수준이 비교적 높다고 판단되는 국공립, 주립대학
        버지니아 대학, 매리랜드 대학, 웨스트몬트 대학 등 7개 대학
'''
