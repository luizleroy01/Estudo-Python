class PatriciaNode:
    def __init__(self, key="", value=None, children=None):
        self.key = key  # A chave armazenada no nó
        self.value = value  # O valor associado à chave, se houver
        if children is None:
            self.children = {}
        else:
            self.children = children

class PatriciaTree:
    def __init__(self):
        self.root = PatriciaNode()

    def insert(self, key, value):
        self._insert(self.root, key, value, key)

    def _insert(self, node, key, value, full_key):
        # Encontre o ponto de divergência entre a chave atual e a chave do nó
        i = 0
        while i < len(key) and i < len(node.key) and key[i] == node.key[i]:
            i += 1

        if i == len(node.key):
            # A chave do nó atual é um prefixo da chave a ser inserida
            if i == len(key):
                # As chaves são idênticas, atualize o valor
                node.value = value
            else:
                # Insira o restante da chave
                rest_key = key[i:]
                if rest_key in node.children:
                    self._insert(node.children[rest_key], rest_key, value, full_key)
                else:
                    node.children[rest_key] = PatriciaNode(rest_key, value)
        else:
            # Há uma divergência, quebre o nó atual
            prefix_common = node.key[:i]
            different_suffix = node.key[i:]
            # Crie um novo nó subdividido
            new_node = PatriciaNode(different_suffix, node.value, node.children)
            # Redefina o nó atual
            node.key = prefix_common
            node.value = None
            node.children = {different_suffix: new_node}

            # Se ainda há mais chave para inserir
            if i < len(key):
                rest_key = key[i:]
                node.children[rest_key] = PatriciaNode(rest_key, value)
            else:
                node.value = value

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(key) and i < len(node.key) and key[i] == node.key[i]:
            i += 1

        if i == len(node.key):
            if i == len(key):
                return node.value
            else:
                rest_key = key[i:]
                if rest_key in node.children:
                    return self._search(node.children[rest_key], rest_key)
        return None  # Chave não encontrada

# Exemplo de uso
ptree = PatriciaTree()
ptree.insert("romane", 1)
ptree.insert("romanus", 2)
ptree.insert("romulus", 3)
ptree.insert("rubens", 4)
ptree.insert("ruber", 5)
ptree.insert("rubicon", 6)
ptree.insert("rubicundus", 7)

print(ptree.search("romulus"))  # Deve retornar 3
print(ptree.search("rubicon"))  # Deve retornar 6
print(ptree.search("rome"))  # Deve retornar None
