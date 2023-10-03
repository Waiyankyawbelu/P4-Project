# P4 Project for IoT Devices

**Title**: Integrated IoT devices uing P4 programming in SDN environment. <br>
**Tutor**: [Juan Pedro Muñoz Gea](https://personas.upct.es/perfil/juanp.gea) <br>
**Degree**: Telematics engineering, [Polytechnic University of Cartagena](https://www.upct.es/) <br>

## Introduction 

In this P4 Project, we have prepared use cases for IoT devices using P4 to help you understand how packets are processed in P4.

1. Drop, which is dropping any received traffic.
* [Drop](./Drop/)
2. Pass, which is forwarding any recived traffic to the destination.
* `Pass`**working on it**
3. Echo Server, which is checking whether the device can actively reply to traffic.
* [Echo Server](./Echo_server/)
4. L3 Forwarding, which is a slighty advanced function that acts on the packet based on a routing table.
* [L3_Forwarding](./L3_forwarding/)
5. Broadcast, which is commonly send the received packets on its network to get reply from the destination device.
* [Broadcast](./Broadcast/)


## P4 Documentation

The documentation for P4_16 and P4Runtime is available [here](https://p4.org/specs/)

All use cases in this repository use the v1model architecture, the documentation for which is available at:
1. The BMv2 Simple Switch target document accessible [here](https://github.com/p4lang/behavioral-model/blob/master/docs/simple_switch.md) talks mainly about the v1model architecture.
2. The include file `v1model.p4` has extensive comments and can be accessed [here](https://github.com/p4lang/p4c/blob/master/p4include/v1model.p4).

## Obtaining required softwer 

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

### `Release` VM images with P4 development tools (Option 2)

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

