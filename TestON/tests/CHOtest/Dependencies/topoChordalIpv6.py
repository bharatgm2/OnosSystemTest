#!/usr/bin/python
"""
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Host, RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections
from mininet.node import ( UserSwitch, OVSSwitch, IVSSwitch )

class dualStackHost( Host ):
    def config( self, v6Addr='1000:1/64', **params ):
        r = super( Host, self ).config( **params )
        intf = self.defaultIntf()
        self.cmd( 'ip -6 addr add %s dev %s' % ( v6Addr, intf ) )
        return r

class chordalTopo( Topo ):

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        s1 = self.addSwitch( 's1', dpid='1000000000000001' )
        s2 = self.addSwitch( 's2', dpid='1000000000000002')
        s3 = self.addSwitch( 's3', dpid='1000000000000003')
        s4 = self.addSwitch( 's4', dpid='1000000000000004')
        s5 = self.addSwitch( 's5', dpid='1000000000000005')
        s6 = self.addSwitch( 's6', dpid='1000000000000006')
        s7 = self.addSwitch( 's7', dpid='1000000000000007')
        s8 = self.addSwitch( 's8', dpid='1000000000000008')
        s9 = self.addSwitch( 's9', dpid='1000000000000009')
        s10 = self.addSwitch( 's10', dpid='1000000000000010')
        s11 = self.addSwitch( 's11', dpid='1000000000000011')
        s12 = self.addSwitch( 's12', dpid='1000000000000012')
        s13 = self.addSwitch( 's13', dpid='1000000000000013')
        s14 = self.addSwitch( 's14', dpid='1000000000000014')
        s15 = self.addSwitch( 's15', dpid='1000000000000015')
        s16 = self.addSwitch( 's16', dpid='1000000000000016')
        s17 = self.addSwitch( 's17', dpid='1000000000000017')
        s18 = self.addSwitch( 's18', dpid='1000000000000018')
        s19 = self.addSwitch( 's19', dpid='1000000000000019')
        s20 = self.addSwitch( 's20', dpid='1000000000000020')
        s21 = self.addSwitch( 's21', dpid='1000000000000021')
        s22 = self.addSwitch( 's22', dpid='1000000000000022')
        s23 = self.addSwitch( 's23', dpid='1000000000000023')
        s24 = self.addSwitch( 's24', dpid='1000000000000024')
        s25 = self.addSwitch( 's25', dpid='1000000000000025')

        # ... and now hosts
        s1_host = self.addHost( 'h1', ip='10.1.0.1/24', cls=dualStackHost, v6Addr='1000::1/64' )
        s2_host = self.addHost( 'h2', ip='10.1.0.2/24', cls=dualStackHost, v6Addr='1000::2/64' )
        s3_host = self.addHost( 'h3', ip='10.1.0.3/24', cls=dualStackHost, v6Addr='1000::3/64' )
        s4_host = self.addHost( 'h4', ip='10.1.0.4/24', cls=dualStackHost, v6Addr='1000::4/64' )
        s5_host = self.addHost( 'h5', ip='10.1.0.5/24', cls=dualStackHost, v6Addr='1000::5/64' )
        s6_host = self.addHost( 'h6', ip='10.1.0.6/24', cls=dualStackHost, v6Addr='1000::6/64' )
        s7_host = self.addHost( 'h7', ip='10.1.0.7/24', cls=dualStackHost, v6Addr='1000::7/64' )
        s8_host = self.addHost( 'h8', ip='10.1.0.8/24', cls=dualStackHost, v6Addr='1000::8/64' )
        s9_host = self.addHost( 'h9', ip='10.1.0.9/24', cls=dualStackHost, v6Addr='1000::9/64' )
        s10_host = self.addHost( 'h10', ip='10.1.0.10/24', cls=dualStackHost, v6Addr='1000::10/64' )
        s11_host = self.addHost( 'h11', ip='10.1.0.11/24', cls=dualStackHost, v6Addr='1000::11/64' )
        s12_host = self.addHost( 'h12', ip='10.1.0.12/24', cls=dualStackHost, v6Addr='1000::12/64' )
        s13_host = self.addHost( 'h13', ip='10.1.0.13/24', cls=dualStackHost, v6Addr='1000::13/64' )
        s14_host = self.addHost( 'h14', ip='10.1.0.14/24', cls=dualStackHost, v6Addr='1000::14/64' )
        s15_host = self.addHost( 'h15', ip='10.1.0.15/24', cls=dualStackHost, v6Addr='1000::15/64' )
        s16_host = self.addHost( 'h16', ip='10.1.0.16/24', cls=dualStackHost, v6Addr='1000::16/64' )
        s17_host = self.addHost( 'h17', ip='10.1.0.17/24', cls=dualStackHost, v6Addr='1000::17/64' )
        s18_host = self.addHost( 'h18', ip='10.1.0.18/24', cls=dualStackHost, v6Addr='1000::18/64' )
        s19_host = self.addHost( 'h19', ip='10.1.0.19/24', cls=dualStackHost, v6Addr='1000::19/64' )
        s20_host = self.addHost( 'h20', ip='10.1.0.20/24', cls=dualStackHost, v6Addr='1000::20/64' )
        s21_host = self.addHost( 'h21', ip='10.1.0.21/24', cls=dualStackHost, v6Addr='1000::21/64' )
        s22_host = self.addHost( 'h22', ip='10.1.0.22/24', cls=dualStackHost, v6Addr='1000::22/64' )
        s23_host = self.addHost( 'h23', ip='10.1.0.23/24', cls=dualStackHost, v6Addr='1000::23/64' )
        s24_host = self.addHost( 'h24', ip='10.1.0.24/24', cls=dualStackHost, v6Addr='1000::24/64' )
        s25_host = self.addHost( 'h25', ip='10.1.0.25/24', cls=dualStackHost, v6Addr='1000::25/64' )

        # add edges between switch and corresponding host
        self.addLink( s1 , s1_host )
        self.addLink( s2 , s2_host )
        self.addLink( s3 , s3_host )
        self.addLink( s4 , s4_host )
        self.addLink( s5 , s5_host )
        self.addLink( s6 , s6_host )
        self.addLink( s7 , s7_host )
        self.addLink( s8 , s8_host )
        self.addLink( s9 , s9_host )
        self.addLink( s10 , s10_host )
        self.addLink( s11 , s11_host )
        self.addLink( s12 , s12_host )
        self.addLink( s13 , s13_host )
        self.addLink( s14 , s14_host )
        self.addLink( s15 , s15_host )
        self.addLink( s16 , s16_host )
        self.addLink( s17 , s17_host )
        self.addLink( s18 , s18_host )
        self.addLink( s19 , s19_host )
        self.addLink( s20 , s20_host )
        self.addLink( s21 , s21_host )
        self.addLink( s22 , s22_host )
        self.addLink( s23 , s23_host )
        self.addLink( s24 , s24_host )
        self.addLink( s25 , s25_host )
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s6)
        self.addLink(s1, s7)
        self.addLink(s1, s8)
        self.addLink(s1, s9)
        self.addLink(s1, s10)
        self.addLink(s1, s11)
        self.addLink(s1, s12)
        self.addLink(s1, s13)
        self.addLink(s1, s14)
        self.addLink(s1, s15)
        self.addLink(s1, s16)
        self.addLink(s1, s17)
        self.addLink(s1, s18)
        self.addLink(s1, s19)
        self.addLink(s1, s20)
        self.addLink(s1, s21)
        self.addLink(s1, s22)
        self.addLink(s1, s23)
        self.addLink(s1, s24)
        self.addLink(s1, s25)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s2, s6)
        self.addLink(s2, s7)
        self.addLink(s2, s8)
        self.addLink(s2, s9)
        self.addLink(s2, s10)
        self.addLink(s2, s11)
        self.addLink(s2, s12)
        self.addLink(s2, s13)
        self.addLink(s2, s14)
        self.addLink(s2, s15)
        self.addLink(s2, s16)
        self.addLink(s2, s17)
        self.addLink(s2, s18)
        self.addLink(s2, s19)
        self.addLink(s2, s20)
        self.addLink(s2, s21)
        self.addLink(s2, s22)
        self.addLink(s2, s23)
        self.addLink(s2, s24)
        self.addLink(s2, s25)
        self.addLink(s3, s4)
        self.addLink(s3, s5)
        self.addLink(s3, s6)
        self.addLink(s3, s7)
        self.addLink(s3, s8)
        self.addLink(s3, s9)
        self.addLink(s3, s10)
        self.addLink(s3, s11)
        self.addLink(s3, s12)
        self.addLink(s3, s13)
        self.addLink(s3, s14)
        self.addLink(s3, s15)
        self.addLink(s3, s16)
        self.addLink(s3, s17)
        self.addLink(s3, s18)
        self.addLink(s3, s19)
        self.addLink(s3, s20)
        self.addLink(s3, s21)
        self.addLink(s3, s22)
        self.addLink(s3, s23)
        self.addLink(s3, s24)
        self.addLink(s3, s25)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s4, s7)
        self.addLink(s4, s8)
        self.addLink(s4, s9)
        self.addLink(s4, s10)
        self.addLink(s4, s11)
        self.addLink(s4, s12)
        self.addLink(s4, s13)
        self.addLink(s4, s14)
        self.addLink(s4, s15)
        self.addLink(s4, s16)
        self.addLink(s4, s17)
        self.addLink(s4, s18)
        self.addLink(s4, s19)
        self.addLink(s4, s20)
        self.addLink(s4, s21)
        self.addLink(s4, s22)
        self.addLink(s4, s23)
        self.addLink(s4, s24)
        self.addLink(s4, s25)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s9)
        self.addLink(s5, s10)
        self.addLink(s5, s11)
        self.addLink(s5, s12)
        self.addLink(s5, s13)
        self.addLink(s5, s14)
        self.addLink(s5, s15)
        self.addLink(s5, s16)
        self.addLink(s5, s17)
        self.addLink(s5, s18)
        self.addLink(s5, s19)
        self.addLink(s5, s20)
        self.addLink(s5, s21)
        self.addLink(s5, s22)
        self.addLink(s5, s23)
        self.addLink(s5, s24)
        self.addLink(s5, s25)
        self.addLink(s6, s7)
        self.addLink(s6, s8)
        self.addLink(s6, s9)
        self.addLink(s6, s10)
        self.addLink(s6, s11)
        self.addLink(s6, s12)
        self.addLink(s6, s13)
        self.addLink(s6, s14)
        self.addLink(s6, s15)
        self.addLink(s6, s16)
        self.addLink(s6, s17)
        self.addLink(s6, s18)
        self.addLink(s6, s19)
        self.addLink(s6, s20)
        self.addLink(s6, s21)
        self.addLink(s6, s22)
        self.addLink(s6, s23)
        self.addLink(s6, s24)
        self.addLink(s6, s25)
        self.addLink(s7, s8)
        self.addLink(s7, s9)
        self.addLink(s7, s10)
        self.addLink(s7, s11)
        self.addLink(s7, s12)
        self.addLink(s7, s13)
        self.addLink(s7, s14)
        self.addLink(s7, s15)
        self.addLink(s7, s16)
        self.addLink(s7, s17)
        self.addLink(s7, s18)
        self.addLink(s7, s19)
        self.addLink(s7, s20)
        self.addLink(s7, s21)
        self.addLink(s7, s22)
        self.addLink(s7, s23)
        self.addLink(s7, s24)
        self.addLink(s7, s25)
        self.addLink(s8, s9)
        self.addLink(s8, s10)
        self.addLink(s8, s11)
        self.addLink(s8, s12)
        self.addLink(s8, s13)
        self.addLink(s8, s14)
        self.addLink(s8, s15)
        self.addLink(s8, s16)
        self.addLink(s8, s17)
        self.addLink(s8, s18)
        self.addLink(s8, s19)
        self.addLink(s8, s20)
        self.addLink(s8, s21)
        self.addLink(s8, s22)
        self.addLink(s8, s23)
        self.addLink(s8, s24)
        self.addLink(s8, s25)
        self.addLink(s9, s10)
        self.addLink(s9, s11)
        self.addLink(s9, s12)
        self.addLink(s9, s13)
        self.addLink(s9, s14)
        self.addLink(s9, s15)
        self.addLink(s9, s16)
        self.addLink(s9, s17)
        self.addLink(s9, s18)
        self.addLink(s9, s19)
        self.addLink(s9, s20)
        self.addLink(s9, s21)
        self.addLink(s9, s22)
        self.addLink(s9, s23)
        self.addLink(s9, s24)
        self.addLink(s9, s25)
        self.addLink(s10, s11)
        self.addLink(s10, s12)
        self.addLink(s10, s13)
        self.addLink(s10, s14)
        self.addLink(s10, s15)
        self.addLink(s10, s16)
        self.addLink(s10, s17)
        self.addLink(s10, s18)
        self.addLink(s10, s19)
        self.addLink(s10, s20)
        self.addLink(s10, s21)
        self.addLink(s10, s22)
        self.addLink(s10, s23)
        self.addLink(s10, s24)
        self.addLink(s10, s25)
        self.addLink(s11, s12)
        self.addLink(s11, s13)
        self.addLink(s11, s14)
        self.addLink(s11, s15)
        self.addLink(s11, s16)
        self.addLink(s11, s17)
        self.addLink(s11, s18)
        self.addLink(s11, s19)
        self.addLink(s11, s20)
        self.addLink(s11, s21)
        self.addLink(s11, s22)
        self.addLink(s11, s23)
        self.addLink(s11, s24)
        self.addLink(s11, s25)
        self.addLink(s12, s13)
        self.addLink(s12, s14)
        self.addLink(s12, s15)
        self.addLink(s12, s16)
        self.addLink(s12, s17)
        self.addLink(s12, s18)
        self.addLink(s12, s19)
        self.addLink(s12, s20)
        self.addLink(s12, s21)
        self.addLink(s12, s22)
        self.addLink(s12, s23)
        self.addLink(s12, s24)
        self.addLink(s12, s25)
        self.addLink(s13, s14)
        self.addLink(s13, s15)
        self.addLink(s13, s16)
        self.addLink(s13, s17)
        self.addLink(s13, s18)
        self.addLink(s13, s19)
        self.addLink(s13, s20)
        self.addLink(s13, s21)
        self.addLink(s13, s22)
        self.addLink(s13, s23)
        self.addLink(s13, s24)
        self.addLink(s13, s25)
        self.addLink(s14, s15)
        self.addLink(s14, s16)
        self.addLink(s14, s17)
        self.addLink(s14, s18)
        self.addLink(s14, s19)
        self.addLink(s14, s20)
        self.addLink(s14, s21)
        self.addLink(s14, s22)
        self.addLink(s14, s23)
        self.addLink(s14, s24)
        self.addLink(s14, s25)
        self.addLink(s15, s16)
        self.addLink(s15, s17)
        self.addLink(s15, s18)
        self.addLink(s15, s19)
        self.addLink(s15, s20)
        self.addLink(s15, s21)
        self.addLink(s15, s22)
        self.addLink(s15, s23)
        self.addLink(s15, s24)
        self.addLink(s15, s25)
        self.addLink(s16, s17)
        self.addLink(s16, s18)
        self.addLink(s16, s19)
        self.addLink(s16, s20)
        self.addLink(s16, s21)
        self.addLink(s16, s22)
        self.addLink(s16, s23)
        self.addLink(s16, s24)
        self.addLink(s16, s25)
        self.addLink(s17, s18)
        self.addLink(s17, s19)
        self.addLink(s17, s20)
        self.addLink(s17, s21)
        self.addLink(s17, s22)
        self.addLink(s17, s23)
        self.addLink(s17, s24)
        self.addLink(s17, s25)
        self.addLink(s18, s19)
        self.addLink(s18, s20)
        self.addLink(s18, s21)
        self.addLink(s18, s22)
        self.addLink(s18, s23)
        self.addLink(s18, s24)
        self.addLink(s18, s25)
        self.addLink(s19, s20)
        self.addLink(s19, s21)
        self.addLink(s19, s22)
        self.addLink(s19, s23)
        self.addLink(s19, s24)
        self.addLink(s19, s25)
        self.addLink(s20, s21)
        self.addLink(s20, s22)
        self.addLink(s20, s23)
        self.addLink(s20, s24)
        self.addLink(s20, s25)
        self.addLink(s21, s22)
        self.addLink(s21, s23)
        self.addLink(s21, s24)
        self.addLink(s21, s25)
        self.addLink(s22, s23)
        self.addLink(s22, s24)
        self.addLink(s22, s25)
        self.addLink(s23, s24)
        self.addLink(s23, s25)
        self.addLink(s24, s25)

topos = { 'chordal': ( lambda: chordalTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

def setupNetwork():
    "Create network"
    topo = chordalTopo()
    #if controller_ip == '':
        #controller_ip = '10.0.2.2';
    #    controller_ip = '127.0.0.1';
    network = Mininet(topo=topo, switch=OVSSwitch,autoSetMacs=True, controller=None)
    network.start()
    CLI( network )
    network.stop()

if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    setupNetwork()
