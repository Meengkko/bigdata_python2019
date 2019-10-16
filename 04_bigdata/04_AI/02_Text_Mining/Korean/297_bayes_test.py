# 과제 수행 목표: 한글 text를 대상으로 한 텍스트마이닝 적용
# 테이터 출처: Sample 데이터 (프로그램 내 가상으로 생성)
# 텍스트 데이터: 메일 제목
# 예측 항목: Spam 여부 진단
# 어휘 분류 기준: 카테고리 별 단어 출현 횟수 (어미, 조사, 마침표 제거)
# 판정 기준: 나이브 베이즈 분류(Naive Bayes classifier) 알고리즘

from bayes import BaysianFilter
import operator
bf = BaysianFilter()

bf.fit("파격 세일 - 오늘까지만 30% 할인", "광고")
bf.fit("쿠폰 선물 & 무료 배송", "광고")
bf.fit("현대계 백화점 세일", "광고")
bf.fit("봄과 함께 찾아온 따뜻한 신제품 소식", "광고")
bf.fit("인기 제품 기간 한정 세일", "광고")
bf.fit("오늘 일정 확인", "중요")
bf.fit("프로젝트 진행 상황 보고", "중요")
bf.fit("계약 잘 부탁드립니다", "중요")
bf.fit("회의 일정이 등록되었습니다", "중요")
bf.fit("오늘 일정이 없습니다", "중요")
# 예측

pre, scorelist = bf.predict("재고 정리 할인, 무료 배송")

print('\n<분석결과>')
print(f'* 카테고리별 평가 점수: {scorelist}')
print("* 판정 결과 =", pre)

effective_words = sorted(bf.word_dict[pre].items(), key=operator.itemgetter(1), reverse=True)
print('* 판정에 영향을 미친 어휘')
for word_set in effective_words:
    print(f'{word_set[0]:<10}: {word_set[1]}회')
