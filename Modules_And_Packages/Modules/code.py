from fibbonacci import*
print(fib(20))
print(fib2(30))

try:
    #Non-existent module
    import fibbonacci
    print(fib(5))
except ImportError:
    print('Module not found')

try:
    # Existing module, but non-existent object
    from mod import s
    print(s)
except ImportError:
    print('Object not found in module')