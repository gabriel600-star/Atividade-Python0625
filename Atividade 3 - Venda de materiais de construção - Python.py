print("=" * 61)
print("   ATIVIDADE 3 - Venda de Materiais de Contrução - Python")
print("-" * 61)
print(" " * 16 + "Gabriel de Castro, 11 - Augusto Messa, 04")
print("=" * 61)

valorDesconto = float(0)
taxaEntrega = float(0)
kgMateriais = float(0)
nome = str(input("Digite o nome do cliente.........: "))
qtdFerramenta = int(input("Qtde. de ferramentas.............: "))
qtdMatAcab = int(input("Qtde. de materiais de acabamento.: "))
qtdTintas = int(input("Qtde. de tintas..................: "))
print("-" * 61)
entrega = str(input("Entrega no local da obra?   (S/N): "))

if entrega == "S" or entrega == "s":
    kgMateriais = float(input("Total de quilos dos produtos.....: "))
    mensagemFinal = "Entregar na obra!"
    taxaEntrega = float(kgMateriais * 1)

cupomDesconto = str(input("Possui cupom de desconto?   (S/N): "))
totalItens = (qtdFerramenta + qtdMatAcab + qtdTintas)
valorTotal = float(qtdFerramenta * 50) + (qtdMatAcab * 30) + (qtdTintas * 80)
mensagemFinal = "Retirar na loja!"
print("=" * 61)
print("Cliente", nome, "comprou", totalItens, "itens:")
print("-" * 61)
if cupomDesconto == "S" or cupomDesconto == "s":
    valorDesconto = float(valorTotal * 0.1)

valorPagar = float(valorTotal + taxaEntrega - valorDesconto)
print("Quantidade total de itens:", totalItens)
print("Valor total dos itens....: R$", ("%.2f" % valorTotal))
print("Desconto do cupom........: R$", ("%.2f" % valorDesconto))
print("Taxa de entrega..........: R$", ("%.2f" % taxaEntrega))
print(" " * 26 + "-" * 13)
print("Valor total a pagar......: R$", ("%.2f" % valorPagar))
print("-" * 61)
print(mensagemFinal)
print("=" * 61)