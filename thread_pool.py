"""
Taller 4 - Patrones Concurrentes
Autor: Angie Xiomara Fuentes Montañez
Fecha: (15/11/2025)
"""
import time, random, queue
from concurrent.futures import ThreadPoolExecutor
import threading


lock = threading.Lock()

clientes = ["Maria", "Leo", "Pablo", "Isabela"]
cola = queue.Queue(maxsize=5)
cant = {"producido": 0, "consumido": 0}


def crear_pedido(id_prod, num):
    """Genera un pedido con datos aleatorios.
    Args:
        num (int): Número secuencial del pedido.
    """

    return {
        "id_pedido": f"P{id_prod}-{num}",
        "cliente": random.choice(clientes),
        "precio": round(random.uniform(1000, 6000), 2),
        "producto": random.choice(["Sandia", "Pera", "Manzana", "Uvas"])
    }


def productor(id_prod):
    """Los productores crean pedidos y los añaden a la cola."""

    print(f"Iniciando el procesador de pedidos {id_prod}")

    for i in range(3):
        time.sleep(random.uniform(0.3, 1.2))
        pedido = crear_pedido(id_prod, i)
        cola.put(pedido)

        with lock:
            cant["producido"] += 1
        print(f"[Productor {id_prod}] produjo: {pedido}")

    print(f"[Productor {id_prod}] finalizó.")


def consumidor(id_cons):
    """Extrae elementos de la cola y los procesa."""

    print(f"Iniciando el consumidor {id_cons}")

    while True:
        try:
            pedido = cola.get(timeout=2)
        except queue.Empty:
            break

        print(f"[Consumidor {id_cons}] procesando pedido {pedido['id_pedido']}")
        time.sleep(random.uniform(0.5, 1.2))

        with lock:
            cant["consumido"] += 1

        cola.task_done()

    print(f"[Consumidor {id_cons}] finalizó.")


def main():
    """Crea productores y consumidores usando ThreadPoolExecutor."""

    inicio = time.time()

    with ThreadPoolExecutor(max_workers=7) as executor:

        for i in range(3):
            executor.submit(productor, i)

        for j in range(4):
            executor.submit(consumidor, j)

    fin = time.time()

    print("Resultados:")
    print(f"Tiempo total: {fin-inicio:.2f} segundos")
    print(f"Pedidos producidos: {cant['producido']}")
    print(f"Pedidos consumidos: {cant['consumido']}")


if __name__ == "__main__":
    main()
