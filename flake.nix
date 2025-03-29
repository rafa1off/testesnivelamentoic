{
  description = "teste de nivelamento";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      flake-utils,
      nixpkgs,
      self,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };

        name = "testeic";

        python = pkgs.python313;

        nativeBuildInputs = [ python ];

        buildInputs = with pkgs; [
          (python.withPackages (
            pypkgs: with pypkgs; [
              beautifulsoup4
              pandas
              zipfile2
              requests
              urllib3
            ]
          ))
          pyright
        ];
      in
      {
        devShells.default = pkgs.mkShell {
          inherit
            name
            buildInputs
            ;
        };

        packages.default = python.pkgs.buildPythonApplication {
          pname = name;
          version = "0.0.0";

          src = ./.;

          inherit nativeBuildInputs buildInputs;
        };
      }
    );
}
