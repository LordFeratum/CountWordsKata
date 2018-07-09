from collections import defaultdict


class Count:
    def __init__(self):
        self._count = defaultdict(lambda: 0)

    def add(self, token):
        self._count[token] += 1

    def items(self):
        for token, count in self._count.items():
            yield token, count

    def __getitem__(self, key):
        return self._count.get(key, 0)

    def __repr__(self):
        total = len(self._count.keys())
        return f'<Count elements={total}>'
