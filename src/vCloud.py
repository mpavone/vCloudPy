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

import base64
import requests
import time
import xml.etree.ElementTree as ET

class vCloud(object):
    
    def __init__(self):
        self.login = None
        self.headers = None
        self.endpoint = None
        self.org_href = None
        self.status = {'code':0, 'description':'ok',  'xml':'', 'request':None}

    def __extract_info__(self, content, select=None):
        ret = {}
        root = ET.fromstring(content)
        
        if select == None :
            for k,v in root.attrib.iteritems():
                ret[k] = str(v)
        else :
                for k in select :
                    if  root.attrib.has_key(k) :  ret[k] = root.attrib[k]            
            
        ret['xml'] = content
           
        return ret
        
    def __extract_info_for_type__(self,  content,  type, filter=None, select=None):
        ret = []
        root = ET.fromstring(content)
        for child in root:
            if  child.attrib.has_key('type') :
                if child.attrib['type'] == type : 
                    include = True
                    if filter is not None :  
                        for f in filter:
                            if  child.attrib.has_key(f) :
                                if child.attrib[f] != filter[f] : 
                                    include = False
                                    break
                            else :
                                include = False
                                break
                    if include :
                        retItem = {};
                        if select is None :
                            for k,v in child.attrib.iteritems():
                                retItem[k] = str(v)
                        else :
                            for k in select :
                                if  child.attrib.has_key(k) :  retItem[k] = child.attrib[k]
                        ret.append(retItem) 
                        
        if len(ret) == 1 :
            ret = ret[0]
        elif len(ret) == 0 :
            ret = {}
        return ret   

    def __extract_info_for_element__(self,  content,  element, subelement=None, filter=None,  select=None):
        ret = []
        root = ET.fromstring(content)
        for child in root:
            if child.tag == element:
                if subelement == None :
                    include = True
                    if filter is not None :  
                        for f in filter:
                            if  child.attrib.has_key(f) :
                                if child.attrib[f] != filter[f] : 
                                    include = False
                                    break
                            else :
                                include = False
                                break
                    if include : 
                        retItem = {};
                        if select is None :
                            for k,v in child.attrib.iteritems():
                                retItem[k] = str(v)
                        else :
                            for k in select :
                                if  child.attrib.has_key(k) :  retItem[k] = child.attrib[k]
                        ret.append(retItem)                        
                else :
                    for subchild in child :
                        include = True
                        if filter is not None :  
                            for f in filter:
                                if  subchild.attrib.has_key(f) :
                                    if subchild.attrib[f] != filter[f] : 
                                        include = False
                                        break
                                else :
                                    include = False
                                    break
                        if include : 
                            retItem = {};
                            if select is None :
                                for k,v in subchild.attrib.iteritems():
                                    retItem[k] = str(v)
                            else :
                                for k in select :
                                    if  subchild.attrib.has_key(k) :  retItem[k] = subchild.attrib[k]
                            ret.append(retItem) 
        if len(ret) == 1 :
            ret = ret[0]
        elif len(ret) == 0 :
            ret = {}
        return ret

    def connect(self, org, username,  password, endpoint):
        'Connect to vCloud server'
        self.endpoint = endpoint
        self.login = {'Accept':'application/*+xml;version=5.1', \
                   'Authorization':'Basic  '+ base64.b64encode(username + "@" + org + ":" + password)}

        p = requests.post(self.endpoint + 'sessions', headers = self.login)

        self.headers = {'Accept':'application/*+xml;version=5.1'}

        for k,v in p.headers.iteritems():
                if k == "x-vcloud-authorization" : self.headers[k]=v

        self.get_org()

    def is_connected(self):
        'Check if the connection to vCloud is estabilished'
        is_connected = (self.headers != None)
        
        return is_connected;
        
    def disconnect(self):
        self.login = None
        self.headers = None
        self.endpoint = None
        self.org_href = None
        
        #TODO: logout from vCloud

    def __set_status__(self, code, description, xml=None, request=None) :
        self.status['code']=code
        self.status['description']=description
        self.status['xml']=xml
        
        req = {}
        req['url']=request.url
        req['method']=request.method
        req['headers']=request.headers
        req['body']=request.body
        self.status['request']=req
        
    def get_request (self, href) :
        is_ok = True
        
        if not(self.is_connected()) :
            self.__set_status__(code=-1, description='Not Connected')
            result = None
            
        if is_ok :    
            result = requests.get(href, data=None, headers = self.headers)
            #TODO: the description must be taken form the attribute Message
            self.__set_status__ (result.status_code, result.reason, xml=result.content, request=result.request )
            is_ok = result.ok
                
        if not(is_ok) : result = None    
        return result        
        
    def post_request (self,  href,  data=None, headers=None) :
        is_ok = True
        
        if not(self.is_connected()) :
            self.__set_status__(code=-1, description='Not Connected')
            is_ok = False
            
        if is_ok :    
            if headers == None :
                post_headers = self.headers
            else :
                post_headers = dict(headers.items() + self.headers.items())
            result = requests.post(href, data=data, headers=post_headers)
            #TODO: the description must be taken form the attribute Message            
            self.__set_status__ (result.status_code, result.reason, xml=result.content, request=result.request )
            is_ok = result.ok 
 
        if not(is_ok) : result = None 
        return result

    def delete_request (self, href) :
        is_ok = True
        
        if not(self.is_connected()) :
            self.__set_status__(code=-1, description='Not Connected')
            result = None
            
        if is_ok :    
            result = requests.delete(href, data=None, headers = self.headers)
            #TODO: the description must be taken form the attribute Message            
            self.__set_status__ (result.status_code, result.reason, xml=result.content, request=result.request )
            is_ok = result.ok
                
        if not(is_ok) : result = None    
        return result        

    def get_status(self):
        
        return self.status

