import random
import os

from timeit import default_timer as timer

def is_prime(n, k=10):  # number of tests = k
    if n % 2 == 0:
        return False
    if n % 5 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def calcular_mdc(a, b):
    resto = None
    while resto != 0:
        resto = a % b
        a  = b
        b  = resto

    return a

def sao_primos_entre_si(num1, num2):
    mdc = calcular_mdc(num1, num2)
    return mdc == 1

def gerar_random_primos():
    primos = []
    start = timer()
    
    while len(primos) < 2:
        #num = random.randint(100, 92233720368547758070345345345345)  # Altere o intervalo conforme necessário
        num = int.from_bytes(os.urandom(256), "big")
        #while True:
        if is_prime(num) and num not in primos:
            primos.append(num)
            end = timer()
            print('Tempo para achar primo ', len(primos), ": ", end - start, " segundos")
            start = timer()
            #break
    return primos

def funcao_totiente(p, q):
    oN = (p-1)*(q-1)
    return oN

def get_e(oN):
    while True:
        e = random.randrange(1, oN)
        if sao_primos_entre_si(e, oN):
            return e

def criptografar(e, n, texto):
    numeros = []
    numerosCripto = []
    textoCripto = []
    textoCriptografado = ""

    for letra in texto:
        numeros.append(ord(letra))
        
    #print(numeros)

    index = 1
    for num in numeros:
        print("Encriptando: ", index, "/", len(numeros))
        index += 1
        #nu = ((num ** e) % n)
        #nuDec = pow(num, e, n)
        #nu = pow_mod(num, e, n)
        nu = pow(num, e, n)
        numerosCripto.append(nu)
        #textoCripto.append(chr(nu))
        #textoCriptografado += chr(nu)

    #print(numerosCripto)

    #return textoCriptografado
    return numerosCripto

#def decriptografar(d, n, texto):
def decriptografar(d, n, numeros):
    numeros2Decript = []
    textoDecriptografado = ""

    #print(numeros2)

    index = 1
    for numd in numeros:
        print("Decriptando: ", index, "/", len(numeros))
        index += 1
        #nuDec = ((numd ** d) % n)
        nuDec = pow(numd, d, n)
        #nuDec = pow_mod(numd, d, n)
        textoDecriptografado += chr(nuDec)
        numeros2Decript.append(nuDec)

    #print(numeros2Decript)

    return textoDecriptografado

def pow_mod(num, e, n):
    result = 1
    num = num % n  # Reduz num modulo n primeiro, se necessário
    while e > 0:
        # Se e é ímpar, multiplica num com o resultado
        if e % 2 == 1:
            result = (result * num) % n
        # Agora e deve ser par
        e = e >> 1  # Divide e por 2
        num = (num * num) % n
    return result

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def get_d(e, oN):
    g, x, _ = egcd(e, oN)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % oN

def main():
    startApplication = timer()
    
    #print('Buscando primos: ')
    #pEq = gerar_random_primos()
    #pEq = [3,5]
    #print("Numeros gerados:", pEq)
    
    #p = pEq[0]
    #q = pEq[1]
    
    #print("p   :", p)
    #print("q   :", q)
    
    #n = p * q
    #print("N   :", n)
    
    #oN = funcao_totiente(p, q)
    #print("Ø(N):", oN)
    
    #e = get_e(oN)
    #print("e   :", e)
    
    #d = get_d(e, oN)
    #print("d   :", d)
    
    texto = "The information security is of significant importance to ensure the privacy of communications"
    
    print("Original: ", texto)
    
    txt = []
    
    #print("Chave Publica: ", "(", e, ", ", n, ")")
    #print("Chave Privada: ", "(", d, ", ", n, ")")
    
    #textoCriptografado = criptografar(e, n, texto)
    #print("Criptografado: ", textoCriptografado)
    
    start = timer()
    textoDecriptografado = decriptografar(d, n, textoCriptografado)
    print("Decriptografado: ", textoDecriptografado)
    end = timer()
    
    print('Tempo para decriptografar: ', end - start, " segundos")
    
    print('Tempo para processo inteiro: ', end - startApplication, " segundos")

# Execução do código
#main()