#!/usr/bin/python3
#Script will ask about VM name, ram, disk size and etc
import os

class create:

    def __init__(self):
        self.check_packages()
        self.name=""
        self.ram=1024
        self.cpus=1
        self.disk_path="/var/lib/libvirt/images/"
        self.size=10
        self.bus="virtio"
        self.location="http://172.22.26.203/repos/fedora25/"
        self.net_adp="virbr0"

    def check_packages(self):
        os.system("sshpass -p minisat ssh root@172.22.26.201 < test")
        print("Prerequisite Check \n donex")
        #os.system('ls')

    def get_name(self):
        self.name=input("Enter name of VM: ")

    def get_ram(self):
        self.ram=int(input("Enter RAM size(MB): "))

    def get_cpus(self):
        self.cpus=int(input("Enter number of vcpus: "))

    def get_size(self):
        self.size=int(input("Enter size you want to allocate to VM(GiB): "))

    def get_ksfile(self):
        self.ksfile=input("Enter the path of kickstart config file in your server: ")

    def get_ksdevice(self):
        self.ksdevice=input("Enter the network interface to be used during installation: ")

    def get_ipaddress(self):
        self.ipaddress=input("Enter the ipaddress to be assigned to operating system: ")

    def get_netmask(self):
        self.netmask=input("Enter the subnet mask to be assigned to operating system: ")

    def get_gateway(self):
        self.gateway=input("Enter the gateway to be assigned to operating system: ")

    def get_dns(self):
        self.dns=input("Enter the dns to be assigned to operating system: ")

    def final(self):
        #os.system('ls')
        self.finalcmd=str("virt-install "
                +"--name "+self.name
                +"--ram "+str(self.ram)
                +" --vcpus "+str(self.cpus)
                +" --disk path="+self.disk_path+self.name+".qcow2,bus="+self.bus+",size="+str(self.size)
                +" --location "+self.location
                +" --extra-args="
                +"'ks="+str(self.ksfile)
                +" ksdevice="+str(self.ksdevice)
                +" ip="+str(self.ipaddress)
                +" netmask="+str(self.netmask)
                +" gateway="+str(self.gateway)
                +" dns="+str(self.dns)
                +"' --network bridge:"+str(self.net_adp))
        print(self.finalcmd)
        #os.system(self.finalcmd)

if __name__ == '__main__':
    vm = create()
    vm.get_name()
    vm.get_ram()
    vm.get_cpus()
    vm.get_size()
    vm.get_ksfile()
    vm.get_ksdevice()
    vm.get_ipaddress()
    vm.get_netmask()
    vm.get_gateway()
    vm.get_dns()
    vm.final()
