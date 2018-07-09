from logging import getLogger

from entity import Count


logger = getLogger("wordcounter")


INVALID_CHARS = (
    '/', '\\', '|', '_', '[', ']', '(', ')', ',', '.', '?', '!', ';', ':', '-'
)

INVALID_END_CHARS = (
    '`', "'", '"', "-",
)

def _is_valid(token):
    if len(token) == 0:
        logger.warn("empty token")
        return False

    elif token.endswith(INVALID_CHARS + INVALID_END_CHARS):
        logger.warn("%s is an invalid token", token)
        return False

    return True


def _remove_invalid_end_chars(token):
    while token.endswith(INVALID_END_CHARS):
        token = token[:-1]

    while token.startswith(INVALID_END_CHARS):
        token = token[1:]

    return token


def _sanitize(token):
    _tkn = ''.join(c for c in token.strip().lower() if c not in INVALID_CHARS)
    return _remove_invalid_end_chars(_tkn)


def simple_counter(loader, data=None):
    data = Count() if data is None else data
    for token in loader:
        sanitized = _sanitize(token)
        if _is_valid(sanitized):
            data.add(sanitized)

    return data
