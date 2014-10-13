#!/usr/bin/env python

'''
This driver enters the onos> prompt to issue commands.

Please follow the coding style demonstrated by existing 
functions and document properly.

If you are a contributor to the driver, please
list your email here for future contact:

jhall@onlab.us
andrew@onlab.us

OCT 13 2014

'''

import sys
import time
import pexpect
import re
import traceback
import os.path
import pydoc
sys.path.append("../")
from drivers.common.clidriver import CLI

class OnosCliDriver(CLI):

    def __init__(self):
        '''
        Initialize client 
        '''
        super(CLI, self).__init__()

    def connect(self,**connectargs):
        '''
        Creates ssh handle for ONOS cli.
        '''
        try:
            for key in connectargs:
                vars(self)[key] = connectargs[key]
            self.home = "~/ONOS"
            for key in self.options:
                if key == "home":
                    self.home = self.options['home']
                    break


            self.name = self.options['name']
            self.handle = super(OnosCliDriver,self).connect(
                    user_name = self.user_name, 
                    ip_address = self.ip_address,
                    port = self.port, 
                    pwd = self.pwd, 
                    home = self.home)
           
            self.handle.sendline("cd "+ self.home)
            self.handle.expect("\$")
            if self.handle:
                return self.handle
            else :
                main.log.info("NO ONOS HANDLE")
                return main.FALSE
        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":     " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name + ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            main.log.error( traceback.print_exc() )
            main.log.info(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            main.cleanup()
            main.exit()

    def disconnect(self):
        '''
        Called when Test is complete to disconnect the ONOS handle.
        '''
        response = ''
        try:
            self.handle.sendline("system:shutdown")
            self.handle.expect("Confirm")
            self.handle.sendline("Yes")
            self.handle.expect("\$")

        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":     " + self.handle.before)
        except:
            main.log.error(self.name + ": Connection failed to the host")
            response = main.FALSE
        return response

    def set_cell(self, cellname):
        '''
        Calls 'cell <name>' to set the environment variables on ONOSbench
        
        Before issuing any cli commands, set the environment variable first.
        '''
        try:
            if not cellname:
                main.log.error("Must define cellname")
                main.cleanup()
                main.exit()
            else:
                self.handle.sendline("cell "+str(cellname))
                #Expect the cellname in the ONOS_CELL variable.
                #Note that this variable name is subject to change
                #   and that this driver will have to change accordingly
                self.handle.expect("ONOS_CELL="+str(cellname))
                handle_before = self.handle.before
                handle_after = self.handle.after
                #Get the rest of the handle
                self.handle.sendline("")
                self.handle.expect("\$")
                handle_more = self.handle.before

                main.log.info("Cell call returned: "+handle_before+
                        handle_after + handle_more)

                return main.TRUE

        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()
        
    def start_onos_cli(self, ONOS_ip):
        try:
            self.handle.sendline("")
            self.handle.expect("\$")

            #Wait for onos start (-w) and enter onos cli
            self.handle.sendline("onos -w "+str(ONOS_ip))
            self.handle.expect("onos>")

        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()

    def sendline(self, cmd_str):
        '''
        Send a completely user specified string to 
        the onos> prompt. Use this function if you have 
        a very specific command to send.
        
        Warning: There are no sanity checking to commands
        sent using this method.
        '''
        try:
            self.handle.sendline("")
            self.handle.expect("onos>")

            self.handle.sendline(cmd_str)
            self.handle.expect("onos>")

            handle = self.handle.before
            
            self.handle.sendline("")
            self.handle.expect("onos>")
            
            handle += self.handle.before
            handle += self.handle.after

            main.log.info("Command sent.")

            return handle
        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()

    #IMPORTANT NOTE:
    #For all cli commands, naming convention should match
    #the cli command replacing ':' with '_'.
    #Ex) onos:topology > onos_topology
    #    onos:links    > onos_links
    #    feature:list  > feature_list
   
    def add_node(self, node_id, ONOS_ip, tcp_port=""):
        '''
        Adds a new cluster node by ID and address information.
        Required:
            * node_id
            * ONOS_ip
        Optional:
            * tcp_port
        '''
        try:
            self.handle.sendline("")
            self.handle.expect("onos>")

            self.handle.sendline("add-node "+
                    str(node_id)+" "+
                    str(ONOS_ip)+" "+
                    str(tcp_port))
            
            i = self.handle.expect([
                "Error",
                "onos>" ])
            
            #Clear handle to get previous output
            self.handle.sendline("")
            self.handle.expect("onos>")

            handle = self.handle.before

            if i == 0:
                main.log.error("Error in adding node")
                main.log.error(handle)
                return main.FALSE 
            else:
                main.log.info("Node "+str(ONOS_ip)+" added")
                return main.TRUE

        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()

    def remove_node(self, node_id):
        '''
        Removes a cluster by ID
        Issues command: 'remove-node [<node-id>]'
        Required:
            * node_id
        '''
        try:
            self.handle.sendline("")
            self.handle.expect("onos>")

            self.handle.sendline("remove-node "+str(node_id))
            self.handle.expect("onos>")

            return main.TRUE
        
        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()

    def onos_topology(self):
        '''
        Shows the current state of the topology
        by issusing command: 'onos> onos:topology'
        '''
        try:
            self.handle.sendline("")
            self.handle.expect("onos>")
            self.handle.sendline("onos:topology")
            self.handle.expect("onos>")

            handle = self.handle.before

            main.log.info("onos:topology returned: " +
                    str(handle))
            
            return handle
        
        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()
       
    def feature_install(self, feature_str):
        '''
        Installs a specified feature 
        by issuing command: 'onos> feature:install <feature_str>'
        '''
        try:
            self.handle.sendline("")
            self.handle.expect("onos>")

            self.handle.sendline("feature:install "+str(feature_str))
            self.handle.expect("onos>")

            return main.TRUE

        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()
       
    def feature_uninstall(self, feature_str):
        '''
        Uninstalls a specified feature
        by issuing command: 'onos> feature:uninstall <feature_str>'
        '''
        try:
            self.handle.sendline("")
            self.handle.expect("onos>")

            self.handle.sendline("feature:uninstall "+str(feature_str))
            self.handle.expect("onos>")

            return main.TRUE

        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()
        
    def devices(self, grep_str=""):
        '''
        Lists all infrastructure devices
        Optional argument:
            * grep_str - pass in a string to grep
        '''
        try:
            self.handle.sendline("")
            self.handle.expect("onos>")

            if not grep_str:
                self.handle.sendline("devices")
                self.handle.expect("onos>")
            else:
                self.handle.sendline("devices | grep '"+
                        str(grep_str)+"'")
                self.handle.expect("onos>")
           
            handle = self.handle.before
            handle += self.handle.after

            self.handle.sendline("")
            self.handle.expect("onos>")

            handle += self.handle.before
            handle += self.handle.after

            return handle
        except pexpect.EOF:
            main.log.error(self.name + ": EOF exception found")
            main.log.error(self.name + ":    " + self.handle.before)
            main.cleanup()
            main.exit()
        except:
            main.log.info(self.name+" ::::::")
            main.log.error( traceback.print_exc())
            main.log.info(self.name+" ::::::")
            main.cleanup()
            main.exit()


