#!/bin/sh

log_file=lvinstall.log

function check {
	if  yum list installed "$@" >/dev/null 2>&1 
	then
		#echo "if"
		echo "$@ already installed."
	else
		echo "$@ is installing"
		dnf install $@ -y
	fi	
}

#function installation for fedora
function for_fedora { 
	check libvirt
	check virt-install
	check virt-manager
} 


distro=$(lsb_release -i | cut -f 2)
if [ "$distro" == "Fedora" ]
	then
	for_fedora hello_fedora
elif [ "$distro" == "Ubuntu" ]
	then 
	for_ubuntu hello_ubuntu
fi
