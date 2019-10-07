import urllib.request as req
local = "mushroom.csv"
# 데이터 소개
# https://archive.ics.uci.edu/ml/datasets/Mushroom
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, local)
print("ok")
