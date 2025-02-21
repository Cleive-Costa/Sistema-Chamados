chamados = []

def cadastrar_chamado(id_chamado, descricao, prioridade):
    chamados.append({
        "id": id_chamado,
        "descricao": descricao,
        "prioridade": prioridade,
        "finalizado": False
    })

def buscar_chamado(chave):
    for chamado in chamados:
        if chamado["id"] == chave or chave.lower() in chamado["descricao"].lower():
            return chamado
    return None

def remover_chamados_finalizados():
    global chamados
    nova_lista = []
    
    for chamado in chamados:
        if not chamado["finalizado"]:
            nova_lista.append(chamado)
    
    chamados = nova_lista

def listar_chamados():
    return sorted(chamados, key=lambda x: x["prioridade"], reverse=True)

def exibir_estatisticas():
    total = len(chamados)
    finalizados = sum(1 for ch in chamados if ch["finalizado"])
    pendentes = total - finalizados
    return {
        "total": total,
        "finalizados": finalizados,
        "pendentes": pendentes
    }

def reverter_chamados():
    chamados.reverse()

def limpar_chamados():
    chamados.clear()
    
cadastrar_chamado(1, "Erro na tela de login", 2)
cadastrar_chamdo(2, "Erro ao clicar", 1)

print('------------------------------------------------------------------------------------', end="\n\n")
print('Chamados Cadastrados: ', chamados, end="\n")
print('====================================================================================', end="\n")
print('Chamados Buscados: ', buscar_chamado(1), end="\n")
print('====================================================================================', end="\n")
print('Chamados depois da Remoção: ', remover_chamados_finalizados(), end="\n")
print('====================================================================================', end="\n")
print('Chamados Listados: ', listar_chamados(), end="\n")
print('====================================================================================', end="\n")
print('Chamados Estatisticas: ', exibir_estatisticas(), end="\n")
print('====================================================================================', end="\n")
print('Chamados Reversão: ', reverter_chamados(), end="\n")
print('====================================================================================', end="\n")
print('Chamados Limpar: ', limpar_chamados(), end="\n")
print('====================================================================================', end="\n\n")
