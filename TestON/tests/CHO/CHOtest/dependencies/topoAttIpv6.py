#!/usr/bin/python

"""
Copyright 2015 Open Networking Foundation (ONF)

Please refer questions to either the onos test mailing list at <onos-test@onosproject.org>,
the System Testing Plans and Results wiki page at <https://wiki.onosproject.org/x/voMg>,
or the System Testing Guide page at <https://wiki.onosproject.org/x/WYQg>

    TestON is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    TestON is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with TestON.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
Custom topology for Mininet
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

class attTopo( Topo ):

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        NY54 = self.addSwitch( 's1' )
        CMBR = self.addSwitch( 's2' )
        CHCG = self.addSwitch( 's3' )
        CLEV = self.addSwitch( 's4' )
        RLGH = self.addSwitch( 's5' )
        ATLN = self.addSwitch( 's6' )
        PHLA = self.addSwitch( 's7' )
        WASH = self.addSwitch( 's8' )
        NSVL = self.addSwitch( 's9' )
        STLS = self.addSwitch( 's10' )
        NWOR = self.addSwitch( 's11' )
        HSTN = self.addSwitch( 's12' )
        SNAN = self.addSwitch( 's13' )
        DLLS = self.addSwitch( 's14' )
        ORLD = self.addSwitch( 's15' )
        DNVR = self.addSwitch( 's16' )
        KSCY = self.addSwitch( 's17' )
        SNFN = self.addSwitch( 's18' )
        SCRM = self.addSwitch( 's19' )
        PTLD = self.addSwitch( 's20' )
        STTL = self.addSwitch( 's21' )
        SLKC = self.addSwitch( 's22' )
        LA03 = self.addSwitch( 's23' )
        SNDG = self.addSwitch( 's24' )
        PHNX = self.addSwitch( 's25' )

        # ... and now hosts
        NY54_host = self.addHost( 'h1', ip='10.1.0.1/24', cls=dualStackHost, v6Addr='1000::1/64' )
        CMBR_host = self.addHost( 'h2', ip='10.1.0.2/24', cls=dualStackHost, v6Addr='1000::2/64' )
        CHCG_host = self.addHost( 'h3', ip='10.1.0.3/24', cls=dualStackHost, v6Addr='1000::3/64' )
        CLEV_host = self.addHost( 'h4', ip='10.1.0.4/24', cls=dualStackHost, v6Addr='1000::4/64' )
        RLGH_host = self.addHost( 'h5', ip='10.1.0.5/24', cls=dualStackHost, v6Addr='1000::5/64' )
        ATLN_host = self.addHost( 'h6', ip='10.1.0.6/24', cls=dualStackHost, v6Addr='1000::6/64' )
        PHLA_host = self.addHost( 'h7', ip='10.1.0.7/24', cls=dualStackHost, v6Addr='1000::7/64' )
        WASH_host = self.addHost( 'h8', ip='10.1.0.8/24', cls=dualStackHost, v6Addr='1000::8/64' )
        NSVL_host = self.addHost( 'h9', ip='10.1.0.9/24', cls=dualStackHost, v6Addr='1000::9/64' )
        STLS_host = self.addHost( 'h10', ip='10.1.0.10/24', cls=dualStackHost, v6Addr='1000::10/64' )
        NWOR_host = self.addHost( 'h11', ip='10.1.0.11/24', cls=dualStackHost, v6Addr='1000::11/64' )
        HSTN_host = self.addHost( 'h12', ip='10.1.0.12/24', cls=dualStackHost, v6Addr='1000::12/64' )
        SNAN_host = self.addHost( 'h13', ip='10.1.0.13/24', cls=dualStackHost, v6Addr='1000::13/64' )
        DLLS_host = self.addHost( 'h14', ip='10.1.0.14/24', cls=dualStackHost, v6Addr='1000::14/64' )
        ORLD_host = self.addHost( 'h15', ip='10.1.0.15/24', cls=dualStackHost, v6Addr='1000::15/64' )
        DNVR_host = self.addHost( 'h16', ip='10.1.0.16/24', cls=dualStackHost, v6Addr='1000::16/64' )
        KSCY_host = self.addHost( 'h17', ip='10.1.0.17/24', cls=dualStackHost, v6Addr='1000::17/64' )
        SNFN_host = self.addHost( 'h18', ip='10.1.0.18/24', cls=dualStackHost, v6Addr='1000::18/64' )
        SCRM_host = self.addHost( 'h19', ip='10.1.0.19/24', cls=dualStackHost, v6Addr='1000::19/64' )
        PTLD_host = self.addHost( 'h20', ip='10.1.0.20/24', cls=dualStackHost, v6Addr='1000::20/64' )
        STTL_host = self.addHost( 'h21', ip='10.1.0.21/24', cls=dualStackHost, v6Addr='1000::21/64' )
        SLKC_host = self.addHost( 'h22', ip='10.1.0.22/24', cls=dualStackHost, v6Addr='1000::22/64' )
        LA03_host = self.addHost( 'h23', ip='10.1.0.23/24', cls=dualStackHost, v6Addr='1000::23/64' )
        SNDG_host = self.addHost( 'h24', ip='10.1.0.24/24', cls=dualStackHost, v6Addr='1000::24/64' )
        PHNX_host = self.addHost( 'h25', ip='10.1.0.25/24', cls=dualStackHost, v6Addr='1000::25/64' )

        # add edges between switch and corresponding host
        self.addLink( NY54 , NY54_host )
        self.addLink( CMBR , CMBR_host )
        self.addLink( CHCG , CHCG_host )
        self.addLink( CLEV , CLEV_host )
        self.addLink( RLGH , RLGH_host )
        self.addLink( ATLN , ATLN_host )
        self.addLink( PHLA , PHLA_host )
        self.addLink( WASH , WASH_host )
        self.addLink( NSVL , NSVL_host )
        self.addLink( STLS , STLS_host )
        self.addLink( NWOR , NWOR_host )
        self.addLink( HSTN , HSTN_host )
        self.addLink( SNAN , SNAN_host )
        self.addLink( DLLS , DLLS_host )
        self.addLink( ORLD , ORLD_host )
        self.addLink( DNVR , DNVR_host )
        self.addLink( KSCY , KSCY_host )
        self.addLink( SNFN , SNFN_host )
        self.addLink( SCRM , SCRM_host )
        self.addLink( PTLD , PTLD_host )
        self.addLink( STTL , STTL_host )
        self.addLink( SLKC , SLKC_host )
        self.addLink( LA03 , LA03_host )
        self.addLink( SNDG , SNDG_host )
        self.addLink( PHNX , PHNX_host )

        # add edges between switches
        self.addLink( NY54 , CMBR, bw=10, delay='0.979030824185ms')
        self.addLink( NY54 , CHCG, bw=10, delay='0.806374975652ms')
        self.addLink( NY54 , PHLA, bw=10, delay='0.686192970166ms')
        self.addLink( NY54 , WASH, bw=10, delay='0.605826192092ms')
        self.addLink( CMBR , PHLA, bw=10, delay='1.4018238197ms')
        self.addLink( CHCG , CLEV, bw=10, delay='0.232315346482ms')
        self.addLink( CHCG , PHLA, bw=10, delay='1.07297714274ms')
        self.addLink( CHCG , STLS, bw=10, delay='1.12827896944ms')
        self.addLink( CHCG , DNVR, bw=10, delay='1.35964770335ms')
        self.addLink( CHCG , KSCY, bw=10, delay='1.5199778541ms')
        self.addLink( CHCG , SNFN, bw=10, delay='0.620743405435ms')
        self.addLink( CHCG , STTL, bw=10, delay='0.93027212534ms')
        self.addLink( CHCG , SLKC, bw=10, delay='0.735621751348ms')
        self.addLink( CLEV , NSVL, bw=10, delay='0.523419372248ms')
        self.addLink( CLEV , STLS, bw=10, delay='1.00360290845ms')
        self.addLink( CLEV , PHLA, bw=10, delay='0.882912133249ms')
        self.addLink( RLGH , ATLN, bw=10, delay='1.1644489729ms')
        self.addLink( RLGH , WASH, bw=10, delay='1.48176810502ms')
        self.addLink( ATLN , WASH, bw=10, delay='0.557636936322ms')
        self.addLink( ATLN , NSVL, bw=10, delay='1.32869749865ms')
        self.addLink( ATLN , STLS, bw=10, delay='0.767705554748ms')
        self.addLink( ATLN , DLLS, bw=10, delay='0.544782086448ms')
        self.addLink( ATLN , ORLD, bw=10, delay='1.46119152532ms')
        self.addLink( PHLA , WASH, bw=10, delay='0.372209320106ms')
        self.addLink( NSVL , STLS, bw=10, delay='1.43250491305ms')
        self.addLink( NSVL , DLLS, bw=10, delay='1.67698215288ms')
        self.addLink( STLS , DLLS, bw=10, delay='0.256389964194ms')
        self.addLink( STLS , KSCY, bw=10, delay='0.395511571791ms')
        self.addLink( STLS , LA03, bw=10, delay='0.257085227363ms')
        self.addLink( NWOR , HSTN, bw=10, delay='0.0952906633914ms')
        self.addLink( NWOR , DLLS, bw=10, delay='1.60231329739ms')
        self.addLink( NWOR , ORLD, bw=10, delay='0.692731063896ms')
        self.addLink( HSTN , SNAN, bw=10, delay='0.284150653798ms')
        self.addLink( HSTN , DLLS, bw=10, delay='1.65690128332ms')
        self.addLink( HSTN , ORLD, bw=10, delay='0.731886304782ms')
        self.addLink( SNAN , PHNX, bw=10, delay='1.34258627257ms')
        self.addLink( SNAN , DLLS, bw=10, delay='1.50063532341ms')
        self.addLink( DLLS , DNVR, bw=10, delay='0.251471593235ms')
        self.addLink( DLLS , KSCY, bw=10, delay='0.18026026737ms')
        self.addLink( DLLS , SNFN, bw=10, delay='0.74304274592ms')
        self.addLink( DLLS , LA03, bw=10, delay='0.506439293357ms')
        self.addLink( DNVR , KSCY, bw=10, delay='0.223328790403ms')
        self.addLink( DNVR , SNFN, bw=10, delay='0.889017541903ms')
        self.addLink( DNVR , SLKC, bw=10, delay='0.631898982721ms')
        self.addLink( KSCY , SNFN, bw=10, delay='0.922778522233ms')
        self.addLink( SNFN , SCRM, bw=10, delay='0.630352278097ms')
        self.addLink( SNFN , PTLD, bw=10, delay='0.828572513655ms')
        self.addLink( SNFN , STTL, bw=10, delay='1.54076081649ms')
        self.addLink( SNFN , SLKC, bw=10, delay='0.621507502625ms')
        self.addLink( SNFN , LA03, bw=10, delay='0.602936230151ms')
        self.addLink( SCRM , SLKC, bw=10, delay='0.461350343644ms')
        self.addLink( PTLD , STTL, bw=10, delay='1.17591515181ms')
        self.addLink( SLKC , LA03, bw=10, delay='0.243225267023ms')
        self.addLink( LA03 , SNDG, bw=10, delay='0.681264950821ms')
        self.addLink( LA03 , PHNX, bw=10, delay='0.343709457969ms')
        self.addLink( SNDG , PHNX, bw=10, delay='0.345064487693ms')

topos = { 'att': ( lambda: attTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

def setupNetwork():
    "Create network"
    topo = attTopo()
    #if controller_ip == '':
        #controller_ip = '10.0.2.2';
    #    controller_ip = '127.0.0.1';
    network = Mininet(topo=topo, link=TCLink, autoSetMacs=True, controller=None)
    network.start()
    CLI( network )
    network.stop()

if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    setupNetwork()
