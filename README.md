# P4 Project for IoT Devices

**Title**: P4-Enabled Programmable Networking for Enhancing IoT Communication Efficiency <br>
**Tutor**: [Juan Pedro Muñoz Gea](https://personas.upct.es/perfil/juanp.gea), **Tutor**: [Elans Grabs](https://ortus.rtu.lv/science/en/experts/1537) <br>
**Degree**: Telematics engineering, [Polytechnic University of Cartagena](https://www.upct.es/) <br>
**Degree**: Engineering Science in Telecommunications [Riga Technical University](https://www.rtu.lv/en)

## Introduction 

In this P4 Project, we have prepared use cases for IoT devices using P4 to help you understand how packets are processed in P4.

1. Drop, which is dropping any received traffic.
* [Drop](./P4/Drop/)
* [Drop(Wireless)](./P4-wireless/Drop/)
2. Pass, which is forwarding any recived traffic to the destination.
* [Pass](./P4/Pass/)
* [Pass(Wireless)](./P4-wireless/Pass/)
3. Echo Server, which is checking whether the device can actively reply to traffic.
* [Echo Server](./P4/Echo_server/)
* [Echo Server(Wireless)](./P4-wireless/Echo_Server/)
4. L3 Forwarding, which is a slighty advanced function that acts on the packet based on a routing table.
* [L3 Forwarding](./P4/L3_forwarding/)
* [L3 Forwarding(Wireless)](./P4-wireless/L3_Forwarding_wifi/)
5. Broadcast, which is commonly send the received packets on its network to get reply from the destination device.
* [Broadcast](./P4/Broadcast/)
* [Broadcast(Wireless)](./P4-wireless/Broadcast/)


## P4 Documentation

The documentation for P4_16 and P4Runtime is available [here](https://p4.org/specs/).

All use cases in this repository use the v1model architecture, the documentation for which is available at:
1. The BMv2 Simple Switch target document accessible [here](https://github.com/p4lang/behavioral-model/blob/master/docs/simple_switch.md) talks mainly about the v1model architecture.
2. The include file `v1model.p4` has extensive comments and can be accessed [here](https://github.com/p4lang/p4c/blob/master/p4include/v1model.p4).

## Obtaining required software 

To evaluate the use cases, you have two options. You can either create a virtual machine and manually install several dependencies, 
or you can use a pre-configured virtual machine that already has all the necessary software installed.

### To install P4 development tools on an existing system (Option 1)

- Install [Vagrant](https://vagrantup.com) and [VirtualBox](https://virtualbox.org)
- Clone the repository
- Before proceeding, ensure that your system has at least 12 Gbytes of free disk space, otherwise the installation can fail in unpredictable ways.
- `cd vm-ubuntu-20.04`
- `vagrant up` - The time for this step to complete depends upon your computer and Internet access speeds. 
- When the machine reboots, you should have a graphical desktop machine with the required software pre-installed.  There are two user accounts on the VM, `vagrant` (password `vagrant`) and `p4` (password `p4`).  The account `p4` is the one you are expected to use.
- You can see the installation steps [here](https://github.com/jafingerhut/p4-guide/blob/master/bin/README-install-troubleshooting.md#quick-instructions-for-successful-install-script-run).

### **Release** VM images with P4 development tools (Option 2)

There are instructions and scripts in another Github repository that can, starting from a freshly installed Ubuntu 20.04 or 22.04 Linux system with enough RAM and free disk space, install all of the necessary P4 development tools to run the exercises in this repository.  You can find those instructions and scripts [here](https://github.com/jafingerhut/p4-guide/blob/master/bin/README-install-troubleshooting.md).

For our project, we selected 'option 2' and utilized the 'Release' VM images (dated '2023-Aug-01') with the Ubuntu 20.04 operating system. We conducted testing on both Linux and Windows operating systems, as shown in the table below.

| Date published | Operation system | Development VM Image Link | REAMME link | Tested working on Linux | Tested working on Windows |
| :------------: | :--------------: | :-----------------------: | :----------:| :---------------------: | :-----------------------: |
| 2023-Aug-01 | Ubuntu 20.04 | [3.0 GByte VM image](https://drive.google.com/file/d/1_1CCNnJeQRpAfhTpw-m2LZ2T97QWgKp8/view?usp=sharing) | [README](https://drive.google.com/file/d/1vBeB_ls4QWxwxT0ruayX5nTXmVN0y7us/view?usp=sharing) | Combo 1 | Combo 2 |

Version combinations I have used above for testing VM image:

| Combination id | Opearting system | VM software |
| :------------: | :--------------: | :---------: |
| Combo 1 | Ubuntu 22.04.2 LTS | Virtualbox 7.0 |
| Combo 2 | Windows 11 Enterprise | Virtualbox 7.0 |

## References

- [Mininet](https://github.com/mininet/mininet)
- [P4.org](https://p4.org/)
- [Advanced Topic in Communication Networks **ETH Zurich**](https://video.ethz.ch/lectures/d-itet/2022/autumn/227-0575-00L/c1df0f1b-d89b-4328-b9d7-7dfd26a5bb46.html) 