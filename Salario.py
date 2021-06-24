'''
Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento. Para
salários superiores a R$1250,00, calcule um aumento
de 10%. Para os inferiores ou iguais, o aumento é de 15%
'''
salario = float(input('Digite o Salário: R$').replace(',','.'))
if salario > 1250:
    r = salario * 0.10
    salario += r
    print('O aumento foi de \33[31mR${0:.2f}\33[m e o salário ficou '
          'R${1:.2f}'.format(r,salario).replace('.',','))
else:
    r = salario * 0.15
    print('O aumento foi de \33[34mR${0:.2f}\33[m e o salário ficou R$'
          '{1:.2f}'.format(r,salario).replace('.',','))
