def valor_avista(valor):
    desconto = valor * 0.09
    valor_com_desconto =valor-desconto
    return valor_com_desconto

def pagamento_em_5vezes(valor):
    parcela = valor / 5
    return parcela 

def pagamento_em_10vezes(valor):
    juros = valor * 0.17
    total_acrescimo = juros + valor 
    prestacoes = total_acrescimo / 10
    return prestacoes

valor_compra = float(input("Digite o valor da compra: "))
valor_a_vista =valor_avista (valor_compra)
valor_parcela_5_vezes = pagamento_em_5vezes(valor_compra)
valor_parcela_10_vezes = pagamento_em_10vezes(valor_compra)

print("Valor para pagamento à vista: {:.2f}".format(valor_a_vista))
print("Valor da prestação para pagamento em 5 vezes: {:.2f}".format(valor_parcela_5_vezes))
print("Valor da prestação para pagamento em 10 vezes: {:.2f}".format(valor_parcela_10_vezes))