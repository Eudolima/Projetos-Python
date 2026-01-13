def verificar_status_pedido(status_code):
    match status_code:
        case 200:
            return "Pedido bem-sucedido ✅"
        case 404:
            return "Pedido não encontrado ❌"
        case 500:
            return "Erro no servidor ⚠️"
        case _:
            return "Código de status desconhecido ❓"
        
print(verificar_status_pedido(200))  # Teste com código 200
print(verificar_status_pedido(404))  # Teste com código 404
print(verificar_status_pedido(500))  # Teste com código 500
print(verificar_status_pedido(123))  # Teste com código desconhecido