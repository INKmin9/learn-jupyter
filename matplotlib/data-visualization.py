# 소원이는 운영 중인 인터넷 쇼핑몰에서 어떤 상품들이 잘 팔리는지 확인해 보려고 합니다.
# 각 품목별 판매수량을 한눈에 볼 수 있도록 아래와 같은 막대 그래프를 그려 주세요.
import numpy as np
import matplotlib.pyplot as plt

sales_array = np.array([10, 13, 8, 15, 6, 11, 4])
category_array = ['skirt', 't-shirt', 'dress', 'sweater', 'coat', 'jeans', 'shoes']

# 여기에 코드를 작성하세요.
plt.bar(category_array, sales_array)
plt.show()