def realizar_saque(valor, saldo):
    if valor > saldo:
        return "Saldo insuficiente para realizar o saque 💸"
    if valor <= 0:
        return "Valor deve ser maior que zero ❌"
    saldo -= valor
    return f"Saque de R${valor} realizado com sucesso. Saldo restante: R${saldo} ✅"

print(realizar_saque(150, 1000))  # Teste com saldo suficiente
print(realizar_saque(1200, 1000)) # Teste com saldo insuficiente
print(realizar_saque(-50, 1000))  # Teste com valor inválido



 
