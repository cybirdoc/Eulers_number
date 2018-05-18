# Eulers_number.py
# outputs e to n places &lt; 8000
# Modified for e from the method used for pi at:
# https://possiblywrong.wordpress.com/2017/09/30/digits-of-pi-and-python-generators/

def continued_fraction(a, b, base=10):
    """Generate digits of continued fraction a(0)+b(1)/(a(1)+b(2)/(...)."""
    (p0, q0), (p1, q1) = (a(0), 1), (a(1) * a(0) + b(1), a(1))
    k = 1
    while True:
        (d0, r0), (d1, r1) = divmod(p0, q0), divmod(p1, q1)
        if d0 == d1:
            yield d1
            p0, p1 = base * r0, base * r1
        else:
            k = k + 1
            x, y = a(k), b(k)
            (p0, q0), (p1, q1) = (p1, q1), (x * p1 + y * p0, x * q1 + y * q0)
            
def e_try(n):
    digits = continued_fraction(lambda k: 2 if k == 0 else k - k//3 if k%3 == 2 else 1,
                                lambda k: 1, 10)                  
    for k, digit in zip(range(n), digits):
        if k == 1:
            print('.',end='')
        print(digit, end='')
    print('\n')
        
while True:
    try:
        n = int(input("Let's calculate n digits of e! Enter an interger <= 8000: "))
        if n > 8000:
            n = 8000
            print("Using n = 8000")
        else:
            print('n =',n)
        break
    except: 
        print("Please enter an integer.")
        continue        

e_try(n)
