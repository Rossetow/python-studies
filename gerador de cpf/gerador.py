import random

cpf=[random.randrange(0,9) for x in range (9)]
dig1 = 0
dig2 = 0

dig1 = sum(cpf[x]*(10-x) for x in range(len(cpf)))
   
cpf.append(0 if dig1%11<=1 else 11-dig1%11)
 
dig2 = sum(cpf[x+1]*(10-x) for x in range(9))

cpf.append(0 if dig2%11<=1 else 11-dig2%11)

# print(str(cpf[0])+str(cpf[1])+str(cpf[2])+"."+str(cpf[3])+str(cpf[4])+str(cpf[5])+"."+str(cpf[6])+str(cpf[7])+str(cpf[8])+"-"+str(cpf[9])+str(cpf[10]))
print('%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf))