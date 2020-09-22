#! /bin/sh

# Get CRI packages list
wget https://ipxe.pie.cri.epita.fr/cri-pxe-images.s3.cri.epita.fr/pie-archlinux-pkglist.txt

# Get your packages list
sudo pacman -Q > my_pkg

# Run diff files
diff pie-archlinux-pkglist.txt my_pkg > diff

# Get diff_cleaner python script
wget https://raw.githubusercontent.com/mxmchdn/Diff-Packages/master/diff_cleaner.py
# remove if already exists
rm diff_cleaner.py.*

# Analyse it and get missing packages
python3 diff_cleaner.py

# move files
mkdir Output
mv diff Output/
mv my_pkg Output/
mv pie-archlinux-pkglist.txt Output/
