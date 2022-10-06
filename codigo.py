c = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
 
#1) eliminamos los espacios y limpiamos el string
s = c.replace(" ", "").replace(",","").replace(".","")
 
#2) metemos en hashlet la cantidad de veces que aparece cada caracter
hashlet = {}
i = 0
while(i < len(s)):
    if(s[i] not in hashlet.keys()):
        hashlet[s[i]] = s.count(s[i])
    i += 1
 
#3) ordenamos las letras en función de su frecuencia
 
frecuentes = []
i = 1
while i < 27:
    max = 0
    for letra in hashlet:
        if hashlet[letra] > max and letra not in frecuentes:
            l = letra
            max = hashlet[letra]
    frecuentes.append(l)
    i += 1

#4) asignamos las dos letras más frecuentes

m = c.replace("P", "M").replace("D","P").replace("A","D").replace(frecuentes[1],"A").replace("O","F").replace("I", "O").replace("C","I").replace("Q","B").replace("S","Q").replace("N","S").replace("J","N").replace("R","C").replace(frecuentes[0],"E").replace("T", "L").replace("K","R").replace("Z", "U").replace("V","Y").replace("H","T")
print(m)
# TABLA DE EQUIVALENCIAS DE C -> M
# X = E
# E = A
# T = L
# J = S
# K = R
# 
# 
# 
# 
# 
# 
# 