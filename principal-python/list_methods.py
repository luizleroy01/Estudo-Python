#an example of list method using python

#crud operations with an task list

tasks = list()
answer = str(input("Deseja realizar alguma operacao?"))

while answer != "n":
    op = int(input("Digite a operacao: 1-inserir,2-visualizar,3-editar,4-excluir,5-filtrar"))

    if op == 1:
        item = str(input("Digite a descrição da tarefa:"))
        tasks.append(item)
    
    elif op == 2:
        for i in range(len(tasks)):
            print(i+1,tasks[i],end="\n")
    
    elif op == 3:
        for i in range(len(tasks)):
            print(i+1,tasks[i],end="\n")
        
        id = int(input("Digite o id da tarefa que deseja editar"))
        
        if id <= len(tasks):
            newTask = str(input("Digite a nova descrição da tarefa"))
            tasks[id] = newTask

    elif op == 4 :
        id = int(input("Digite o id da taefa que deseja excluir"))
        if id < len(tasks):
            #is possible to use op ou remove to delete and determinated task
            del tasks[id]
    
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
    
    answer = str(input("Deseja realizar alguma operacao?"))
    #operation encaixar to insert a new task between others

print("Sistema Finalizado com sucesso")