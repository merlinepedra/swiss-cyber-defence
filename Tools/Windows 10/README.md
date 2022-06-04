# Windows 10


# Installation

## Create Bootable USB Stick on MacOS

For Boot via GPT (Newer Devices)
`diskutil eraseDisk MS-DOS “WINDOWS10” GPT /dev/disk4`

For Boot via MBR (Older Devices)
`diskutil eraseDisk MS-DOS “WINDOWS10” GPT /dev/disk4`

`rsync -vha --exclude=sources/install.wim /Volumes/CCCOMA_X64FRE_EN-_DV9/* /Volumes/WIN10`

`wimlib-imagex split /Volumes//Volumes/CCCOMA_X64FRE_EN-GB_DV9/sources/install.wim /Volumes/W10/sources/install.swm 3000`