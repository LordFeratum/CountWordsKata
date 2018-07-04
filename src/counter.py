from collections import defaultdict


class Counter:
    invalid_chars = (
        '|', '_', '[', ']', '(', ')', ',', '.', '?', '!', ';', ':', '-'
    )

    def __init__(self, loader):
        self._data = defaultdict(lambda: 0)
        self._loader = loader

    @property
    def result(self):
        return self._data

    def count(self):
        for line in self._loader:
            self._process(line)

        return self._data

    def _process(self, line):
        for token in self._tokenize(line):
            self._data[token] += 1

    def _tokenize(self, line):
        for token in line.split():
            yield self._sanitize(token)

    def _sanitize(self, token):
        return ''.join(
            c for c in token.strip().lower() if c not in self.invalid_chars)
