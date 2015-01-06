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

print ('\nSelected vApp Destination')
print ('----------------------------------')
select = ['name', 'href']
filter = {'name':'newVA2'}
vapps= vCloudClient.get_vapp(select=select,  filter=filter)
vCloudClient.print_item(vapps,  select=select)

vapp_href_destination = vapps['href']

print ('\nSelected vApp Source')
print ('----------------------------------')
select = ['name', 'href']
filter = {'name':'newVA7'}
vapps= vCloudClient.get_vapp(select=select,  filter=filter)
vCloudClient.print_item(vapps,  select=select)

vapp_href_source= vapps['href']

print ('\nCopy the vapp into the vApp ')
print ('----------------------------------')
task = vCloudClient.copy_vapp(vapp_href_destination,  vapp_href_source, 'this is a copied VM2')
vCloudClient.print_item(task)
vCloudClient.wait_task(task['href'], print_progress=True)
print ('\nCompleted ')




