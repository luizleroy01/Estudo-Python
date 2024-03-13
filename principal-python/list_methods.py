#an example of list method using python

#crud operations with an task list
tasks = list()
def adicionar_tarefa():
     item = str(input("Digite a tarefa que desa incluir na lista:"))
     tarefa = {"descricao": item,"status":false}
    tasks.append(tarefa)

def exibir_tarefas():
    for i in range(len(tasks)):
        status = tasks[i].status ? 'completada' : 'não completada'
        print(f"{i+1} - {tasks[i]} : {status}")

def completar_tarefa(task_id):

    try:
        tasks[task_id].status = True
    except Exception as e:
        print("O id digitado para a tarefa é inválido, tente novamente")
        id = int(str("Digite o id da tarefa que deseja completar:"))
        tasks[id].status = True

def editar_tarefa(task_id):
    try:
        new_task = str(input("Digite a nova tarefa:"))
        tasks[task_id] = new_task
    except Exception as e:
        print("O id digitado para a tarefa é inválido, tente novamente")
        id = int(str("Digite o id da tarefa que deseja excluir:"))
        tasks[id].status = True

def excluir_tarefa(task_id):
    try:
        del tasks[task_id]
    except Exception as e:
        print("O id digitado para a tarefa é inválido, tente novamente")
        id = int(str("Digite o id da tarefa que deseja excluir:"))
        tasks.remove(id)

def menu():
        print("Lista de tarefas")
        print("1 - Adicionar nova tarefa")
        print("2 - Exibir tarefas")
        print("3 - Completar tarefa")
        print("4 - Editar tarefa")
        print("5 - Excluir tarefa")
        print("6 - Exportar lista de tarefas")
        print("7 - Filtrar tarefas")
        print("8 - Sair do programa")
        op = int(input("Digite a operacao que deseja realizar"))
        return op


op = menu()

while answer != 7:
    if op == 1:

       adicionar_tarefa()

    elif op == 2:
        exibir_tarefas()
    
    elif op == 3:
        exibir_tarefas()
        
        id = int(input("Digite o id da tarefa que deseja completar"))
        
        completar_tarefa(id)

    elif op == 4 :
        id = int(input("Digite o id da taefa que deseja editar"))
        editar_tarefa(id)
    
    elif op == 5 :
        opFiltro =int(input("Digite 1 para filtrar pelo inicio ou 2 para filtrar pelo fim"))

        if opFiltro == 1:
            inicial = int(input("Digite o index inicial:"))
            inicio = tasks[inicial:]
            for i in range(len(inicio)):
                print(inicio[i],end="\n")
        
        elif opFiltro == 2:
            final = int(input("Digite o index final"))
            fim = tasks[:final]
            for i in range(len(fim)):
                print(fim[i],end="\n")
    
    op = menu()
    #operation encaixar to insert a new task between others

print("Sistema Finalizado com sucesso")