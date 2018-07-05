from entity import Count


INVALID_CHARS = (
        '|', '_', '[', ']', '(', ')', ',', '.', '?', '!', ';', ':', '-'
    )


def _sanitize(token):
    return ''.join(c for c in token.strip().lower() if c not in INVALID_CHARS)


def simple_counter(loader):
    data = Count()
    for token in loader:
        data.add(_sanitize(token))

    return data
