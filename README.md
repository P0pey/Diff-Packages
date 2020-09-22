# Diff Packages

Very small project for analyse your missing packages with the CRI (ING1).
This project concern distro with pacman as package manager.

## Installation

### Requierment

* python3
* diff
* wget

### Run

Clone the repo and run the script
```shell=
git clone https://github.com/mxmchdn/Diff-Packages.git

./get_missing_pkg.sh
```

Install missing packages
```shell=
sudo pacman -S --needed - < missing_pk
```

## About

You will find many differents files

* missing_version_pkg: (missing package and version conflict)
* missing_pkg: (missing package)
* Output/my_pkg: (list of your package)
* Output/my_pkg_version (list of your package version)
