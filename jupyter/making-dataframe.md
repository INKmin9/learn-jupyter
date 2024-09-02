이번 레슨에서는 DataFrame을 만드는 다양한 방법에 대해 알아보도록 하겠습니다. 일단 아래와 같이 NumPy와 pandas 라이브러리를 불러올게요.
```python
import pandas as pd
import numpy as np
```
그리고 지난 시간에 배운 것처럼 `pd.DataFrame()` 안에 DataFrame으로 만들 재료를 넣어 주면 되는데요. 이때, 아래와 같이 딕셔너리를 넣기도 하지만, 리스트나 NumPy array를 넣을 수도 있습니다.
```python
dict_df = pd.DataFrame({
    'category': ['skirt', 'sweater', 'coat', 'jeans'],
    'quantity': [10, 15, 6, 11],                                     
    'price': [30000, 60000, 95000, 35000]
})
```
그러면 이번엔 2차원 리스트와 2차원 NumPy array를 가지고 DataFrame을 만들어 볼게요. 아래 코드를 보면, `two_dimensional_list`라는 2차원 리스트(list of lists)를 가지고 `list_df`를 만들었고 `two_dimensional_array`라는 2차원 NumPy array를 가지고 `array_df`를 만들었습니다.
```python
two_dimensional_list = [
    ['skirt', 10, 30000],
    ['sweater', 15, 60000],
    ['coat', 6, 95000],
    ['jeans', 11, 35000]
]
two_dimensional_array = np.array(two_dimensional_list)

list_df = pd.DataFrame(two_dimensional_list)
array_df = pd.DataFrame(two_dimensional_array)
```
이렇게 만든 `list_df`와 `array_df`를 출력해 보면, 둘다 아래와 같은 결과물이 나오는데요. DataFrame을 만들 때 컬럼의 이름을 따로 설정하지 않았기 때문에, 컬럼 자리에 그냥 0부터 시작하는 숫자값이 들어 있습니다. 이러면 각 컬럼이 무엇을 의미하는 지 알 수 없어서 불편하겠죠?



DataFrame을 만들 때 `columns`라는 옵션을 사용해서 컬럼명을 설정하는 것도 가능합니다.
```python
list_df = pd.DataFrame(two_dimensional_list, columns=['category', 'quantity', 'price'])
array_df = pd.DataFrame(two_dimensional_array, columns=['category', 'quantity', 'price'])
```
위와 같이 컬럼명을 설정한 뒤 다시 `list_df`와 `array_df`를 출력해 보면, 컬럼명이 아래 이미지처럼 잘 바뀌어 있는 것을 확인할 수 있죠.



마지막으로, 딕셔너리가 담겨 있는 리스트로 DataFrame을 만들 수도 있는데요. 아래 코드에서는 `dict_list`라는 리스트를 가지고 `dict_list_df`라는 DataFrame을 만들었습니다. 이것 또한 위에서 만든 DataFrame과 동일한 형태를 가지고 있죠.
```python
dict_list = [
    {'category': 'skirt', 'quantity': 10, 'price': 30000},
    {'category': 'sweater', 'quantity': 15, 'price': 60000},
    {'category': 'coat', 'quantity': 6, 'price': 95000},
    {'category': 'jeans', 'quantity': 11, 'price': 35000}
]

df4 = pd.DataFrame(dict_list)
```
지금까지 DataFrame을 만드는 여러 가지 방법을 알아봤는데요. 이번 레슨에서 배운 내용을 모두 외울 필요는 없지만, 코드를 보고 대략 어떤 형태의 DataFrame이 만들어지는지 이해할 수 있다면 앞으로 데이터 분야를 학습하실 때 많은 도움이 될 겁니다.