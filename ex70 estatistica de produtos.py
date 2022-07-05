
print('='*30)
print('{:^30}'.format('Lojas Silva'))
print('='*30)
totalp = maismil = maisbarato = cont = 0
while True:
    produto = str(input('Digite o nome do produto:'))
    p = float(input('Preço:'))
    totalp += p
    cont += 1
    if p > 1000:
        maismil += 1
    if cont == 1:
        maisbarato = p
    else:
        if p < maisbarato:
            maisbarato = p
    continuar = str(input('Quer continuar? S/N')).strip().upper()
    if continuar == 'S':
        print('ok...')
    if continuar == 'N':
        break
print(f'O total da compra foi de R$:{totalp:.2f}')
print(f'Temos {maismil} produtos custando mais de R$1000')
print(f'E o produto mais barato foi de R${maisbarato:.2f} ')
print('='*40)
print('FIM. Volte sempre.')
