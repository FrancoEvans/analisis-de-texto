nombres = ('derito', 'evans', 'uade', 'z', 'a', 'zz')

gen = (len(p) for p in nombres)
lens = tuple(gen)

print(nombres[lens.index(max(lens))])