# função que recebe a largura e comprimento do terreno e calcula sua área
def calc_area(lenght, width):
    area = lenght * width
    return area


le = float(input("Informe o comprimento: "))
wi = float(input("Informe a largura: "))
print(f"A área da figura {le}x{wi} é: {calc_area(le, wi)}u.n²")
