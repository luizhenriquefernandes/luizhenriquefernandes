'''
Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência
de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8

'''
n = int(input('Digite o número da sequência de Finobacci: '))
cont = 0
cont1 = 1
t1 = 0
t2 = 1
print('{0}➡{1}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1+t2
    print('➡{0}'.format(t3),end='')
    '''
    0   1   1   2   3   5   8   13
    t1  t2  t3
        t1  t2  t3
            t1  t2  t3 percorre o termo.
    '''
    t1 = t2 # percorre o termo e vai somando o fibonacci
    t2 = t3
    cont += 1
print('➡fim'.format(t3),end='')















