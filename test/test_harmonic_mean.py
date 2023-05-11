import sys

from termcolor import colored

from imppkg.harmony import main



def test_harmony_happy_path(monkeypatch, capsys):
    inputs = ["1", "4", "4"]
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)
    main()
    expected_value = 2.0
    assert capsys.readouterr().out.strip() == colored(
        expected_value,
        "red",
        "on_yellow",
        attrs = ["bold"]
    )


def test_harmony_no_input(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["harmony"])
    main()
    expected_value = 0.0
    assert capsys.readouterr().out.strip() == colored(
        expected_value,
        "red",
        "on_yellow",
        attrs = ["bold"]
    )


def test_harmony_bad_input(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["harmony", "1mbad"])
    main()
    expected_value = 0.0
    assert capsys.readouterr().out.strip() == colored(
        expected_value,
        "red",
        "on_yellow",
        attrs = ["bold"]
    )
