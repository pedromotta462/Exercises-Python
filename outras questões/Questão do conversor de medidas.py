print('Iremos converter uma medida em cm para m,dcm e km, com uma precisão de 5 casa decimais')
num = float(input('Digite a medida que você gostaria de converter: '))

m = num/100
dcm = num/10
km = num/100000

print('valor convertido em:')
print('metro: {:.5f}'.format(m))
print('decímetro: {:.5f}'.format(dcm))
print('Quilômetro: {:.5f}'.format(km))