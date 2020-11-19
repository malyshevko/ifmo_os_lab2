# Указываем кол-во потоков
THREADS = 99

# Подключаем нужные библиотеки
# Время выполнения
import time
# Ограничение потоков
from threadpoolctl import threadpool_limits
# Расчет матрицы
import numpy as np

# запускаем расчеты и ограничиваем потоки
with threadpool_limits(limits=THREADS, user_api='blas'):
	# время начала выполнения
	start = time.time()
	#создаем матрицу (двумерный массив) и умножаем его на самого себя
	a = np.ones((4096, 4096))
	a.dot(a)
	# время выполнения
	print(time.time()-start)