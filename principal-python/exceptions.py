#example of use of exceptions with python
r = str(input("Deseja realizar operação?"))

while r == "s":
    try:
        digito = int(input("Digite um numero:"))
        resultado = 20/digito
        print(resultado)
    except Exception as v:
        print(f"Error:{v}")
        raise ValueError("Tipos de variáveis incompatíveis")
    else:
        print(f"O resultado correto eh : {resultado}")
    finally:
        print(f"Operação finalizada")
    r = str(input("Deseja realizar operação?"))