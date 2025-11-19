"""
Taller 4 - Patrones Concurrentes
Autor: Angie Xiomara Fuentes Montañez
Fecha: (18/11/2025)
"""

import threading, queue, time, random

lock = threading.Lock()

clientes = ["Maria", "Leo", "Pablo", "Isabela"]
cola = queue.Queue(maxsize=5)
cant = {"producido": 0, "consumido": 0}

def crear_pedido(id_prod, num):
    """Se genera in pedido con datos especificos.
    Args:
        num (int): Numero secuencial del pedido. """
    
    return{
        "id_pedido": f"P{id_prod}-{num}",
        "cliente": random.choice(clientes),
        "precio": round(random.uniform(700, 3000), 2),
        "producto": random.choice(["Sandia", "Pera", "Manzana", "Uvas"])
    }


def productor(id_prod):
    """Los productores crean pedidos y se añaden a la cola.
    Args:
        id_prod(int): El id del productor asignado.
    """

    print(f"Iniciando el productor {id_prod}")

    for i in range(3):
        time.sleep(random.uniform(0.3, 1.2))
        pedido = crear_pedido(id_prod, i)
        cola.put(pedido)

        with lock:
            cant["producido"] += 1
        print(f"[Productor {id_prod}] produjo: {pedido}")
    print(f"[Productor {id_prod}] finalizó.")


def consumidor(id_cons):
    """Extrae elementos de la cola y los procesa.
    Args:
        id_cons(int): id del consumidor asignado."""
    
    print(f"Iniciando el consumidor {id_cons}")
    while True:
        try:
            pedido = cola.get(timeout=2)
        except queue.Empty:
            break
        print(f" [Consumidor {id_cons}] procesando pedido {pedido['id_pedido']}")
        time.sleep(random.uniform(0.5, 1.2))
        with lock:
            cant["consumido"] += 1
        cola.task_done()
    print(f" [Consumidor {id_cons}] finalizó.")

def main():
    """Crea productores, consumidores y mide el tiempo total."""

    inicio = time.time()

    productores = [threading.Thread(target=productor, args=(i,)) for i in range(3)]
    consumidores = [threading.Thread(target=consumidor, args=(j,)) for j in range(4)]

    for h in productores: h.start()
    for h in consumidores: h.start()
    for h in productores + consumidores: h.join()

    fin = time.time()

    print("Resultados:")
    print(f"Tiempo total: {fin - inicio:.2f} segundos")
    print(f"Pedidos producidos: {cant['producido']}")
    print(f"Pedidos consumidos: {cant['consumido']}")

if __name__ == "__main__":
    main()