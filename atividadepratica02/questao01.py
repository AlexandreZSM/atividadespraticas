valor_em_rais = float(input("Digite o valor em reais: "))
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_em_rais / taxa_dolar
valor_em_euro = valor_em_rais / taxa_euro

print("Valor em reais: R$", valor_em_rais)
print("Valor em dólar: U$", round(valor_em_dolar, 2))
print("Valor em euro: €", round(valor_em_euro, 2))
