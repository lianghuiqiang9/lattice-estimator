from sage.all import *
x = var('x')
print(solve(3*x+5==10,x))

print(solve(x ** 2 + 4 * x + 4 == 100, x))

print(solve(x ** 3 - 3 * x ** 2 + 2 * x - 6 == 0, x))

y = var('y')
print(solve(x + y == 10, x))
print(solve(x + y == 10, (x, y)))
print(solve((x + y == 10, x - y == 5), (x, y)))


mod = 7
print(solve_mod(2*x + y == 3, mod))
print(solve_mod(2*x + y == 3, mod, solution_dict = True))
print(solve_mod((2*x + y == 3, x + 3*y == 1), mod))
print(solve_mod((2*x + y == 3, x + 3*y == 1), mod, solution_dict = True))


inv=inverse_mod(30,1373)
print(30*inv%1373) #1


d,u,v=xgcd(20,30)
print("d:{0} u:{1} v:{2}".format(d,u,v))#d:10 u:-1 v:1


