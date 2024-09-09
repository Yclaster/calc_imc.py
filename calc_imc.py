def calcular_imc(peso, altura):
    """Calcula o IMC com base no peso e altura fornecidos."""
    imc = peso / (altura ** 2)
    return imc

# Solicita os dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Chama a função para calcular o IMC
resultado = calcular_imc(peso, altura)

# Imprime o resultado
print(f"Seu IMC é: {resultado: .2f}")

# Classificação do IMC (simplificada)
if resultado < 18.5:
    print("Abaixo do peso")
elif resultado < 25:
    print("Peso normal")
elif resultado < 30:
    print("Sobrepeso")
else:
    print("Obesidade")