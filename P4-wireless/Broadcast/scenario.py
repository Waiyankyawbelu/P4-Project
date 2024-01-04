#!/usr/bin/python



import os
import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.bmv2 import P4AP, P4Host
from mininet.node import RemoteController


def topology(remote_controller):
    'Create a network.'
    net = Mininet_wifi()

    info('*** Adding stations/hosts\n')
    sta1 = net.addStation('sta1', ip='192.168.1.1', mac="08:00:00:00:01:11")
    sta2 = net.addStation('sta2', ip='192.168.2.2', mac="08:00:00:00:02:22")
    sta3 = net.addStation('sta3', ip='192.168.3.3', mac="08:00:00:00:03:33")

    args1 = dict()
    if not remote_controller:
        path = os.path.dirname(os.path.abspath(__file__))
        log_console = True
        log_dir = os.path.abspath('logs')
        log_file = 'ap1.log'
        pcap_dump = os.path.abspath('pcaps')
        json_file = path + '/build/broadcast.json'
        config1 = path + '/build/ap1-runtime.json'
        args1 = {'json': json_file, 'switch_config': config1, 'log_console': log_console,
        'log_dir': log_dir, 'log_file' : log_file, 'log_file' : log_file, 'pcap': pcap_dump}
        

    info('*** Adding P4APs\n')
    ap1 = net.addAccessPoint('ap1', cls=P4AP, netcfg=True, **args1)

    if remote_controller:
        info('*** Adding Controller\n')
        net.addController('c0', controller=RemoteController)

    net.configureWifiNodes()

    info('*** Creating links\n')
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)
    

    info('*** Starting network\n')
    net.start()
    if not remote_controller:
        net.staticArp()

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    remote_controller = True if '-r' in sys.argv else False
    topology(remote_controller)
