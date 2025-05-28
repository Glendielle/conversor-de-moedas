def conversor_moedas():
    print("Bem-vindo ao Conversor de Moedas!")
    valor_reais = float(input("Digite o valor em reais (R$): "))
    print("Para qual moeda deseja converter?")
    print("1 - Dólar (USD)")
    print("2 - Euro (EUR)")
    print("3 - Libra Esterlina (GBP)")

    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == "1":
        taxa = 5.10  # valor fictício, 1 USD = 5.10 BRL
        moeda = "Dólar"
    elif opcao == "2":
        taxa = 5.60  # 1 EUR = 5.60 BRL
        moeda = "Euro"
    elif opcao == "3":
        taxa = 6.20  # 1 GBP = 6.20 BRL
        moeda = "Libra Esterlina"
    else:
        print("Opção inválida.")
        return

    valor_convertido = valor_reais / taxa
    print(f"R${valor_reais:.2f} equivalem a {valor_convertido:.2f} {moeda}.")

if __name__ == "__main__":
    conversor_moedas()
