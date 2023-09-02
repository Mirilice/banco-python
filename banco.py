menu="""
1 - Depósito
2 - Saque
3 - Ver Extrato
4 - Encerrar sessão    
=>"""

saldo = 0
LIMITE = 500
quant_saques = 0
LIMITE_SAQUE = 3
extrato = ""


while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor=float(input("""Depósito: Informe o valor 
                          =>"""))
        if valor>0:
            saldo+=valor
            extrato+=f"Depósito:       {valor:.2f}\n"
        else:
            print("Operação inválida!")
    elif opcao == 2:
         valor=float(input("""Saque: Informe o valor 
                          =>"""))
         excedeu_saldo = valor>saldo
         excedeu_limite = valor>LIMITE
         excedeu_saques = quant_saques>LIMITE_SAQUE    
         if (excedeu_saldo or excedeu_limite):
             print("Operação inválida!")    
             break
         if(excedeu_saques):
              print("Operação inválida!")    
              break
         elif valor>0:
            saldo-=valor
            extrato+=f"Saque:          {valor:.2f}\n"
            quant_saques+=1
            print(quant_saques)
         else:
             print("Operação inválida!")  
             break
    elif opcao==3:
        print("Gerando Extrato...")
        print(f"""\n=Total Disponível  {saldo}

Limites de Crédito

Saques disponíveis  {LIMITE_SAQUE - quant_saques}
Limite por Saque    {LIMITE}

Histórico       Valor(R$)
""")
        print(extrato)
    elif opcao==4:
        print("Encerrando...")
        break
    else:
        print("Operação inválida!")
        break