# Programa para cálculo de IMC (compatível com duplo clique no Windows)

def entrada_valida(valor):
    if len(valor) > 5:
        return False

    if valor.count(",") + valor.count(".") > 1:
        return False

    for c in valor:
        if not (c.isdigit() or c in [",", "."]):
            return False

    return True


def converter_para_float(valor):
    try:
        return float(valor.replace(",", "."))
    except ValueError:
        return None


# Peso
while True:
    peso_str = input("Digite seu peso (kg) e pressione ENTER: ")

    if not entrada_valida(peso_str):
        print("Entrada inválida. Use apenas números e vírgula ou ponto.\n")
        continue

    peso = converter_para_float(peso_str)

    if peso is None or peso < 1 or peso > 999:
        print("Peso inválido. Informe um valor entre 1 e 999 kg.\n")
        continue

    break


# Altura
while True:
    altura_str = input("Digite sua altura (m) e pressione ENTER: ")

    if not entrada_valida(altura_str):
        print("Entrada inválida. Use apenas números e vírgula ou ponto.\n")
        continue

    altura = converter_para_float(altura_str)

    if altura is None or altura < 0.5 or altura > 2.5:
        print("Altura inválida. Informe um valor entre 0.5 e 2.5 metros.\n")
        continue

    break


# Cálculo do IMC
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Baixo peso"
elif imc < 25:
    classificacao = "Peso adequado"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade grau I"
elif imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"


# Resultado
print("\n==============================")
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print("==============================\n")

input("Pressione ENTER para sair...")
