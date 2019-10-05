p = int(input())
q = int(input())
def is_prime(n: int) -> bool:
    delitel = 2
    koldel = 1
    while delitel*delitel <= n and n % delitel == 0:
        koldel+=1
    if koldel > 1:
        return False
    else:
        return True
    pass

def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    elif (is_prime(p) and is_prime(q)):
         n = pq
         phi = (p-1)(q-1)

    def gcd(e: int, phi: int) -> int:
        while gsd!=1:
            e = random.randrange(1, phi)
            e1=e
            if phi-e == 1:
                gsd = 1
            else:
                if phi > e:
                    while phi%e != 0 or phi!=e or phi==0 or e==0:
                        phi = phi-e
                        gsd = phi
                else:
                    while e%phi != 0 or phi!=e or phi==0 or e==0:
                        e = e-phi
                        gsd = e
                        
            if phi == 1 and e == 1 or gsd == 1:
                e = e1 
    pass       
    d=0
    while d*(e%phi)!=1:
        d1 = random.randrange(1, phi)
        if d1 != e:
            d = d1
        else:
            d=0
    return ((e, n), (d, n))