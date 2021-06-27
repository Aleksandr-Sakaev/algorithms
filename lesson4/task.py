# Посчитать четные и нечетные цифры введенного натурального числа.
import timeit
import cProfile


# n = int(input('Введите натуральное число: '))
# even = odd = 0
# while n > 0:
#     if n % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     n = n // 10

print(timeit.timeit("even, odd", number=100, globals=globals()))
# 1.430000000013365e-05
# 1.0699999999808085e-05
# 1.039999999985497e-05
# 1.0299999999574538e-05
# 1.0500000000135401e-05
cProfile.run('even, odd')
# 3 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# def even_odd(number, even_=0, odd_=0):
#     if number == 0:
#         return even_, odd_
#     if number % 2 == 0:
#         even_ += 1
#     else:
#         odd_ += 1
#     number = number // 10
#     return even_odd(number, even_, odd_)
#
#
print(
    timeit.timeit('even_odd(532532)', number=100, globals=globals()), #0.0002375000000000016
    timeit.timeit('even_odd(53546546464565642532)', number=100, globals=globals()),  #0.0002375000000000016
    timeit.timeit('even_odd(53546454938534987593847598374546464565642532)', number=100, globals=globals()), #0.0002375000000000016
    sep='\n'
    )
cProfile.run('even_odd(5154545333333333333333348656685576899999934343565678988888888888888888888888888888888888888888888888888888888888888888888888888888888899999999999976530039493530490590565455655615451541514224125142512415241251425125457575754753040859434545315)')

# 245 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     242/1    0.001    0.000    0.001    0.001 task.py:25(even_odd)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def count_even_odd(n):
    n = abs(n)
    result = (1, 0) if n % 2 == 0 else (0, 1)
    if n < 10:
        return result
    return tuple(map(sum, zip(count_even_odd(n // 10), result)))


print(
    timeit.timeit('count_even_odd(532532)', number=100, globals=globals()), #0.000633600000000005
    timeit.timeit('count_even_odd(53546546464565642532)', number=100, globals=globals()),  #0.002169199999999996
    timeit.timeit('count_even_odd(53546454938534987593847598374546464565642532)', number=100, globals=globals()), #0.0055739
    sep='\n'
    )
cProfile.run('count_even_odd(5154545333333333333333348656685576899999934343565678988888888888888888888888888888888888888888888888888888888888888888888888888888888899999999999976530039493530490590565455655615451541514224125142512415241251425125457575754753040859434545315)')
# 485 function calls (245 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     241/1    0.001    0.000    0.001    0.001 task.py:61(count_even_odd)
#       241    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}