import timeit

def time_m (*args,**kwargs):
    valores=locals()['args']
    def _decorador(target):
        def _decorated (number):
            objetivo = {'target': target, 'args': valores,'kwargs':kwargs}
            result=timeit.timeit('target(*args,**kwargs)',number=number,globals=objetivo)
            print(f'El tiempo de ejecución es {result}')
            return result
        return _decorated
    return _decorador

@time_m(20,30,40)
def solve(a, b, c):
   """Solves a quadratic equation given the coefficients."""
   root = (b**2 - 4*a*c) ** 1/2
   return (b + root)/2*a, (b - root)/2*a

solve(number=1000)

