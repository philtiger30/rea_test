Building a simple LAMP stack and deploying Application using Ansible Playbooks.
# author: Lin Bi
-------------------------------------------

Prerequisite:

This deployment script requires Ansible 1.6 or above.
Please deploy this application onto a EC2 Amazon Linux or CentOS. (I just tested the installation on EC2 Amazon Linux)

Requires the target Linux OS support "yum" install command.

Requires the target Linux OS have been imported the publich ssh key from ansible node to allow be accessible via SSH from ansible node.


Usage:

./installSinatra <username@hostname:ssh-port>

This will deploy the whole application package on the target host via ansible. Including apache mod passenger, security and hellp world application.


Mandatory arguments:
username@hostname:ssh-port  set the username, hostname and ssh-port to access the target node

Example:

./installSinatra user@hostname:22

./installSinatra ec2-user@172.31.21.211:9898
 


This deploy script can be on a single node or multiple nodes. The inventory file 'hosts' defines the nodes in which the stacks should be configured.

The deployment will automatically run the command ansible-playbook -i hosts site.yml

Once done, you can check the hello world application results by browsing to the http://hostname
