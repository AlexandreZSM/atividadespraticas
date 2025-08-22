peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros:"))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacado = "Abaixo do peso"
elif imc < 25:
    classificacado = "Peso normal"
elif imc < 30:
    classificacado = "Sobrepeso"
else:
    classificacado = "Obeso"

print(f"Seu IMC é {imc:.1f} e você está classificado como {classificacado}")