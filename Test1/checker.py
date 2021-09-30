from Test01 import *
try:
    a=prob19()
    b=prob19()
    c=prob19()

    d=prob20()

    e=prob21()

    try:
        f=prob22()
    except ValueError as e:
        assert e!='math domain error', 'code did not detect problematic triangle'

    g=prob22()
    h=prob22()
    i=prob22()

except Exception as e:
    print(e)
    print('tests failed')
