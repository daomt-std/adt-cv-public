import random
from collections import deque
from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    source: deque
    dest: deque
    period: int
    spread_factor: float = 0.0
    timer: int = 0


def get_delay(period: int, spread_factor: float) -> int:
    return int(random.gauss(period, period * spread_factor))



def worker_tick(worker: Worker) -> None:
    if worker.timer > 0:
        worker.timer -= 1
        return
    if len(worker.source) == 0:
        return
    worker.dest.append(worker.source.popleft())
    worker.timer = get_delay(worker.period, worker.spread_factor)



def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"Aktuální čas: {time} s, {time // 3600} h")
    for name, queue in queues:
        print(f"{name}: ({len(queue)})")



def main() -> None:
    people_number = 1000
    people_in_the_city = deque(list(range(people_number)))

    # 1. Vytvoření front
    gate_queue = deque()
    vege_queue = deque()
    cashier_queue = deque()
    final_queue = deque()

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe: list[tuple[str, deque]] = [
        ("Street", people_in_the_city),
        ("Gate", gate_queue),
        ("Vege", vege_queue),
        ("Cashier", cashier_queue),
        ("Final", final_queue)
    ]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30  # Každých 30s přijde někdo z ulice
    gate_m = 15  # Gate keeper každého odbavuje 5s
    vege_m = 45  # Vážení zeleniny trvá 45s
    final_m = 2 * 60  # Pokladna zabere 2 minuty

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    street_worker = Worker("Street Worker", people_in_the_city, gate_queue, day_m, 0.1)
    gate_worker = Worker("Gate Worker", gate_queue, vege_queue, gate_m, 0.2)
    vege_worker = Worker("Vege Worker", vege_queue, cashier_queue, vege_m, 0.5)
    cashier_worker = Worker("Cashier Worker", cashier_queue, final_queue, final_m, 0.3)
    cashier2_worker = Worker("Cashier 2 Worker", cashier_queue, final_queue, final_m, 0.2)
    # 3. Hlavní smyčka simulace
    print_snapshot(0, queues_to_observe)

    for time in range(7201):
        worker_tick(street_worker)
        worker_tick(gate_worker)
        worker_tick(vege_worker)
        worker_tick(cashier_worker)

        if time % 60 == 0:
            print_snapshot(time, queues_to_observe)
            print()

if __name__ == "__main__":
    main()
