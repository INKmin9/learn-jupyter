import numpy as np
import matplotlib.pyplot as plt

age_array = np.array([
	27, 25, 29, 22, 26, 28, 40, 42, 34, 31,
	37, 36, 40, 32, 41, 47, 52, 49, 51, 50,
	49, 46, 47, 46, 47, 45, 57, 58, 60, 56
])

salary_array = np.array([
	44009, 83450, 95025, 63748, 78652,
	58977, 114733, 126353, 121904, 125083,
	143739, 140754, 144346, 114899, 125806,
	180252, 153374, 171057, 161305, 193786,
	167238, 150157, 179843, 195326, 165849,
	164887, 131372, 135876, 113796, 143050
])

# 여기에 코드를 작성하세요.
plt.scatter(age_array, salary_array, c = 'red', marker = 's')
plt.title('Age and Salary')
plt.xlabel('Age')
plt.ylabel('Salary($)')
plt.show