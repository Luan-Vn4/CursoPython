# Conversor de temperatura

oprt = True
while oprt is True:
    resposta = float(input("Qual a unidade de medida? Celsius[1] Fahrenheit[2] Kelvin[3]\n"))
    if resposta == 1:
        t = float(input("Informe a temperatura: ºC"))
        tf = ((9*t+160)/5)
        tk = (t+273.15)
        print(f"Fahrenheit: {tf:.2f}ºF\nKelvin: {tk:.2f}K")
        oprt = False
    elif resposta == 2:
        t = float(input("Informe a temperatura: ºF"))
        tc = ((t-32)*5/9)
        tk = (tc + 273.15)
        print(f"Celsius: {tc:.2f}ºC\nKelvin: {tk:.2f}K")
        oprt = False
    elif resposta == 3:
        t = float(input("Informe a temperatura: K"))
        tc = (t - 273.15)
        tf = ((9*tc+160)/5)
        print(f"Celsius: {tc:.2f}ºC\nFahrenheit: {tf:.2f}ºF")
        oprt = False
    else:
        print("Resposta Inválida!!")
print("\nOperação concluída com sucesso!!")
