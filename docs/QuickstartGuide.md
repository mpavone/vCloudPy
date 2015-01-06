Quickstart Guide
================

Before diving in the ins and outs of the proxy class, this section hepls to learn the basic concepts and start working with vCloudPy immediately.

The main object of vCloudPy is the proxy class vCloud. It implements all the interfaces to interact with VMWare vCloud.

Let's instantiate it:

```
#Required to import the vCloud class
from vCloud import vCloud

vCloudClient = vCloud()
```

vCloudClient instance implements all the methods to work with VMWare vCloud.
Anyway, before to call any method it is required to connect the proxy.
The connection requires three parameters:

*	user account: 	the account in VMWare vCloud DC
*	password: 	the account's password
*	organization:	the organization name
*	endpoint:	the endpoint URL


username 	= 'admin'
org      		= 'acme'
password 	= 'changeME'
endpoint 	= 'https://admin.dc.private.acme.it/api/'

#logon into vCloud
vCloudClient.connect(org, username, password, endpoint)

Now, you are connected to vCloud than you can start using all the method exposed by vCloudClient. Fist of all, let's retrieve organizations's info:

org =vCloudClient.get_org()

org is a dictionary containing the organization's info.
With the following command you can retrieve the organization's properties.

org.keys()

result: ['FullName', 'href', 'type', 'name']

Then use the command below to get a value:

org['name']

Better, you can use the method  print_item to have a formated print all the values:

print ('Connected to the following organization...\n')
vCloudClient.print_item(org)


Now, suppose that you want to retrieve and print the complete list of VM:

vms=vCloudClient.get_vm()
vCloudClient.print_item(vms)

IMPORTANT: all the methods return a single dictionay item if only one item is retrieved; otherwise, a list of dictionaries.
 
A lot of info are displayed, let print only name, status and href:

select=['name','status','href']
vCloudClient.print_item(vms,  select=select)

Much better, but a table presentation would be more appropriate:

vCloudClient.print_item(vms,  select=select,  table=True)

It is also possible to retrieve a filter the list of vm by properties

select=['name','status', 'href']   # you are interested only into name, status and href properties
filter={'status':'POWERED_OFF'} # you want only the list of  POWERED_OFF vms
vms_suspended =vCloudClient.get_vm(select=select,  filter=filter) 

then you can display them:

vCloudClient.print_item(vms_suspended, select=select,  table=True) # in this case the select argument is required just to order the columns.

for vm in vms_suspended :
    vCloudClient.start_vm(vm['href'])
