# Dotfiles eXtreme

## How to use
Specify the Kickstart file when installing Fedora. Boot up a netinstall with this boot option:

```sh
inst.ks=http://git.io/v0NoL
```

My preferred way to set that up is:

1. [Download a netinstall image](https://getfedora.org/en/workstation/download/) and write it to a USB drive.
2. Open up `path/to/usb-drive/EFI/BOOT/grub.cfg` and add the boot option to the `linuxefi` line of one of the "Install Fedora" menu entries. You'll have something that looks like this:

```cfg
menuentry 'Install Fedora 23' --class fedora --class gnu-linux --class gnu --class os {
	linuxefi /images/pxeboot/vmlinuz inst.ks=http://git.io/v0NoL inst.stage2=hd:LABEL=FEDORA-WS-2 quiet
	initrdefi /images/pxeboot/initrd.img
}
```
