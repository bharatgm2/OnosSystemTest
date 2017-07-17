#!/usr/bin/python

"""
Copyright 2016 Open Networking Foundation (ONF)

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
    def config( self, v6Addr='1000::1/64', **params ):
        r = super( Host, self ).config( **params )
        intf = self.defaultIntf()
        self.cmd( 'ip -6 addr add %s dev %s' % ( v6Addr, intf ) )
        return r

class spineTopo( Topo ):

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        # add nodes, Leaf switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )
        s8 = self.addSwitch( 's8' )
        s9 = self.addSwitch( 's9' )
        s10 = self.addSwitch( 's10' )
        s11 = self.addSwitch( 's11' )
        s12 = self.addSwitch( 's12' )
        s13 = self.addSwitch( 's13' )
        s14 = self.addSwitch( 's14' )

        # add nodes, Spine switches first...
        s15 = self.addSwitch( 's15' )
        s16 = self.addSwitch( 's16' )
        s17 = self.addSwitch( 's17' )
        s18 = self.addSwitch( 's18' )
        s19 = self.addSwitch( 's19' )
        s20 = self.addSwitch( 's20' )
        s21 = self.addSwitch( 's21' )
        s22 = self.addSwitch( 's22' )
        s23 = self.addSwitch( 's23' )
        s24 = self.addSwitch( 's24' )
        s25 = self.addSwitch( 's25' )
        s26 = self.addSwitch( 's26' )
        s27 = self.addSwitch( 's27' )
        s28 = self.addSwitch( 's28' )
        s29 = self.addSwitch( 's29' )
        s30 = self.addSwitch( 's30' )
        s31 = self.addSwitch( 's31' )
        s32 = self.addSwitch( 's32' )
        s33 = self.addSwitch( 's33' )
        s34 = self.addSwitch( 's34' )
        s35 = self.addSwitch( 's35' )
        s36 = self.addSwitch( 's36' )
        s37 = self.addSwitch( 's37' )
        s38 = self.addSwitch( 's38' )
        s39 = self.addSwitch( 's39' )
        s40 = self.addSwitch( 's40' )
        s41 = self.addSwitch( 's41' )
        s42 = self.addSwitch( 's42' )
        s43 = self.addSwitch( 's43' )
        s44 = self.addSwitch( 's44' )
        s45 = self.addSwitch( 's45' )
        s46 = self.addSwitch( 's46' )
        s47 = self.addSwitch( 's47' )
        s48 = self.addSwitch( 's48' )
        s49 = self.addSwitch( 's49' )
        s50 = self.addSwitch( 's50' )
        s51 = self.addSwitch( 's51' )
        s52 = self.addSwitch( 's52' )
        s53 = self.addSwitch( 's53' )
        s54 = self.addSwitch( 's54' )
        s55 = self.addSwitch( 's55' )
        s56 = self.addSwitch( 's56' )
        s57 = self.addSwitch( 's57' )
        s58 = self.addSwitch( 's58' )
        s59 = self.addSwitch( 's59' )
        s60 = self.addSwitch( 's60' )
        s61 = self.addSwitch( 's61' )
        s62 = self.addSwitch( 's62' )
        s63 = self.addSwitch( 's63' )
        s64 = self.addSwitch( 's64' )
        s65 = self.addSwitch( 's65' )
        s66 = self.addSwitch( 's66' )
        s67 = self.addSwitch( 's67' )
        s68 = self.addSwitch( 's68' )
        s69 = self.addSwitch( 's69' )
        s70 = self.addSwitch( 's70' )
        s71 = self.addSwitch( 's71' )
        s72 = self.addSwitch( 's72' )
        s73 = self.addSwitch( 's73' )
        s74 = self.addSwitch( 's74' )
        s75 = self.addSwitch( 's75' )
        s76 = self.addSwitch( 's76' )
        s77 = self.addSwitch( 's77' )
        s78 = self.addSwitch( 's78' )


        # ... and now hosts
        # s1_host = self.addHost( 'h1', ip='10.1.0.1/24', cls=dualStackHost, v6Addr='1000::1/64' )
        # s2_host = self.addHost( 'h2', ip='10.1.0.2/24', cls=dualStackHost, v6Addr='1000::2/64' )
        # s3_host = self.addHost( 'h3', ip='10.1.0.3/24', cls=dualStackHost, v6Addr='1000::3/64' )
        # s4_host = self.addHost( 'h4', ip='10.1.0.4/24', cls=dualStackHost, v6Addr='1000::4/64' )
        # s5_host = self.addHost( 'h5', ip='10.1.0.5/24', cls=dualStackHost, v6Addr='1000::5/64' )
        # s6_host = self.addHost( 'h6', ip='10.1.0.6/24', cls=dualStackHost, v6Addr='1000::6/64' )
        # s7_host = self.addHost( 'h7', ip='10.1.0.7/24', cls=dualStackHost, v6Addr='1000::7/64' )
        # s8_host = self.addHost( 'h8', ip='10.1.0.8/24', cls=dualStackHost, v6Addr='1000::8/64' )
        # s9_host = self.addHost( 'h9', ip='10.1.0.9/24', cls=dualStackHost, v6Addr='1000::9/64' )
        # s10_host = self.addHost( 'h10', ip='10.1.0.10/24', cls=dualStackHost, v6Addr='1000::10/64' )
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
        s26_host = self.addHost( 'h26', ip='10.1.0.26/24', cls=dualStackHost, v6Addr='1000::26/64' )
        s27_host = self.addHost( 'h27', ip='10.1.0.27/24', cls=dualStackHost, v6Addr='1000::27/64' )
        s28_host = self.addHost( 'h28', ip='10.1.0.28/24', cls=dualStackHost, v6Addr='1000::28/64' )
        s29_host = self.addHost( 'h29', ip='10.1.0.29/24', cls=dualStackHost, v6Addr='1000::29/64' )
        s30_host = self.addHost( 'h30', ip='10.1.0.30/24', cls=dualStackHost, v6Addr='1000::30/64' )
        s31_host = self.addHost( 'h31', ip='10.1.0.31/24', cls=dualStackHost, v6Addr='1000::31/64' )
        s32_host = self.addHost( 'h32', ip='10.1.0.32/24', cls=dualStackHost, v6Addr='1000::32/64' )
        s33_host = self.addHost( 'h33', ip='10.1.0.33/24', cls=dualStackHost, v6Addr='1000::33/64' )
        s34_host = self.addHost( 'h34', ip='10.1.0.34/24', cls=dualStackHost, v6Addr='1000::34/64' )
        s35_host = self.addHost( 'h35', ip='10.1.0.35/24', cls=dualStackHost, v6Addr='1000::35/64' )
        s36_host = self.addHost( 'h36', ip='10.1.0.36/24', cls=dualStackHost, v6Addr='1000::36/64' )
        s37_host = self.addHost( 'h37', ip='10.1.0.37/24', cls=dualStackHost, v6Addr='1000::37/64' )
        s38_host = self.addHost( 'h38', ip='10.1.0.38/24', cls=dualStackHost, v6Addr='1000::38/64' )
        s39_host = self.addHost( 'h39', ip='10.1.0.39/24', cls=dualStackHost, v6Addr='1000::39/64' )
        s40_host = self.addHost( 'h40', ip='10.1.0.40/24', cls=dualStackHost, v6Addr='1000::40/64' )
        s41_host = self.addHost( 'h41', ip='10.1.0.41/24', cls=dualStackHost, v6Addr='1000::41/64' )
        s42_host = self.addHost( 'h42', ip='10.1.0.42/24', cls=dualStackHost, v6Addr='1000::42/64' )
        s43_host = self.addHost( 'h43', ip='10.1.0.43/24', cls=dualStackHost, v6Addr='1000::43/64' )
        s44_host = self.addHost( 'h44', ip='10.1.0.44/24', cls=dualStackHost, v6Addr='1000::44/64' )
        s45_host = self.addHost( 'h45', ip='10.1.0.45/24', cls=dualStackHost, v6Addr='1000::45/64' )
        s46_host = self.addHost( 'h46', ip='10.1.0.46/24', cls=dualStackHost, v6Addr='1000::46/64' )
        s47_host = self.addHost( 'h47', ip='10.1.0.47/24', cls=dualStackHost, v6Addr='1000::47/64' )
        s48_host = self.addHost( 'h48', ip='10.1.0.48/24', cls=dualStackHost, v6Addr='1000::48/64' )
        s49_host = self.addHost( 'h49', ip='10.1.0.49/24', cls=dualStackHost, v6Addr='1000::49/64' )
        s50_host = self.addHost( 'h50', ip='10.1.0.50/24', cls=dualStackHost, v6Addr='1000::50/64' )
        s51_host = self.addHost( 'h51', ip='10.1.0.51/24', cls=dualStackHost, v6Addr='1000::51/64' )
        s52_host = self.addHost( 'h52', ip='10.1.0.52/24', cls=dualStackHost, v6Addr='1000::52/64' )
        s53_host = self.addHost( 'h53', ip='10.1.0.53/24', cls=dualStackHost, v6Addr='1000::53/64' )
        s54_host = self.addHost( 'h54', ip='10.1.0.54/24', cls=dualStackHost, v6Addr='1000::54/64' )
        s55_host = self.addHost( 'h55', ip='10.1.0.55/24', cls=dualStackHost, v6Addr='1000::55/64' )
        s56_host = self.addHost( 'h56', ip='10.1.0.56/24', cls=dualStackHost, v6Addr='1000::56/64' )
        s57_host = self.addHost( 'h57', ip='10.1.0.57/24', cls=dualStackHost, v6Addr='1000::57/64' )
        s58_host = self.addHost( 'h58', ip='10.1.0.58/24', cls=dualStackHost, v6Addr='1000::58/64' )
        s59_host = self.addHost( 'h59', ip='10.1.0.59/24', cls=dualStackHost, v6Addr='1000::59/64' )
        s60_host = self.addHost( 'h60', ip='10.1.0.60/24', cls=dualStackHost, v6Addr='1000::60/64' )
        s61_host = self.addHost( 'h61', ip='10.1.0.61/24', cls=dualStackHost, v6Addr='1000::61/64' )
        s62_host = self.addHost( 'h62', ip='10.1.0.62/24', cls=dualStackHost, v6Addr='1000::62/64' )
        s63_host = self.addHost( 'h63', ip='10.1.0.63/24', cls=dualStackHost, v6Addr='1000::63/64' )
        s64_host = self.addHost( 'h64', ip='10.1.0.64/24', cls=dualStackHost, v6Addr='1000::64/64' )
        s65_host = self.addHost( 'h65', ip='10.1.0.65/24', cls=dualStackHost, v6Addr='1000::65/64' )
        s66_host = self.addHost( 'h66', ip='10.1.0.66/24', cls=dualStackHost, v6Addr='1000::66/64' )
        s67_host = self.addHost( 'h67', ip='10.1.0.67/24', cls=dualStackHost, v6Addr='1000::67/64' )
        s68_host = self.addHost( 'h68', ip='10.1.0.68/24', cls=dualStackHost, v6Addr='1000::68/64' )
        s69_host = self.addHost( 'h69', ip='10.1.0.69/24', cls=dualStackHost, v6Addr='1000::69/64' )
        s70_host = self.addHost( 'h70', ip='10.1.0.70/24', cls=dualStackHost, v6Addr='1000::70/64' )
        s71_host = self.addHost( 'h71', ip='10.1.0.71/24', cls=dualStackHost, v6Addr='1000::71/64' )
        s72_host = self.addHost( 'h72', ip='10.1.0.72/24', cls=dualStackHost, v6Addr='1000::72/64' )
        s73_host = self.addHost( 'h73', ip='10.1.0.73/24', cls=dualStackHost, v6Addr='1000::73/64' )
        s74_host = self.addHost( 'h74', ip='10.1.0.74/24', cls=dualStackHost, v6Addr='1000::74/64' )
        s75_host = self.addHost( 'h75', ip='10.1.0.75/24', cls=dualStackHost, v6Addr='1000::75/64' )
        s76_host = self.addHost( 'h76', ip='10.1.0.76/24', cls=dualStackHost, v6Addr='1000::76/64' )
        s77_host = self.addHost( 'h77', ip='10.1.0.77/24', cls=dualStackHost, v6Addr='1000::77/64' )
        s78_host = self.addHost( 'h78', ip='10.1.0.78/24', cls=dualStackHost, v6Addr='1000::78/64' )

        # add edges between switch and corresponding host
        #self.addLink( s1 , s1_host )
        #self.addLink( s2 , s2_host )
        #self.addLink( s3 , s3_host )
        #self.addLink( s4 , s4_host )
        #self.addLink( s5 , s5_host )
        #self.addLink( s6 , s6_host )
        #self.addLink( s7 , s7_host )
        #self.addLink( s8 , s8_host )
        #self.addLink( s9 , s9_host )
        #self.addLink( s10 , s10_host )
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
        self.addLink( s26 , s26_host )
        self.addLink( s27 , s27_host )
        self.addLink( s28 , s28_host )
        self.addLink( s29 , s29_host )
        self.addLink( s30 , s30_host )
        self.addLink( s31 , s31_host )
        self.addLink( s32 , s32_host )
        self.addLink( s33 , s33_host )
        self.addLink( s34 , s34_host )
        self.addLink( s35 , s35_host )
        self.addLink( s36 , s36_host )
        self.addLink( s37 , s37_host )
        self.addLink( s38 , s38_host )
        self.addLink( s39 , s39_host )
        self.addLink( s40 , s40_host )
        self.addLink( s41 , s41_host )
        self.addLink( s42 , s42_host )
        self.addLink( s43 , s43_host )
        self.addLink( s44 , s44_host )
        self.addLink( s45 , s45_host )
        self.addLink( s46 , s46_host )
        self.addLink( s47 , s47_host )
        self.addLink( s48 , s48_host )
        self.addLink( s49 , s49_host )
        self.addLink( s50 , s50_host )
        self.addLink( s51 , s51_host )
        self.addLink( s52 , s52_host )
        self.addLink( s53 , s53_host )
        self.addLink( s54 , s54_host )
        self.addLink( s55 , s55_host )
        self.addLink( s56 , s56_host )
        self.addLink( s57 , s57_host )
        self.addLink( s58 , s58_host )
        self.addLink( s59 , s59_host )
        self.addLink( s60 , s60_host )
        self.addLink( s61 , s61_host )
        self.addLink( s62 , s62_host )
        self.addLink( s63 , s63_host )
        self.addLink( s64 , s64_host )
        self.addLink( s65 , s65_host )
        self.addLink( s66 , s66_host )
        self.addLink( s67 , s67_host )
        self.addLink( s68 , s68_host )
        self.addLink( s69 , s69_host )
        self.addLink( s70 , s70_host )
        self.addLink( s71 , s71_host )
        self.addLink( s72 , s72_host )
        self.addLink( s73 , s73_host )
        self.addLink( s74 , s74_host )
        self.addLink( s75 , s75_host )
        self.addLink( s76 , s76_host )
        self.addLink( s77 , s77_host )
        self.addLink( s78 , s78_host )

        #info( '*** Add Leaf links\n')
        self.addLink(s1, s9)
        self.addLink(s2, s10)
        self.addLink(s3, s9)
        self.addLink(s4, s10)
        self.addLink(s5, s9)
        self.addLink(s6, s10)
        self.addLink(s7, s9)
        self.addLink(s8, s10)
        self.addLink(s9, s11)
        self.addLink(s9, s12)
        self.addLink(s10, s13)
        self.addLink(s10, s14)
        self.addLink(s11, s12)
        self.addLink(s13, s14)

        #info( '*** Add Spine-1 links\n')
        self.addLink(s15, s1)
        self.addLink(s15, s2)
        self.addLink(s16, s1)
        self.addLink(s16, s2)
        self.addLink(s17, s1)
        self.addLink(s17, s2)
        self.addLink(s18, s1)
        self.addLink(s18, s2)
        self.addLink(s19, s1)
        self.addLink(s19, s2)
        self.addLink(s20, s1)
        self.addLink(s20, s2)
        self.addLink(s21, s1)
        self.addLink(s21, s2)
        self.addLink(s22, s1)
        self.addLink(s22, s2)
        self.addLink(s23, s1)
        self.addLink(s23, s2)
        self.addLink(s24, s1)
        self.addLink(s24, s2)
        self.addLink(s25, s1)
        self.addLink(s25, s2)
        self.addLink(s26, s1)
        self.addLink(s26, s2)
        self.addLink(s27, s1)
        self.addLink(s27, s2)
        self.addLink(s28, s1)
        self.addLink(s28, s2)
        self.addLink(s29, s1)
        self.addLink(s29, s2)
        self.addLink(s30, s1)
        self.addLink(s30, s2)

        #info( '*** Add Spine-2 links\n')
        self.addLink(s31, s3)
        self.addLink(s31, s4)
        self.addLink(s32, s3)
        self.addLink(s32, s4)
        self.addLink(s33, s3)
        self.addLink(s33, s4)
        self.addLink(s34, s3)
        self.addLink(s34, s4)
        self.addLink(s35, s3)
        self.addLink(s35, s4)
        self.addLink(s36, s3)
        self.addLink(s36, s4)
        self.addLink(s37, s3)
        self.addLink(s37, s4)
        self.addLink(s38, s3)
        self.addLink(s38, s4)
        self.addLink(s39, s3)
        self.addLink(s39, s4)
        self.addLink(s40, s3)
        self.addLink(s40, s4)
        self.addLink(s41, s3)
        self.addLink(s41, s4)
        self.addLink(s42, s3)
        self.addLink(s42, s4)
        self.addLink(s43, s3)
        self.addLink(s43, s4)
        self.addLink(s44, s3)
        self.addLink(s44, s4)
        self.addLink(s45, s3)
        self.addLink(s45, s4)
        self.addLink(s46, s3)
        self.addLink(s46, s4)

        #info( '*** Add Spine-3 links\n')
        self.addLink(s47, s5)
        self.addLink(s47, s6)
        self.addLink(s48, s5)
        self.addLink(s48, s6)
        self.addLink(s49, s5)
        self.addLink(s49, s6)
        self.addLink(s50, s5)
        self.addLink(s50, s6)
        self.addLink(s51, s5)
        self.addLink(s51, s6)
        self.addLink(s52, s5)
        self.addLink(s52, s6)
        self.addLink(s53, s5)
        self.addLink(s53, s6)
        self.addLink(s54, s5)
        self.addLink(s54, s6)
        self.addLink(s55, s5)
        self.addLink(s55, s6)
        self.addLink(s56, s5)
        self.addLink(s56, s6)
        self.addLink(s57, s5)
        self.addLink(s57, s6)
        self.addLink(s58, s5)
        self.addLink(s58, s6)
        self.addLink(s59, s5)
        self.addLink(s59, s6)
        self.addLink(s60, s5)
        self.addLink(s60, s6)
        self.addLink(s61, s5)
        self.addLink(s61, s6)
        self.addLink(s62, s5)
        self.addLink(s62, s6)

        #info( '*** Add Spine-4 links\n')
        self.addLink(s63, s7)
        self.addLink(s63, s8)
        self.addLink(s64, s7)
        self.addLink(s64, s8)
        self.addLink(s65, s7)
        self.addLink(s65, s8)
        self.addLink(s66, s7)
        self.addLink(s66, s8)
        self.addLink(s67, s7)
        self.addLink(s67, s8)
        self.addLink(s68, s7)
        self.addLink(s68, s8)
        self.addLink(s69, s7)
        self.addLink(s69, s8)
        self.addLink(s70, s7)
        self.addLink(s70, s8)
        self.addLink(s71, s7)
        self.addLink(s71, s8)
        self.addLink(s72, s7)
        self.addLink(s72, s8)
        self.addLink(s73, s7)
        self.addLink(s73, s8)
        self.addLink(s74, s7)
        self.addLink(s74, s8)
        self.addLink(s75, s7)
        self.addLink(s75, s8)
        self.addLink(s76, s7)
        self.addLink(s76, s8)
        self.addLink(s77, s7)
        self.addLink(s77, s8)
        self.addLink(s78, s7)
        self.addLink(s78, s8)

topos = { 'spine': ( lambda: spineTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

def setupNetwork():
    "Create network"
    topo = spineTopo()
    #if controller_ip == '':
        #controller_ip = '10.0.2.2';
    #    controller_ip = '127.0.0.1';
    network = Mininet(topo=topo, switch=OVSSwitch, link=TCLink, autoSetMacs = True, controller=None)
    network.start()
    CLI( network )
    network.stop()

if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    setupNetwork()
