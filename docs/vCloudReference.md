#vCloud Reference
================

[vCloud (Constructor)](vCloudReference.md#vcloud-constructor)
[vCloud.__extract_info__](vCloudReference.md#vcloudextract_info)
[vCloud.__extract_info_for_element__](vCloudReference.md#vCloudextract_info_for_element)
[vCloud.__extract_info_for_type__](vCloudReference.md#vCloudextract_info_for_type)
[vCloud.recompose_vapp_to_add](vCloudReference.md#vCloudrecompose_vapp_to_add)
[vCloud.set_status](vCloudReference.md#vCloudset_status)
[vCloud.connect](vCloudReference.md#vCloud.connect)
[vCloud.copy_vapp](vCloudReference.md#vCloud.copy_vapp)
[vCloud.copy_vm](vCloudReference.md#vCloud.copy_vm)
[vCloud.delete_request](vCloudReference.md#vCloud.delete_request)
[vCloud.delete_vapp](vCloudReference.md#vCloud.delete_vapp)
[vCloud.disconnect](vCloudReference.md#vCloud.disconnect)
[vCloud.get_catalog](vCloudReference.md#vCloud.get_catalog)
[vCloud.get_catalogItem](vCloudReference.md#vCloud.get_catalogItem)
[vCloud.get_item](vCloudReference.md#vCloud.get_item)
[vCloud.get_network](vCloudReference.md#vCloud.get_network)
[vCloud.get_org](vCloudReference.md#vCloud.vCloud.get_org)
[vCloud.get_request](vCloudReference.md#vCloud.get_request)
[vCloud.get_status](vCloudReference.md#vCloud.get_status)
[vCloud.get_storage_profiles](vCloudReference.md#vCloud.get_storage_profiles)
[vCloud.get_task](vCloudReference.md#vCloud.get_task)
[vCloud.get_vapp](vCloudReference.md#vCloud.get_vapp)
[vCloud.get_vapp_templates](vCloudReference.md#vCloud.get_vapp_templates)
[vCloud.get_vdc](vCloudReference.md#vCloud.get_vdc)
[vCloud.get_vm](vCloudReference.md#vCloud.get_vm)
[vCloud.move_vapp](vCloudReference.md#vCloud.move_vapp)
[vCloud.move_vm](vCloudReference.md#vCloud.move_vm)
[vCloud.new_vapp_from_template](vCloudReference.md#vCloud.new_vapp_from_template)
[vCloud.post_request](vCloudReference.md#vCloud.post_request)
[vCloud.print_item](vCloudReference.md#vCloud.print_item)
[vCloud.reboot_vapp](vCloudReference.md#vCloud.reboot_vapp)
[vCloud.reset_vapp](vCloudReference.md#vCloud.reset_vapp)
[vCloud.reset_vm](vCloudReference.md#vCloud.reset_vm)
[vCloud.shutdown_vapp](vCloudReference.md#vCloud.shutdown_vapp)
[vCloud.shutdown_vm](vCloudReference.md#vCloud.shutdown_vm)
[vCloud.start_vapp](vCloudReference.md#vCloud.start_vapp)
[vCloud.stop_vapp](vCloudReference.md#vCloud.stop_vapp)
[vCloud.stop_vm](vCloudReference.md#vCloud.stop_vm)
[vCloud.suspend_vapp](vCloudReference.md#vCloud.suspend_vapp)
[vCloud.suspend_vm](vCloudReference.md#vCloud.suspend_vm)
[vCloud.undeploy_vapp](vCloudReference.md#vCloud.undeploy_vapp)
[vCloud.wait_task](vCloudReference.md#vCloud.wait_task)


========================================================================================
vCloud (Constructor)
--------------------
vCloud() 

vCloud.__extract_info__
-----------------------
__extract_info__(content, select=None) 

vCloud.__extract_info_for_element__
-----------------------------------
__extract_info_for_element__(content, element, subelement=None, filter=None, select=None) 

vCloud.__extract_info_for_type__
------------------------------------
__extract_info_for_type__(content, type, filter=None, select=None) 

vCloud.__recompose_vapp_to_add__
--------------------------------
__recompose_vapp_to_add__(vapp_href, item_href, description, source_delete=False) 

vCloud.__set_status__
---------------------------------------------------------
__set_status__(code, description, xml=None, request=None) 

vCloud.connect
--------------
connect(org, username, password, endpoint) 

vCloud.copy_vapp
----------------
copy_vapp(vapp_dest_href, vapp_source_href, description) 

vCloud.copy_vm
--------------
copy_vm(vapp_href, vm_href, description) 

vCloud.delete_request
---------------------
delete_request(href) 

vCloud.delete_vapp
------------------
delete_vapp(vm_href)
 
vCloud.disconnect
-----------------
disconnect() 

vCloud.get_catalog
------------------
get_catalog(filter=None, select=None) 

vCloud.get_catalogItem
----------------------
get_catalogItem(catalog_href, filter=None, select=None) 

vCloud.get_item
---------------
get_item(href) 

vCloud.get_network
------------------
get_network(filter=None) 

vCloud.get_org
--------------
get_org() 

vCloud.get_request
------------------
get_request(href) 

vCloud.get_status
------------------
get_status() 

vCloud.get_storage_profiles
--------------------------
get_storage_profiles(vdc_href, filter=None, select=None) 

vCloud.get_task
-----------------
get_task(task_id) 

vCloud.get_vapp
---------------
get_vapp(filter=None, select=None) 

vCloud.get_vapp_templates
-------------------------
get_vapp_templates(filter=None, select=None) 

vCloud.get_vdc
--------------
get_vdc(filter=None, select=None) 

vCloud.get_vm
-------------
get_vm(filter=None, select=None) 

vCloud.is_connected
_------------------
is_connected() 

vCloud.move_vapp
----------------
move_vapp(vapp_dest_href, vapp_source_href, description) 

vCloud.move_vm
--------------
move_vm(vapp_href, vm_href, description) 

vCloud.new_vapp_from_template
-----------------------------
new_vapp_from_template(vdc_href, vapp_template_href, new_vapp_name, new_vapp_description ='') 

vCloud.post_request
-------------------
post_request(href, data=None, headers=None) 

vCloud.print_item
-----------------
print_item(item, select=None, table=False) 

vCloud.reboot_vapp
------------------
reboot_vapp(href) 

vCloud.reboot_vm
----------------
reboot_vm(href) 

vCloud.reset_vapp
-----------------
reset_vapp(href) 

vCloud.reset_vm
---------------
reset_vm(href) 

vCloud.shutdown_vapp
--------------------
shutdown_vapp(href) 

vCloud.shutdown_vm
------------------
shutdown_vm(href) 

vCloud.start_vapp
-----------------
start_vapp(href) 

vCloud.stop_vapp
----------------
stop_vapp(href) 

vCloud.stop_vm
--------------
stop_vm(href) 

vCloud.suspend_vapp
-------------------
suspend_vapp(href) 

vCloud.suspend_vm
-----------------
suspend_vm(href) 

vCloud.undeploy_vapp
--------------------
undeploy_vapp(vapp_href) 

vCloud.wait_task
----------------
wait_task(task_href, print_progress=False) 
