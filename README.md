# Diff Packages

Very small project for analyse your missing packages with the CRI (ING1).
This project concern distro with pacman as package manager.

## Installation

### Requierment

* pacman
* python3
* diff
* wget

### Run

Clone the repo and run the script
```bash
git clone https://github.com/mxmchdn/Diff-Packages.git

./get_missing_pkg.sh
```

Install missing packages (Skip AUR packages) (!!! Be careful with your system packages !!!)
```bash
sudo pacman -S --needed $(comm -12 <(pacman -Slq | sort) <(sort missing_pkg))
```
Example: I don't want to remove dmenu-manjaro
```bash
looking for conflicting packages...
:: openbsd-netcat and gnu-netcat are in conflict. Remove gnu-netcat? [y/N] y
:: dmenu and dmenu-manjaro are in conflict. Remove dmenu-manjaro? [y/N] N
error: unresolvable package conflicts detected
error: failed to prepare transaction (conflicting dependencies)
:: dmenu and dmenu-manjaro are in conflict
```
Solution is to go on missing_pkg and remove dmenu line.
```vim
dash
dconf
dkms
dmenu (remove this line)
docbook-xml
docbook-xsl
```

## About

You will find many differents files

* missing_version_pkg: (missing package and version conflict)
* missing_pkg: (missing package)
* Output/my_pkg: (list of your package)
* Output/my_pkg_version (list of your package version)

## Sources

* pacman: [ArchWiki - Tips_and_tricks#List_of_installed_packages](https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#List_of_installed_packages)
* [CRI packages](https://static.cri.epita.fr/pie/)

A la base je voulais juste faire des diff entre fichiers..
