class Nodo:
	def __init__(self, valor):
		self.valor = valor  # Asigna el valor al nodo
		self.izquierdo = None  # Inicializa el hijo izquierdo como None
		self.derecho = None  # Inicializa el hijo derecho como None

def insertar_en_bst(raiz, valor):
	if raiz is None:  # Si la raíz es None, crea un nuevo nodo con el valor
		return Nodo(valor)
	else:
		if valor < raiz.valor:  # Si el valor es menor que el valor de la raíz
			raiz.izquierdo = insertar_en_bst(raiz.izquierdo, valor)  # Inserta en el subárbol izquierdo
		else:  # Si el valor es mayor o igual que el valor de la raíz
			raiz.derecho = insertar_en_bst(raiz.derecho, valor)  # Inserta en el subárbol derecho
	return raiz  # Retorna la raíz actualizada

def lista_a_bst(lista):
	raiz = None  # Inicializa la raíz como None
	for valor in lista:  # Itera sobre cada valor en la lista
		raiz = insertar_en_bst(raiz, valor)  # Inserta el valor en el BST
	return raiz  # Retorna la raíz del BST construido

def imprimir_bst(raiz):
	if raiz is not None:  # Si la raíz no es None
		imprimir_bst(raiz.izquierdo)  # Imprime el subárbol izquierdo
		print(raiz.valor, end=' ')  # Imprime el valor del nodo actual
		imprimir_bst(raiz.derecho)  # Imprime el subárbol derecho

# Definición de la lista de elementos
lista = [100, 20, 33, 45, 59, 26, 7, 9, 50, 23, 101, 123, 2, 3, 6, 8, 20]  # Lista de elementos a insertar en el BST

# Convertir la lista en un árbol binario de búsqueda
arbol = lista_a_bst(lista)  # Construye el BST a partir de la lista

# Imprimir el árbol binario de búsqueda en orden
imprimir_bst(arbol)  # Imprime los valores del BST en orden ascendente
