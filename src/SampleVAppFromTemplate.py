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
print ("This sample shows how to create a new vApp from a template")
print ("--------------------------------------------------------------------")

vCloudClient = vCloud()

# credentials and endpoint
username 	= 'admin'
org      	= 'ACME'
password 	= '***change me***'
endpoint 	= 'https://admin.dc1.acme.it/api/'


vCloudClient.connect(org, username, password, endpoint)

print ('\nVirtual Datacenter where you want to create the new vApp')
print ('----------------------------------------------------------')
filter={'name': 'vdc1-acme'}
vdc = vCloudClient.get_vdc(filter=filter)
vCloudClient.print_item(vdc)


print ('\nvApp Templates list ')
print ('----------------------------------------------------------')
vappTemplate = vCloudClient.get_vapp_templates()
select = ['name', 'href', 'catalogName', 'ownerName' ]
vCloudClient.print_item(vappTemplate,  select=select)

print ('\nNew vApp based on the first tamplate in the selected vdc')
print ('----------------------------------------------------------')
task =vCloudClient.new_vapp_from_template(vdc['href'],vappTemplate[0]['href'], 'newVA16')
vCloudClient.print_item(task)

print ('\nWaiting until the task is completed.......')
vCloudClient.wait_task(task['href'])

print ('\nList all vApps')
print ('----------------------------------------------------------')
vapps= vCloudClient.get_vapp()
select = ['name', 'href']
vCloudClient.print_item(vapps, select=select, table=True)



