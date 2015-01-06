from vCloud import vCloud

print ("\n--------------------------------------------------------------------")
print ("vCloudPy: VMWare vCloud Pyhon SDK for Devops ")
print ("--------------------------------------------------------------------")

vCloudClient = vCloud()

# credentials and endpoint
username 	= 'admin'
org      	= 'ACME'
password 	= '***change me***'
endpoint 	= 'https://admin.dc1.acme.it/api/'


vCloudClient.connect(org, username, password, endpoint)

print ('\nSelected vApp')
print ('----------------------------------')
select = ['name', 'href']
filter = {'name':'newVA1'}
vapps= vCloudClient.get_vapp(select=select,  filter=filter)
vCloudClient.print_item(vapps,  select=select)

vapp_href = vapps['href']

print ('\nSelected vm ')
print ('----------------------------------')
vms= vCloudClient.get_vm()
select = ['name', 'href', 'containerName']
filter = {'containerName':'newVA8'}
vCloudClient.print_item(vms[0],  select=select)

vm_href = vms[0]['href']

print ('\nMove the vm into the vApp ')
print ('----------------------------------')
task = vCloudClient.copy_vm(vapp_href,  vm_href, 'this is a copied VM2')
vCloudClient.print_item(task)
vCloudClient.wait_task(task['href'])
print ('\nCompleted ')


