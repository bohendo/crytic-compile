{ pkgs ? import (
    fetchTarball "https://github.com/NixOS/nixpkgs/archive/bf972dc380f36a3bf83db052380e55f0eaa7dcb6.tar.gz"
  ) {}
}:

pkgs.python39Packages.buildPythonPackage rec {
  pname = "mypy";
  version = "0.942";
  src = pkgs.python39Packages.fetchPypi {
    inherit pname version;
    sha256 = "sha256-F+RGSf7JLp+CECtIo797SlUQrQzSL6IaEEgmtdtJA+I=";
  };
  doCheck = false;
  propagatedBuildInputs = with pkgs.python39Packages; [
    mypy-extensions
    tomli
    types-setuptools
    typing-extensions
  ];
}
