n = q = m = s = 0
c = 'S'
maior = menor = 0
while c in ['S']:
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    s += n
    q += 1
    m = s / q
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {}'.format(q, m))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
