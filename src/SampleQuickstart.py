# vCloudPy: VMWare vCloud Automation for Python Devops
# Copyright (c) 2014 Martino Pavone. All Rights Reserved.
#
# Licensed under the MIT License , (the "License"); 
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from vCloud import vCloud

print ("\n--------------------------------------------------------------------")
print ("vCloudPy: VMWare vCloud Automation for Python Devops")
print ("--------------------------------------------------------------------")
print ("This is the sample code used into Quickstart Guide available at the ")
print ("the link below:")
print ("https://github.com/mpavone/vCloudPy/blob/master/docs/QuickstartGuide.md ")
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


