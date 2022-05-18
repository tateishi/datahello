def foo():
    return "foo"


def to_whom():
    from importlib.resources import files

    path = files("datahello") / "data/to_whom.txt"
    data = path.read_text().split()
    return data


def resource_dir():
    from importlib.resources import files

    path = files("datahello")
    return path
