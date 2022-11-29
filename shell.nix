{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python39
    pkgs.poetry
  ];
  shellHook = ''
    source "$PWD/.venv/bin/activate"
    export PYTHONPATH="$PWD/.venv/lib/python3.9/site-packages"
  '';
}
