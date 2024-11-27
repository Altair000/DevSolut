import random

def luhn_check(card_number):
    """Verifica si el número de tarjeta es válido según el algoritmo de Luhn."""
    total = 0
    reverse_digits = [int(d) for d in str(card_number)][::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:  # Duplicar cada segundo dígito
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0

def generate_card(bin_number):
    """Genera un número de tarjeta de crédito válido."""
    bin_number = str(bin_number)
    card_number = bin_number  # Comienza con el BIN

    # Completa los primeros 15 dígitos, dejando espacio para el dígito de control
    while len(card_number) < 15:
        card_number += str(random.randint(0, 9))

    # Calcula el dígito de control
    for i in range(10):  # Probar con dígitos del 0 al 9
        if luhn_check(card_number + str(i)):
            return card_number + str(i)  # Retorna el número de tarjeta válido
