# author: Lin Bi
-------------------------------------------
The general idea to improve the Hellp World app is to use some AWS service to get a robust and redundant deployment in AWS cloud.
Another idea to improve is to use Nagios to monitor the servers and deploy HA proxy for the load sharing.

#Examples on AWS cloud platform: 
-------------------------------------------
Add "-include create_ec2_ins" in your ansible playbook to create AWS EC2 instance with ansible ec2 module.

After you have deployed the Nginx, Ruby APP and securing down the server in the AWS ec2 instance, add "-include create_ami" to bake a new AMI image.

Use create_lc.yml to configure the baked AMI with Launch Configuraiton module.

Use create_asg.yml to create the Auto Scaling Group to deploy new intance automatically in redundant Availablity Zone

Use create_elb.yml to create Elastic Load Balancers as the proxy to sharing the load to many EC2 APP servers.

Use the create_route53_dns.yml to create the new DNS domain name for the Web service.

#Examples to setup the Nagios network monitoring, HA Proxy and Database:
-------------------------------------------
See the examples on "roles" directory to deploy the Nagios network monitoring, HA Proxy and Database. 

