from vCloud import vCloud

print ("\n--------------------------------------------------------------------")
print ("vCloudPy: VMWare vCloud Automation in Pyhon for Devops ")
print ("--------------------------------------------------------------------")

vCloudClient = vCloud()

# credentials and endpoint
username 	= 'admin'
org      	= 'ACME'
password 	= '***change me***'
endpoint 	= 'https://admin.dc1.acme.it/api/'

#Step 1: logon into vCloud
vCloudClient.connect(org, username, password, endpoint)

#Step 2: retrieve organization's info
org =vCloudClient.get_org()
print ('Connected to the following organization...\n')
vCloudClient.print_item(org)

#Step 3: list vms
vms=vCloudClient.get_vm()

vCloudClient.print_item(vms)

#Step 4: print only selected properties
select=['name','status','href']
vCloudClient.print_item(vms,  select=select)

#Step 5: print only selected properties in table format
select=['name','status', 'href']
vCloudClient.print_item(vms,  select=select,  table=True)

#Step 6: retieve only the name and href of all powered off vm
print("--------------------------------------------------------------------")
print("Suspended VMs\n")

select=['name','status', 'href']
filter={'status':'SUSPENDED'}
vms_suspended =vCloudClient.get_vm(select=select,  filter=filter) 
vCloudClient.print_item(vms_suspended, select=select,  table=True) # select parameter just to order the columns

#Step 7: start all powered off vm
for vm in vms_suspended :
    vCloudClient.start_vm(vm['href'])

#vCloudClient.suspend_vm('https://admin01.dc1.private.cloud.it/api/vApp/vm-fbce3b00-c5a3-4afb-ab59-d64cc76df5dd')
 
#vCloudClient.suspend_vm('https://admin01.dc1.private.cloud.it/api/vApp/vm-91b6e0ad-2aa9-422d-b41f-14048b206468')


