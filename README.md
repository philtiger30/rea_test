# author: Lin Bi
-------------------------------------------
#Prerequisite:
-------------------------------------------
This deployment script requires Ansible tools on Admin PC.

Please deploy this Sinatra application onto a EC2 Amazon Linux or RHEL 6. (I just tested the installation on EC2 Amazon Linux)

Requires the target Linux OS support "yum" install command.

Requires the target Linux OS have been imported the publich ssh key from ansible Admin PC to allow be accessible via SSH.


#Usage:
-------------------------------------------
(I wrote 2 scripts with both bash shell and python to install Sinatra, you can choose any either of them)

./installSinatra username@hostname:ssh-port

or use python scripts to install

./pyinstallSinatra.py username@hostname:ssh-port

This will deploy the whole application package on the target host via ansible. Including nginx with unicorn, security and hello world application.


Mandatory arguments:

username@hostname:ssh-port      set the username, hostname and ssh-port to access the target node

Example:

./installSinatra user@hostname:22

./installSinatra ec2-user@172.31.21.211:9898

or use python scripts to install

./pyinstallSinatra.py user@hostname:22

This deploy script can be on a single node. The inventory file 'hosts' defines the nodes in which the stacks should be configured.

The deployment will automatically run the command ansible-playbook -i hosts site.yml

Once done, you can check the hello world application results by browsing to the http://hostname

# See the directory "improvements" to get some tips how to improve the deployment
-------------------------------------------

