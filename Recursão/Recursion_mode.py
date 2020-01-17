cadeia = []
def Recursion(string,start,end):
    global cadeia
    if start == end:
        return
    if string[start:end] not in cadeia:
        cadeia.append(string[start:end])
    Recursion(string,start,end-1)
    Recursion(string,start+1,end)
    return

entrada = input()
Recursion(entrada,0,len(entrada))
    
