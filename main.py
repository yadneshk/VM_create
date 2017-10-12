#!/usr/bin/python3
#Script will ask about VM name, ram, disk size and etc
import os

class create:

    def __init__(self):
        self.check_packages()
        self.disk_path="/var/lib/libvirt/images/"
        self.bus="virtio"
        self.location="http://172.22.26.203/repos/fedora25/"
        self.net_adp="virbr0"
        
    def check_packages(self):
        os.system("./libvirt.sh")
        print("Prerequisite Check \n donex")

    def get_name(self):
        name=input("Enter name of VM: ")
        return name

    def get_ram(self):
        ram=input("Enter RAM size(MiB): ")
        return ram

    def get_cpus(self):
        cpus=input("Enter number of vcpus: ")
        return cpus

    def get_size(self):
        size=input("Enter size you want to allocate to VM(GiB): ")
        return size

    def get_ksfile(self):
        ksfile=input("Enter the path of kickstart config file in your server: ")
        return ksfile

    def get_ksdevice(self):
        ksdevice=input("Enter the network interface to be used during installation: ")
        return ksdevice

    def get_ipaddress(self):
        ipaddress=input("Enter the ipaddress to be assigned to operating system: ")
        return ipaddress

    def get_netmask(self):
        netmask=input("Enter the subnet mask to be assigned to operating system: ")
        return netmask

    def get_gateway(self):
        gateway=input("Enter the gateway to be assigned to operating system: ")
        return gateway

    def get_dns(self):
        dns=input("Enter the dns to be assigned to operating system: ")
        return dns

    def final(self):
        #os.system('ls')
        self.finalcmd=str("virt-install "
                +" --name "+self.get_name()
                +" --ram "+self.get_ram()
                +" --vcpus "+self.get_cpus()
                +" --disk path="+self.disk_path+".qcow2,bus="+self.bus+",size="+self.get_size()
                +" --location "+self.location
                +" --extra-args="
                +"'ks="+self.get_ksfile()
                +" ksdevice="+self.get_ksdevice()
                +" ip="+self.get_ipaddress()
                +" netmask="+self.get_netmask()
                +" gateway="+self.get_gateway()
                +" dns="+self.get_dns()
                +"' --network bridge:"+self.net_adp)
        print(self.finalcmd)
        #os.system(self.finalcmd)

if __name__ == '__main__':
    vm = create()
    vm.final()
