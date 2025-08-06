{
  description = "Python dev flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };
  outputs =
    { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShell.x86_64-linux = pkgs.mkShell {
        buildInputs = with pkgs; [
          python313
          python313Packages.pyls-flake8
          python313Packages.black
          hy
        ];
      };
    };
}
