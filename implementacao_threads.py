import threading

def soma_sublista(sublista, resultado, indice):
	resultado[indice] = sum(sublista)

def main(lista, n_threads):
	# Dividir a lista em n_threads partes
	tamanho = len(lista)
	partes = [lista[i * tamanho // n_threads: (i + 1) * tamanho // n_threads] for i in range(n_threads)]

	# Array para armazenar os resultados das threads
	resultado = [0] * n_threads

	# Criar e iniciar as threads
	threads = []
	for i in range(n_threads):
		thread = threading.Thread(target=soma_sublista, args=(partes[i], resultado, i))
		threads.append(thread)
		thread.start()

	# Esperar as threads terminarem
	for thread in threads:
		thread.join()

	# Agregar os resultados das threads
	soma_total = sum(resultado)
	print(f"Soma total: {soma_total}")

if __name__ == "__main__":
	lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	n_threads = 3

	# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
	# n_threads = 5

	# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	# n_threads = 4
	main(lista, n_threads)
