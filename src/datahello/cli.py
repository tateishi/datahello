from fire import Fire

from . import core


def hello():
    print("Hello, World.")


def datahello_main():
    for whom in core.to_whom():
        print(f"Hello, {whom}")


def datahello():
    Fire(datahello_main)


def resource_main():
    print(core.resource_dir())


def resource():
    Fire(resource_main)
