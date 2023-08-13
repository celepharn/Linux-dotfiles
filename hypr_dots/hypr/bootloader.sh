#!/bin/sh
# this is a script to set keep refind working
sudo pacman -Syu
dro=$(ls /efi/ | grep 0e)
dri=$(ls /efi/"$dro" | grep lts)
echo "Copying /efi/$dro/$dri/initrd and /efi/$dro/$dri/linux to /efi/EFI/eos."
sudo cp /efi/"$dro"/"$dri"/initrd /efi/EFI/eos/initrd
sudo cp /efi/"$dro"/"$dri"/linux /efi/EFI/eos/linux
echo "Done. You should be fine."
