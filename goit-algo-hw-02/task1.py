# Код виконується, використано клас Queue з модуля queue в Python.
# Програма автоматично генерує нові заявки, додає їх до черги, а потім послідовно видаляє з черги.
# Структура коду відповідає наданому псевдокоду.


import time
from queue import Queue


def call_center() -> None:
    request_queue = Queue()
    request_id = 0

    def generate_request():
        nonlocal request_id
        request_id += 1
        request = {"id": request_id, "data": f"Request {request_id}"}
        request_queue.put(request)
        print(f"Generated request: {request}")

    def process_request():
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Processing request: {request}")
            return request
        else:
            print("No requests to process.")
            return None

    print("System started. Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
            generate_request()
            time.sleep(1)
            request = process_request()
            if request and request.get("id") < 10:
                continue
            else:
                print(f"request_queue size: {request_queue.qsize()}")
                break

    except KeyboardInterrupt:
        print("\nSystem stopped by user.")


if __name__ == "__main__":
    call_center()
