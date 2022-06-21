from ortools.linear_solver import pywraplp

print('Задача ЛП: ')

solver = pywraplp.Solver.CreateSolver('GLOP')

# добавление переменных задачи
x1 = solver.NumVar(0, solver.infinity(), 'x1')
x2 = solver.NumVar(0, solver.infinity(), 'x2')
x3 = solver.NumVar(0, solver.infinity(), 'x3')
x4 = solver.NumVar(0, solver.infinity(), 'x4')
x5 = solver.NumVar(0, solver.infinity(), 'x5')
x6 = solver.NumVar(0, solver.infinity(), 'x6')
# проверим, что мы добавили верное количество переменных
print(f'Kоличество переменных: {solver.NumVariables()}')

# добавление ограничений
solver.Add(2*x1 + 1*x2 - 1*x3 - 3*x4 + 4*x5 + 7*x6 <= 7)
solver.Add(0*x1 + 1*x2 + 1*x3 + 1*x4 + 2*x5 + 4*x6 <= 16)
solver.Add(6*x1 - 3*x2 - 3*x3 + 1*x4 + 1*x5 + 1*x6 <= 6)
# проверим, что мы добавили верное количество переменных
print(f'Количество ограничений: {solver.NumConstraints()}')

# добавление целевой функции
solver.Maximize(1*x1 + 2*x2 + 1*x3 - 1*x4 + 2*x5 + 3*x6)

# решение задачи
status = solver.Solve()

# вывод резульатов
if status == pywraplp.Solver.OPTIMAL:
    print('Решение:')
    print(f'Значение целевой функции = {solver.Objective().Value()}')
    print(f'x1 = {x1.solution_value()}')
    print(f'x2 = {x2.solution_value()}')
    print(f'x3 = {x3.solution_value()}')
    print(f'x4 = {x4.solution_value()}')
    print(f'x5 = {x5.solution_value()}')
    print(f'x6 = {x6.solution_value()}')
else:
    print('Задача не имеет решений')

########################################################################
print('Задача целочисленного ЛП: ')
solver = pywraplp.Solver.CreateSolver('SCIP')

# добавление переменных задачи
x1 = solver.IntVar(0, solver.infinity(), 'x1')
x2 = solver.IntVar(0, solver.infinity(), 'x2')
x3 = solver.IntVar(0, solver.infinity(), 'x3')
x4 = solver.IntVar(0, solver.infinity(), 'x4')
x5 = solver.IntVar(0, solver.infinity(), 'x5')
x6 = solver.IntVar(0, solver.infinity(), 'x6')

# проверим, что мы добавили верное количество переменных
print(f'Kоличество переменных: {solver.NumVariables()}')

# добавление ограничений
solver.Add(2*x1 + 1*x2 - 1*x3  - 3*x4 + 4*x5 + 7*x6 <= 7)
solver.Add(0*x1 + 1*x2 + 1*x3  + 1*x4 + 2*x5 + 4*x6 <= 16)
solver.Add(6*x1 - 3*x2 - 3*x3  + 1*x4 + 1*x5 + 1*x6 <= 6)

# проверим, что мы добавили верное количество переменных
print(f'Количество ограничений: {solver.NumConstraints()}')

# добавление целевой функции
solver.Maximize(1*x1 + 2*x2 + 1*x3 - 1*x4 + 2*x5 + 3*x6)

# решение задачи
status = solver.Solve()

# вывод результатов
if status == pywraplp.Solver.OPTIMAL:
    print('Решение:')
    print(f'Значение целевой функции = {solver.Objective().Value():.0f}')
    print(f'x1 = {x1.solution_value():.0f}')
    print(f'x2 = {x2.solution_value():.0f}')
    print(f'x3 = {x3.solution_value():.0f}')
    print(f'x4 = {x4.solution_value():.0f}')
    print(f'x5 = {x5.solution_value():.0f}')
    print(f'x6 = {x6.solution_value():.0f}')
else:
    print('Задача не имеет решений')
