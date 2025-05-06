import re

def validar_cartao_credito(numero_cartao):
    bandeiras = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Elo": r"^(4011(78|79)|431274|438935|451416|457393|504175|5067[0-6]|509[0-9]{2}|627780|636297|636368|650[0-9]{2}|6516[0-9]|6550[0-9])\d{10,12}$",
        "Hipercard": r"^(606282|3841(?:[0|4|6]{1}))[0-9]{10,12}$"
    }

    numero_cartao = numero_cartao.replace(" ", "").replace("-", "")
    
    for bandeira, regex in bandeiras.items():
        if re.match(regex, numero_cartao):
            return f"Bandeira identificada: {bandeira}"
    
    return "Cartão inválido ou bandeira desconhecida"

# Exemplo de uso
numero = input("Digite o número do cartão de crédito: ")
resultado = validar_cartao_credito(numero)
print(resultado)