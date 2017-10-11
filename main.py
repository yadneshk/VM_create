#!/usr/bin/python3
#Script will ask about VM name, ram, disk size and etc


class create:

    def __init__(self):
        self.name=""
        self.ram=1024
        self.cpus=1
        self.disk_path="/var/lib/libvirt/images/"
        self.size=10
        self.bus="virtio"
        self.location="http:192.168.0.203/repos/fedora25/"
        self.net_adp="virbr0"

    def get_name(self):
        self.name=input("Enter name of VM: ")

    def get_ram(self):
        self.ram=int(input("Enter RAM size(MB): "))

    def get_cpus(self):
        self.cpus=int(input("Enter number of vcpus: "))

    def get_size(self):
        self.size=int(input("Enter size you want to allocate to VM(GiB): "))

    def final(self):
        print("virt-install "\
              " --name "+self.name+ \
              " --ram "+str(self.ram)+ \
              " --vcpus "+str(self.cpus)+ \
              " --disk path="+self.disk_path+self.name+".qcow2,bus="+self.bus+",size="+str(self.size)+ \
              " --location "+self .location+ \
              " --network bridge:"+str(self.net_adp))

if __name__ == '__main__':
    a = create()
    a.get_name()
    a.get_ram()
    a.get_cpus()
    a.get_size()
    a.final()
