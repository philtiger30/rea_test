#! /usr/local/bin/python
# author: Lin Bi
# This python scritp will automatically get the username hostname and ssh port 
# It has the same function as installSinatra, but realized by Python
import os
import sys

def printhelp():
    print "Usage: %s <username@host:ssh-port-num>" %sys.argv[0]
    print "Mandatory arguments:"
    print "username@hostname:ssh-port  set the username, hostname and ssh-port to access the target node"
    print "Examples:"
    print "./pyinstallSinatra.py user@hostname:22"
    print "./pyinstallSinatra.py ec2-user@172.31.21.211:9898"

# get the username hostname and ssh port of target node
try:
   attr=sys.argv[1]
except Exception:
 printhelp()
#print 'sys.argv is %s' %attr

def get_param(attr):
    if attr != None:
       if attr.find('@')!= -1:
          userend=attr.find('@')
          user=attr[:userend]
          #print 'user is %s'%user
          if attr.find(':')!=-1:
             hoststart=userend+1
             hostend=attr.find(':')
             host=attr[hoststart:hostend]
             #print 'host is %s' %host
             sshstart=hostend+1
             ssh_port=attr[sshstart:]
             #print 'ssh_port is %s' %ssh_port
             return user,host,ssh_port
          else:
             host=attr[userend+1:]
             #print 'host is %s' %host
             ssh_port='22'
             #print 'default ssh_port is %s' %ssh_port
             return user,host,ssh_port
       printhelp()
       return False
    printhelp()
    return False

# Write ansible inventory file
def main():
  usr, hos, ssh_p=get_param(attr)
#  print "return usr is%s hos is %si sshp is %s" %(usr,hos,ssh_p)
  with open('hosts','a') as hostf:
    hostf.write("[webservers]\n")
    hostf.write("%s:%s   ansible_ssh_user=%s \n" %(hos,ssh_p,usr))
# Write the global variables for ansible group_vars
  with open('group_vars/remoteuser','a') as remoteuserf:
    remoteuserf.write("ssh_user: %s\n" %usr)
    remoteuserf.write("ssh_port: %s\n" %ssh_p)
# execute ansible playbook
  os.system('ansible-playbook -i hosts site.yml')  
# remove the tmp hosts file and remoteuser file
  os.remove('hosts')
  os.remove('group_vars/remoteuser')

if __name__ == '__main__':
  main()

