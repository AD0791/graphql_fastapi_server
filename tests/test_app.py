from app import __version__, __Project__


def test_version():
    assert __version__ == '0.1.0'


def test_project() -> None:
    assert __Project__ == "GraphQl services"
