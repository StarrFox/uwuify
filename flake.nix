{
  description = "uwuifys text";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts/";
    nix-systems.url = "github:nix-systems/default";
  };

  outputs = inputs @ {
    self,
    flake-parts,
    nix-systems,
    ...
  }:
    flake-parts.lib.mkFlake {inherit inputs;} {
      debug = true;
      systems = import nix-systems;
      perSystem = {
        pkgs,
        system,
        self',
        ...
      }: let
        python = pkgs.python311;

        pyproject = builtins.fromTOML (builtins.readFile ./pyproject.toml);

        packageName = "uwuify";
      in {
        packages.${packageName} = python.pkgs.buildPythonPackage {
          src = ./.;
          pname = packageName;
          version = pyproject.tool.poetry.version;
          format = "pyproject";
          pythonImportsCheck = [packageName];
          nativeBuildInputs = [python.pkgs.poetry-core];
          propagatedBuildInputs = [python.pkgs.click];
          nativeCheckInputs = [python.pkgs.pytestCheckHook];

          meta.mainProgram = packageName;
        };

        packages.default = self'.packages.${packageName};

        devShells.default = pkgs.mkShell {
          name = packageName;
          packages = with pkgs; [
            (poetry.withPlugins(ps: with ps; [poetry-plugin-up]))
            python
            just
            alejandra
            python.pkgs.black
            python.pkgs.isort
            python.pkgs.vulture
          ];
        };
      };
    };
}
