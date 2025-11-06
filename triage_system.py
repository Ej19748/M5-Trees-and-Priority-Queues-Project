import heapq


class TriageSystem:
    _arrival_counter = 0

    def __init__(self):
        self._queue = []

    @classmethod
    def _next_arrival_order(cls):
        current = cls._arrival_counter
        cls._arrival_counter += 1
        return current

    def add_patient(self, name, severity):
        if not name or not isinstance(name, str) or name.strip() == "":
            raise ValueError("Patient name must be a non-empty string")

        if not isinstance(severity, int) or severity < 1 or severity > 5:
            raise ValueError("Severity must be an integer between 1 and 5")

        arrival_order = self._next_arrival_order()
        heapq.heappush(self._queue, (-severity, arrival_order, name, severity))

    def process_next(self):
        if self.is_empty():
            return None

        _, _, name, severity = heapq.heappop(self._queue)
        return (name, severity)

    def peek_next(self):
        if self.is_empty():
            return None

        _, _, name, severity = self._queue[0]
        return (name, severity)

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def clear(self):
        self._queue.clear()
