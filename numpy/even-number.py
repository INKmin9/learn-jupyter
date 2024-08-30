# 1부터 100까지 숫자가 들어 있는 numbers_array에서 짝수에 해당하는 숫자들만 뽑아 보세요!

import numpy as np

numbers_array = np.arange(1, 101)

# 여기에 코드를 작성하세요.
numbers_array[(numbers_array % 2 == 0)]