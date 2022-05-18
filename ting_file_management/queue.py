from collections import deque


class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        # adaptado de: https://www.codingem.com/what-is-a-fifo-queue/
        self.queue = deque([])

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index > (self.__len__() - 1):
            raise IndexError
        else:
            print(self.queue)
            return self.queue[index]
