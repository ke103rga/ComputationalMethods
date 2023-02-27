import pandas as pd


def f(x):
    return 12*x**4 + 11*x**3 - 10*x**2 - 999


def der_f(x):
    return 48*x**3 + 33*x**2 - 20*x


def computate(x0, p=1, eps=10**(-4)):
    x_prev = x0
    x_next = x_prev - p*f(x_prev)/der_f(x_prev)
    count = 0
    while abs(x_next - x_prev) > eps:
        x_prev = x_next
        x_next = x_next - p * f(x_next) / der_f(x_next)
        count += 1
    return x_next, count


def solve(x0_values):
    results = []
    for p in [1]:
        for x0 in x0_values:
            res, n_iter = computate(x0, p)
            results.append({"param_p": p, "result": res, "n_iterations": n_iter})
    return pd.DataFrame(results)


print(solve([-3, 3]))