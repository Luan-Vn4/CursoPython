# Conversor centimentro/milímetros
medida = float(input("Informe uma medida em metros: "))
dec = medida*10
cent = medida*100
mili = medida*1000
dam = medida/10
hec = medida/100
quil = medida/1000
print(f"A medida {medida:.2f}m corresponde:\nMilímetros: {mili:.2f}mm\nCentímetros: {cent:.2f}cm\n"
      f"Decímetros:{dec:.2f}dm\nDecâmetro: {dam:.2f}dam\nHectômetro: {hec:.2f}hm\nQuilômetro: {quil:.2f}km")
