def anteriores(string,atual,inicial):
    global subcadeias
    global cadeia
    if atual < 0:
        return
    if string[atual:inicial] not in cadeia:
        subcadeias.append(string[atual:inicial])
    anteriores(string,atual-1,inicial)
    return
    
entrada = input()
cadeia = []
anterior = ''
for p,i in enumerate(entrada):
    subcadeias = []
    anteriores(entrada,p-1,p+1)
    if i not in cadeia:
        subcadeias.append(i)
    cadeia.extend(subcadeias)
