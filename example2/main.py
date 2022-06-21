from ortools.linear_solver import pywraplp

# тарифы на поставку
p = [
    [7, 9, 15, 4, 18],
    [13, 25, 8, 15, 5],
    [5, 11, 6, 20, 12],
]

# объем запасов на складах
Z = [200, 250, 250]

# заявки магазинов
R = [80, 260, 100, 140, 120]

# количество магазинов
Nm = len(R)
Ns = len(Z)

solver = pywraplp.Solver.CreateSolver('GLOP')

# добавление переменных задачи
x = []
for i in range(Ns):
    x.append([])
    for j in range(Nm):
        x[i].append(solver.NumVar(0, solver.Infinity(), f'x_{i+1}_{j+1}'))
# проверка того, что добавилось необходимое количество переменных
print(f'Количество переменных: {solver.NumVariables()}')

# добавление ограничений по объемам на складах
for i in range(Ns):
    constrain_expr = [x[i][j] for j in range(Nm)]
    solver.Add(sum(constrain_expr) <= Z[i])
# добавление ограничений по заявкам магазинов
for j in range(Nm):
    constrain_expr = [x[i][j] for i in range(Ns)]
    solver.Add(sum(constrain_expr) == R[j])
# проверка того, что добавилось необходимое количество ограничений
print(f'Количество ограничений: {solver.NumConstraints()}')

# добавление целевой функции
objective_expr = []
for i in range(Ns):
    for j in range(Nm):
        objective_expr.append(x[i][j] * p[i][j])
solver.Minimize(solver.Sum(objective_expr))

# решение задачи
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print(f'Значение целевой функции = {solver.Objective().Value()}')
    solution = [[x[i][j].solution_value() for j in range(Nm)] for i in range (Ns)]
    print('План поставок в виде матрицы:[')
    for i in range(Ns):
        print(solution[i])
    print(']')
else:
    print('Задача не имеет решения')
