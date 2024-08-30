지난 영상에서 그래프를 간단하게 꾸미는 방법에 대해 배웠는데요. 이번 레슨에서는 Matplotlib을 사용해서 그래프의 크기를 조절하는 방법 몇 가지를 소개해 드리겠습니다. 이번에도 키와 몸무게 데이터가 들어 있는 `height_array`와 `weight_array`를 사용하겠습니다.

```python
import numpy as np
import matplotlib.pyplot as plt

height_array = np.array([
    165, 164, 155, 151, 157, 162, 155, 157, 165, 162,
    165, 167, 167, 183, 180, 184, 177, 178, 175, 181,
    172, 173, 169, 172, 177, 178, 185, 186, 190, 187
])

weight_array = np.array([
    62, 59, 57, 55, 60, 58, 51, 56, 68, 64,
    57, 58, 64, 79, 73, 76, 61, 65, 83, 80,
    67, 82, 88, 62, 61, 79, 81, 68, 83, 80
])
```
일단 아래와 같은 코드를 통해 산점도를 그려 볼게요. Matplotlib에서는 그래프의 크기를 기본적으로 인치 단위로 표현하는데요. 따로 설정을 하지 않으면 가로 6인치, 세로 4인치 크기의 그래프가 나옵니다.

```python
plt.scatter(height_array, weight_array)
plt.title('Height and Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
```
다른 크기의 그래프를 원할 때에는 아래와 같이 pyplot의 `figure()`라는 함수를 호출해서, 그래프의 크기를 의미하는 `figsize`라는 파라미터에 가로 길이, 세로 길이 순서로 튜플 값을 넘겨주면 됩니다. 가로 10인치, 세로 4인치 크기의 그래프를 그려 봤는데, 기존 그래프보다 가로로 좀 더 길쭉한 그래프가 나온 거 보이시죠? 이 방법은 그래프 하나하나의 크기를 설정할 때 사용하는데요. 즉, 그래프 크기를 가로 10인치, 세로 4인치로 설정한 코드는 이번에만 적용되고 다음에 그래프를 그릴 때에는 다시 기본값(가로 6인치, 세로 4인치)으로 초기화가 됩니다.

```python
plt.figure(figsize=(10, 4)) 
plt.scatter(height_array, weight_array)
plt.title('Height and Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
```

이런 식으로 그래프를 그릴 때마다 일일이 크기를 지정하지 않고, 전체적으로 그래프 크기를 통일하고 싶을 수도 있겠죠? 이럴 때에는 아래와 같이 pyplot의 `rcParams` 속성에 직접 접근하여 그래프 사이즈의 기본 설정을 변경할 수 있습니다. 이번에는 가로 5인치, 세로 5인치로 바꿔줬는데요. 앞으로 같은 노트북 파일 안에서 그래프를 그리면, 따로 설정을 바꿔주지 않는 한 계속 가로 5인치, 세로 5인치 크기의 그래프가 나올 겁니다.

```python
plt.rcParams['figure.figsize'] = (5, 5)
plt.scatter(height_array, weight_array)
plt.title('Scatter Plot')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()
```

간단히 정리하면, 그래프의 크기를 개별적으로 바꾸고 싶을 때에는 `figure()` 함수로 `figsize`를 설정하면 되고요. 전체적으로 그래프 크기를 일관되게 설정하고 싶을 때에는 `rcParams` 속성을 변경해 주면 됩니다. 사실 그래프 크기를 설정하는 방법은 더 다양한데요. Matplotlib 기준으로는 이번 레슨에서 소개해 드린 방법들이 가장 쉽고 간단한 편이니까, 노트를 잘 읽어 보고 코드를 숙지해 두시는 걸 추천드립니다!