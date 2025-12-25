# Programa para cálculo de IMC com validações completas

def entrada_valida(valor):
    if len(valor) > 4:
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
peso_str = input("Digite seu peso (kg) e pressione ENTER: ")

if not entrada_valida(peso_str):
    print("Entrada inválida. Use apenas números e vírgula ou ponto.")
    exit()

peso = converter_para_float(peso_str)

if peso is None or peso < 1 or peso > 999:
    print("Peso inválido. Informe um valor entre 1 e 999 kg.")
    exit()


# Altura
altura_str = input("Digite sua altura (m) e pressione ENTER: ")

if not entrada_valida(altura_str):
    print("Entrada inválida. Use apenas números e vírgula ou ponto.")
    exit()

altura = converter_para_float(altura_str)

if altura is None or altura < 1 or altura > 3:
    print("Altura inválida. Informe um valor entre 1 e 3 metros.")
    exit()


# Cálculo do IMC
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "baixo peso"
elif imc < 25:
    classificacao = "peso adequado"
elif imc < 30:
    classificacao = "sobrepeso"
elif imc < 35:
    classificacao = "obesidade grau I"
elif imc < 40:
    classificacao = "obesidade grau II"
else:
    classificacao = "obesidade grau III"


# Resultado
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
