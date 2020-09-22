#! /bin/sh

# Remove Output folder
rm -rf Output/

# Get CRI packages list
wget https://ipxe.pie.cri.epita.fr/cri-pxe-images.s3.cri.epita.fr/pie-archlinux-pkglist.txt

# Get your packages list
sudo pacman -Q > my_pkg_version

# Run diff files
diff pie-archlinux-pkglist.txt my_pkg_version > diff

# Get a tiny list of my package
sudo pacman -Qqe > my_pkg

# Clean diff file
python3 diff_cleaner.py

# Second diff
diff missing_pkg my_pkg > diff2

# Analyzing really missing packages
python3 missing.py

# move files
mkdir Output
mv diff Output/
mv diff2 Output/
mv my_pkg* Output/
mv pie-archlinux-pkglist.txt Output/
