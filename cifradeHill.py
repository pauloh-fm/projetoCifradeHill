import numpy as numpy # Caso de error: pip install numpy

# utilizando a biblioteca numpy para realizar as operaçãoes matématicas avançadas

# alfabeto proposto: 26 (minusculas) + espaço + 26 (maiusculas) = 53
# inicialmente apenas projetado para letras minusculas
def converterTextoAscii (texto):
    asciiTexto = []
    for i in range(0,len(texto)):
        asciiTexto.append((ord(texto[i]))) # transformo cada caracter do texto em seu equivalente ascii
        if asciiTexto[i] == 32:
            asciiTexto[i] = 27 #definindo o espaço no alfabeto
        elif asciiTexto[i] < 97:
            asciiTexto[i] = (asciiTexto[i] % 65) + 28 # definindo as letras maiusculas no alfabeto (28 - 54)
        else:
            asciiTexto[i] = (asciiTexto[i]%97)+1 # definindo as letras minusculas do alfabeto ( 1 - 26)
    print(f"Array inicial (numerica) ={asciiTexto}")
    return asciiTexto

def converterasciiTexto(textoEncriptografado):
    print(f"Array criptografada ={textoEncriptografado}")
    textoConvertido = []
    for valor in textoEncriptografado:
        if valor == 32:
                textoConvertido.append(chr(valor)) # convertendo de volta para o valor ascii espaço
        elif valor >= 28 and valor <= 54:
                textoConvertido.append(chr((valor-28)+ 65))  # convertendo de volta para o valor ascii letras maisculas
        else:
                textoConvertido.append(chr(valor+96))# convertendo de volta para o valor ascii letras minusculas
    return textoConvertido

def criptografar(asciiTexto,matrizChave):
    textoEncriptografado = [] # array para armazenar o valor final do texto encriptografado
    t = 0
    cont = 0
    # Passo 1: Inverter a matrizChave
    #matrizInversa = numpy.linalg.inv(matrizChave) # Função para inverter a matriz
    # Passo 2: multiplicar a matrizInversa pelos caracters correspondentes do asciiTexto
    if (len(asciiTexto) % 2):
        asciiTexto.append(0) # tornando o tamanho do asciiTexto sempre em par
    for i in range(0, int(len(asciiTexto)/2)):
        if i > 0:
            t +=2
        for j in range(0, 2):
            #print (f"({matrizChave[j][0]} * {asciiTexto[t]}) + ({matrizChave[j][1]}*{asciiTexto[t+1]})")
            textoEncriptografado.append(round(matrizChave[j][0] * asciiTexto[t]) + (matrizChave[j][1]*asciiTexto[t+1])) # mutiplicando os valores da primeira linha da matriz inversa 
            #print(i+j)
            if textoEncriptografado[cont] < 0:
                textoEncriptografado[cont] = (26-(textoEncriptografado[cont] % 26)) # caso o valor seja negativo, deixamos eles no alfabeto e subitraimos por 26
            else:
                textoEncriptografado[cont] = (textoEncriptografado[cont] % 26) # mantendo os valores dentro da faixa do alfabeto
            cont+=1
    return converterasciiTexto(textoEncriptografado)
# def descriptografar
resultado = ""
matrizChave = numpy.array([
    [2 , 1],
    [-1 , 4]
])
with open ("texto.txt", "r") as texto:
    textoInicial = texto.read()
print(f"Texto a ser convertido : {textoInicial}")
asciiTexto = converterTextoAscii(textoInicial)
textoEncriptografado = criptografar(asciiTexto,matrizChave)
print("Texto criptografado: ",end="")
#print(*textoEncriptografado, sep = "")
resultado = "".join(textoEncriptografado)
print(resultado)
arquivo = open("saida.txt", "w")

arquivo.write(resultado)

#print(f"Texto criptografado: {*textoEncriptografado}")
# textoConvertido = converterTextoAscii(entrada)
# print(asciiTexto)
#print(matrizChave[0][0])
#print(criptografar(entrada,matrizChave))