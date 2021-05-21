acao_inicial = int(input('Quantas ações vc já tem ou irá comprar na primeira leva? '))
acao_mensal = int(input('Quantas ações vc irá comprar por mês? '))
preco = float(input('Qual é o valor da ação que vc irá comprar? '))
rend = float(input('Qual é a porcetagem de rendimento? '))
renda_desejada = float(input('Qual é a renda que vc deseja receber mensalmente? '))
rend = preco * rend / 100
rendimento_mensal = 0.0
rendimento = 0.0
rendimento_real = 0.0
contador = 0
valor_investido = 0.0
acao = acao_inicial + acao_mensal

while rendimento_mensal<renda_desejada:
    rendimento_mensal = acao * rend
    rendimento += rendimento_mensal
    valor_investido = acao * preco
    
    if rendimento_mensal > renda_desejada:
        rendimento_real = rendimento_mensal
        break
        
    else:
        acao += acao_mensal
        if rendimento > preco:
            quantidade = rendimento // preco
            rendimento %= preco
            acao += quantidade
    
    rendimento_mensal = 0
    contador += 1
meses =  contador % 12
ano = contador // 12
print(f'Vc irá demorar {contador} meses ou {ano} anos e {meses} meses para conseguir R${rendimento_real:.2f} de renda mensal.')
print(f'Você investiu R${valor_investido:.2f} comprando {acao:.0f} ações para conseguir a renda mensal desejada.')
