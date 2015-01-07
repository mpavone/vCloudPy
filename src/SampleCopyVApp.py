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
print ("This sample shows how to copy an entire vApp")
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
filter = {'name':'DESTINATION VAPP'}
vapps= vCloudClient.get_vapp(select=select,  filter=filter)
vCloudClient.print_item(vapps,  select=select)

vapp_href_destination = vapps['href']

print ('\nSelected vApp Source')
print ('----------------------------------')
select = ['name', 'href']
filter = {'name':'SOURCE VAPP'}
vapps= vCloudClient.get_vapp(select=select,  filter=filter)
vCloudClient.print_item(vapps,  select=select)

vapp_href_source= vapps['href']

print ('\nCopy the vapp into the vApp ')
print ('----------------------------------')
task = vCloudClient.copy_vapp(vapp_href_destination,  vapp_href_source, 'this is copied in the destination vApp')
vCloudClient.print_item(task)
vCloudClient.wait_task(task['href'], print_progress=True)
print ('\nCompleted ')




