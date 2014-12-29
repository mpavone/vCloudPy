vCloudPy
========

vCloudPy: VMWare vCloud Automation in Pyhon for Devops

The vCloud automation using Python can be done using REST API call, witch encapsulate the input and output parameters in a HTTP call. The REST API calls are well documented by VMWare (http://pubs.vmware.com/vcd-55/index.jsp ), nevertheless the approach to the API is not simple and it requires an enormous amount of work to perform even simple tasks.

The main objective of this project is to make as simple as possible the vCloud automation. The ideas is to create a proxy class functioning as an interface to vCloud REST API.

The proxy class maps parameters to XML elements and the send the HTTP calls over the network. In this way the proxy class frees you from having to communicate at REST API level and allow you to invoke vCloud automation methods using an easy to use Python object.

The project has been created for personal use to learn the VMWare vCloud REST API and to solve specific tasks. At the moment, it has been developed and tested using VMWare vCloud 5.5 and there is no full coverage of the vCloud API but, in the spirit of the Open Source, vCloudPy encourage the community code and feedbacks for future improvements.

License
-------

vCloudPy is released under the [MIT License](http://www.opensource.org/licenses/MIT).