#TODO: multi-organization
    def get_org(self):
        is_ok = True
        g= self.get_request(self.endpoint + 'org')
        is_ok = not(g==None)

        result = {}
        if is_ok : 
            root = ET.fromstring(g.content)
            
            for child in root:
                for k,v in child.attrib.iteritems():
                    result[k] = str(v)
    
            self.org_href = result["href"]
            g= self.get_request(self.org_href)
            is_ok = not(g==None)
            if is_ok : 
                root = ET.fromstring(g.content)
                for child in root:
                    if child.tag == '{http://www.vmware.com/vcloud/v1.5}FullName': 
                        result['FullName'] = child.text
                        
        if not(is_ok) : result = None
        return result
        
    def get_vdc(self,  filter=None, select=None ):
        is_ok = True
            
        g= self.get_request(self.org_href)
        is_ok = not(g==None)

        if is_ok :
            result = self.__extract_info_for_type__(g.content, 'application/vnd.vmware.vcloud.vdc+xml', filter, select)                

        if not(is_ok) : result = None
        return result

    def get_catalog(self,  filter=None, select=None):
        is_ok = True
            
        g= self.get_request(self.org_href)
        is_ok = not(g==None)
        
        if is_ok :
            result = self.__extract_info_for_type__(g.content, 'application/vnd.vmware.vcloud.catalog+xml', filter, select)    

        if not(is_ok) : result = None
        return result
        
    def get_catalogItem(self, catalog_href, filter=None, select=None):
        is_ok = True
            
        g= self.get_request(catalog_href)
        is_ok = not(g==None)        
        
        if is_ok :
            result = self.__extract_info_for_element__(g.content, '{http://www.vmware.com/vcloud/v1.5}CatalogItems', '{http://www.vmware.com/vcloud/v1.5}CatalogItem',  filter=filter,  select=select )   

        if not(is_ok) : result = None
        return result
        
    def get_storageProfiles(self, vdc_href, filter=None, select=None):
        is_ok = True
            
        g= self.get_request(vdc_href)
        is_ok = not(g==None)        
        
        if is_ok :
            result = self.__extract_info_for_element__(g.content, '{http://www.vmware.com/vcloud/v1.5}VdcStorageProfiles', '{http://www.vmware.com/vcloud/v1.5}VdcStorageProfile',  filter=filter,  select=select )   

        if not(is_ok) : result = None
        return result

    def get_network(self,  filter=None):
        is_ok = True
            
        g= self.get_request(self.org_href)
        is_ok = not(g==None)
        
        if is_ok :
            result = self.__extract_info_for_type__(g.content, 'application/vnd.vmware.vcloud.orgNetwork+xml', filter) 

        if not(is_ok) : result = None
        return result
        
    def get_vapp(self, filter=None, select=None):
        is_ok = True
            
        g= self.get_request(self.endpoint + 'vApps/query')
        is_ok = not(g==None)        

        if is_ok :
            result = self.__extract_info_for_element__(g.content, '{http://www.vmware.com/vcloud/v1.5}VAppRecord',  filter=filter,  select=select ) 

        if not(is_ok) : result = None
        return result
        
    def get_vapp_templates(self, filter=None, select=None):
        is_ok = True
            
        g= self.get_request(self.endpoint + '/vAppTemplates/query')
        is_ok = not(g==None)        
        
        if is_ok :
            result = self.__extract_info_for_element__(g.content, '{http://www.vmware.com/vcloud/v1.5}VAppTemplateRecord',  filter=filter,  select=select ) 

        if not(is_ok) : result = None
        return result

    def get_vm(self, filter=None, select=None):
        is_ok = True
            
        g= self.get_request(self.endpoint + 'vms/query')
        is_ok = not(g==None) 
        
        if filter == None :
            filter = {}
        filter['isVAppTemplate']='false'
        
        if is_ok :
            result = self.__extract_info_for_element__(g.content, '{http://www.vmware.com/vcloud/v1.5}VMRecord',  filter=filter,  select=select )  

        if not(is_ok) : result = None
        return result
        
    def delete_vapp(self, vm_href):
        is_ok = True
            
        delete= self.delete_request(vm_href)
        is_ok = not(delete==None) 
        
        if is_ok :
            select = ['name', 'id', 'href']
            result = self.__extract_info__(delete.text, select=select)

        if not(is_ok) : result = None
        return result

    def undeploy_vapp(self, vapp_href):
        is_ok = True
        post_headers={}
        post_headers['Content-Type']='application/vnd.vmware.vcloud.undeployVAppParams+xml'
        
        xml = """<?xml version="1.0" encoding="UTF-8"?>
                <UndeployVAppParams
                xmlns="http://www.vmware.com/vcloud/v1.5">
                <UndeployPowerAction>powerOff</UndeployPowerAction>
                </UndeployVAppParams>"""

        post = self.post_request (vapp_href + '/action/undeploy',  data=xml, headers=post_headers)
        is_ok = not(post==None) 
        
        if is_ok :
            select = ['name', 'id', 'href']
            result = self.__extract_info__(post.text, select=select)
        if not(is_ok) : result = None
        return result        

