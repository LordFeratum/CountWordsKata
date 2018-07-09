from counter import simple_counter


def test_simple_counter():
    loader = ["this", "is", "a", "test"]
    data = simple_counter(loader)
    expected = {
        'this': 1,
        'is': 1,
        'a': 1,
        'test': 1
    }
    for key, count in data.items():
        assert expected[key] == count


def test_complex_simple_counter():
    loader = [
        "theres'", "'theres", "theres!", "theres?", "--theres", "theres!--"
    ]
    data = simple_counter(loader)
    assert data['theres'] == 6


def test_accumulate_simple_counter():
    loader_1 = [
        "Sweet", "home", "Alabama!",
        "where", "the", "skies", "are", "so", "blue!"
    ]
    loader_2 = [
        "Sweet", "home", "Alabama!",
        "Lord,", "I'm", "coming", "home", "to", "you"
    ]
    expected = {
        'sweet': 2,
        'home': 3,
        'alabama': 2,
        'where': 1,
        'the': 1,
        'skies': 1,
        'are': 1,
        'so': 1,
        'blue': 1,
        'lord': 1,
        "i'm": 1,
        'coming': 1,
        'to': 1,
        'you': 1
    }
    data = simple_counter(loader_1)
    data = simple_counter(loader_2, data=data)

    for key, count in data.items():
        assert expected[key] == count
