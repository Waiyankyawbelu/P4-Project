#!/usr/bin/python

import os
import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.bmv2 import P4AP, P4Host
from mininet.node import RemoteController


def topology():
    'Create a network.'
    net = Mininet_wifi()

    info('*** Adding stations/hosts\n')
    h1 = net.addHost('h1', ip='192.168.1.2', cls=P4Host, mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', ip='192.168.2.2', cls=P4Host, mac="00:00:00:00:00:02")
    sta1 = net.addStation('sta1', ip='192.168.1.1', mac="00:00:00:00:00:03")
    sta2 = net.addStation('sta2', ip='192.168.2.1', mac="00:00:00:00:00:04")

    info('*** Adding P4APs\n')
    ap1 = net.addAccessPoint('ap1', cls=P4AP, json_path='build/drop.json', runtime_json_path='runtime/ap1-runtime.json', 
			     log_console = True, log_dir = os.path.abspath('logs'), log_file = 'ap1.log', pcap_dump = os.path.abspath('pcaps'))
    ap2 = net.addAccessPoint('ap2', cls=P4AP, json_path='build/drop.json', runtime_json_path='runtime/ap2-runtime.json', 
			     log_console = True, log_dir = os.path.abspath('logs'), log_file = 'ap2.log', pcap_dump = os.path.abspath('pcaps'))

    net.configureWifiNodes()

    info('*** Creating links\n')
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap2)
    net.addLink(h1, ap1)
    net.addLink(h2, ap2)

    info('*** Starting network\n')
    net.start()

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