#TODO: method __recompose_vapp_to_remove__
    def __recompose_vapp_to_add__(self, vapp_href, item_href, description, source_delete=False ):
        is_ok = True
        post_headers={}
        post_headers['Content-Type']='application/vnd.vmware.vcloud.recomposeVAppParams+xml'
        
        if (source_delete) :
            source_delete_text = "true"
        else :
            source_delete_text = "false"
        
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                    <RecomposeVAppParams
                        xmlns="http://www.vmware.com/vcloud/v1.5"
                        xmlns:ns2="http://schemas.dmtf.org/ovf/envelope/1"
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                        xmlns:ovf="http://schemas.dmtf.org/ovf/envelope/1"
                        xmlns:environment_1="http://schemas.dmtf.org/ovf/environment/1">
                    <Description> "%s" </Description>
                    <SourcedItem sourceDelete="%s">
                        <Source href="%s"/>
                    </SourcedItem>
                    <AllEULAsAccepted>true</AllEULAsAccepted>
                    </RecomposeVAppParams>""" % (description, source_delete_text,  item_href)
                    
        post = self.post_request (vapp_href + '/action/recomposeVApp',  data=xml, headers=post_headers)
        is_ok = not(post==None) 
        
        if is_ok :
            select = ['name', 'id', 'href']
            result = self.__extract_info__(post.text, select=select)
        if not(is_ok) : result = None
        return result

    def copy_vm(self, vapp_href,  vm_href, description):
        
        return self.__recompose_vapp_to_add__(vapp_href, vm_href, description, False )
        
    def copy_vapp(self, vapp_dest_href,  vapp_source_href, description):
        
        return self.__recompose_vapp_to_add__(vapp_dest_href, vapp_source_href, description, False )
        
    def move_vm(self, vapp_href,  vm_href, description):
        
        return self.__recompose_vapp_to_add__(vapp_href, vm_href, description, True )
                
    def move_vapp(self, vapp_dest_href,  vapp_source_href, description):
        
        return self.__recompose_vapp_to_add__(vapp_dest_href, vapp_source_href, description, True )

    def new_vapp_from_template(self, vdc_href, vapp_template_href,  new_vapp_name, new_vapp_description ='' ):
        is_ok = True
        post_headers={}
        post_headers['Content-Type']='application/vnd.vmware.vcloud.instantiateVAppTemplateParams+xml'
        
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <InstantiateVAppTemplateParams
                    xmlns="http://www.vmware.com/vcloud/v1.5"
                    xmlns:ovf="http://schemas.dmtf.org/ovf/envelope/1"
                    name="%s"
                    deploy="true"
                    powerOn="true">
                <Description>%s</Description>
                <Source href="%s"/>
                </InstantiateVAppTemplateParams>""" % (new_vapp_name, new_vapp_description,  vapp_template_href)
                    
        post = self.post_request(vdc_href + '/action/instantiateVAppTemplate', data=xml, headers=post_headers)
        is_ok = not(post==None) 
        
        if is_ok :
            select = ['name', 'id', 'href']
            result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   

        if not(is_ok) : result = None
        return result

    def get_task(self, task_id):
        is_ok = True
            
        get= self.get_request(self.org_href)
        is_ok = not(get==None)

        if is_ok :
            tasks = self.__extract_info_for_type__(get.content, 'application/vnd.vmware.vcloud.tasksList+xml')                
            is_ok = not(tasks==None)

        if is_ok :
            if type(tasks) == list :
                for task in tasks :
                    get_task = self.get_request(task['href'])
                    select = ['name', 'id', 'href']
                    filter ={'id':task_id}
                    result = self.__extract_info_for_element__(get_task.content, '{http://www.vmware.com/vcloud/v1.5}Task',  filter=filter,  select=select )   
                    if result != {} : break 
            else :
                get_task = self.get_request(tasks['href'])
                is_ok = not(get_task==None)
            
            if is_ok :
                select = ['name', 'id', 'href']
                filter ={'id':task_id}
                result = self.__extract_info_for_element__(get_task.content, '{http://www.vmware.com/vcloud/v1.5}Task',  filter=filter,  select=select )   
     
        if not(is_ok) : result = None
        return result
        

    def wait_task(self, task_href,  print_progress=False):
        is_ok = True
        
        x=0
        while (x == 0):
            time.sleep(5)
            get = self.get_request(task_href)
            is_ok = not(get==None) 
            
            if is_ok :
                root = ET.fromstring(get.content)
                found_progress = False
                for child in root.iter():
                    if child.tag == "{http://www.vmware.com/vcloud/v1.5}Progress" :
                        if print_progress : print("Progress:"+ child.text)
                        if child.text == '100' : x = 1
                        found_progress = True
                if not(found_progress) : x=1

        if is_ok :
            time.sleep(5)
            result = True
        
        if not(is_ok) : result = None
        return result
        
    def stop_vm(self, href):
        post = self.post_request(href + '/power/action/powerOff')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def reboot_vm(self, href):
        post = self.post_request(href + '/power/action/reboot')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
                
    def reset_vm(self, href):
        post = self.post_request(href + '/power/action/reset')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def shutdown_vm(self, href):
        post = self.post_request(href + '/power/action/shutdown')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def suspend_vm(self, href):
        post = self.post_request(href + '/power/action/suspend')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def start_vapp(self, href):
        post = self.post_request(href + '/power/action/powerOn')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def stop_vapp(self, href):
        post = self.post_request(href + '/power/action/powerOff')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def reboot_vapp(self, href):
        post = self.post_request(href + '/power/action/reboot')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def reset_vapp(self, href):
        post = self.post_request(href + '/power/action/reset')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def shutdown_vapp(self, href):
        post = self.post_request(href + '/power/action/shutdown')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result
        
    def suspend_vapp(self, href):
        post = self.post_request(href + '/power/action/suspend')
        select = ['name', 'id', 'href']
        result = self.__extract_info_for_element__(post.text, '{http://www.vmware.com/vcloud/v1.5}Tasks', '{http://www.vmware.com/vcloud/v1.5}Task', select=select )   
     
        return result

#TODO: method create_snapshot
#TODO: method revert_snapshot
    def get_item(self, href):
        is_ok = True
            
        g= self.get_request(href)
        is_ok = not(g==None) 
        
        if is_ok :
            result = self.__extract_info__(g.content)

        if not(is_ok) : result = None
        return result        

    def print_item(self, item, select=None,  table=False):
        if item == None : return
        
        cols={}
        
        if select is None :
            if type(item) is list :
                cols = item[0].keys()
            else :
                cols = item.keys()
        else :
            cols = select

        f = ''
        if table :     
            for k in cols :
                f = f + '{0[' + k +']:15} ' 
            n = dict(zip(cols, cols))
            print (f.format(n))
        
        if type(item) is list :
            for i in item :
                f=''
                for k in cols :
                    if i.has_key(k) :
                        if table :
                            f = f + '{0[' + k +']:15} ' 
                        else :
                            f = f + k + ': {0[' + k +']:15} \n'
                    else :
                        if table :
                            f = f + '                '
                        else :
                            f = f + k + ':  '
                print (f.format(i))
        else :
            for k in cols :
                if item.has_key(k) :
                    f =  k + ': {0[' + k +']:15} '
                    print (f.format(item))
                else :
                    f =  '               '        

    
