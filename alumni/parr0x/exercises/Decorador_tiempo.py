import timeit

def time_m (target):

    def _decorated (*args, **kwargs):
        objetivo={'target':target,'args':args,'kwargs':kwargs}
        print(args,kwargs)
        result=timeit.timeit('target(*args, **kwargs)',number=1000,globals=objetivo)
        print(f'El tiempo de ejecución es {result}')
        return result
    return _decorated

@time_m
def solve(a, b, c):
   """Solves a quadratic equation given the coefficients."""
   root = (b**2 - 4*a*c) ** 1/2
   return (b + root)/2*a, (b - root)/2*a

solve(4, 2, 1)
solve(16, 25, c=5)


