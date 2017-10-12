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
        self.name=input("Enter name of VM: ")
        return self.name

    def get_ram(self):
        return(input("Enter RAM size(MiB): "))

    def get_cpus(self):
        return(input("Enter number of vcpus: "))

    def get_size(self):
        return(input("Enter size you want to allocate to VM(GiB): "))

    def get_ksfile(self):
        return(input("Enter the path of kickstart config file in your server: "))

    def get_ksdevice(self):
        return(input("Enter the network interface to be used during installation: "))

    def get_ipaddress(self):
        return(input("Enter the ipaddress to be assigned to operating system: "))

    def get_netmask(self):
        return(input("Enter the subnet mask to be assigned to operating system: "))

    def get_gateway(self):
        return(input("Enter the gateway to be assigned to operating system: "))

    def get_dns(self):
        return(input("Enter the dns to be assigned to operating system: "))

    def final(self):
        #os.system('ls')
        self.finalcmd=str("virt-install "
                +" --name "+self.get_name()
                +" --ram "+self.get_ram()
                +" --vcpus "+self.get_cpus()
                +" --disk path="+self.disk_path+self.name+".qcow2,bus="+self.bus+",size="+self.get_size()
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
        os.system(self.finalcmd)

if __name__ == '__main__':
    vm = create()
    vm.final()
