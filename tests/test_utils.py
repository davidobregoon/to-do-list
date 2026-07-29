from src.utils import obtener_indice_usuario


def test_obtener_indice_usuario(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")

    resultado = obtener_indice_usuario()

    assert resultado == 2


def test_obtener_indice_usuario_invalido(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "abc")

    resultado = obtener_indice_usuario()

    assert resultado is None
