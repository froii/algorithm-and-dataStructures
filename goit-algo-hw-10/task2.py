import time
import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла
start_time = time.perf_counter()
result, error = spi.quad(f, a, b)
quad_time = time.perf_counter() - start_time
print("Інтеграл: ", result, error, quad_time)  # Інтеграл: 2.666666666666667 2.960594732333751e-14
print(f"Час: {quad_time * 1000:.4f} мс")

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


# Метод Монте-Карло
test_sizes = [100, 1000, 10000, 100000, 1000000, 10000000]

for n in test_sizes:
    start_time = time.perf_counter()
    x_rand = np.random.uniform(a, b, n)
    y_rand = np.random.uniform(0, f(b), n)
    under_curve = y_rand <= f(x_rand)
    mc_result = (under_curve.sum() / n) * (b - a) * f(b)

    error_abs = abs(mc_result - result)
    error_rel = (error_abs / result) * 100
    mc_time = time.perf_counter() - start_time

    print(f"\nn = {n:}")
    print(f"  Результат: {mc_result:.6f}")
    print(f"  Похибка: {error_abs:.6f}")
    print(f"⏱️  Час: {mc_time * 1000:.4f} мс\n")
