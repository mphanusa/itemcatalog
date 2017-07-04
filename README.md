# Item Catalog

A full stack application keeps track of categories and its items.   As an example, some major music categories are configured.  In each of these categories, there will be some popular titles accompanied by its artists.  Only creators of titles can edit or delete.   The application uses Google Authentication System to keep track of creators of titles.   Authenticated users can add new titles/items.

The application has 2 major components: a frontend that users interact with and a backend that where categories, items, and web pages are maintained and generated.

## Set Up

## Prerequisites
Requires python, flask, pip, and git, html/css boostraps.

## How to Install
- Install Vagrant and VirtualBox
- Clone the fullstack-nanodegree-vm
- Configure Vagrantfile to enable DNS:
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end
- Launch the Vagrant VM (vagrant up)
- start up a shell: vagrant ssh
- Change directory to vagrant
- Download and install this program issuing the following command:
`git clone https://github.com/mphanusa/itemcatalog.git`
- Change directory to *itemcatalog*.
- Run the db initializer:
`python initialize_db.py`
- Run the itemcatalog application
`python application.py`
- Access and test the application by using a browser with the url:
`http://localhost:8000`

## How to Use Google Authentication Services
Since Google Login with your Goolge user name and password will be used, you will need to supply a client_secrets.json file. This file can be downloaded after creating a Google credentials https://console.developers.google.com/apis.  Click Credentials, select Web Application, type Catalog App in Name, http://localhost:8000 in Authorized JavaScript origins, http://localhost:8000 in Authorized redirect URIs. Click Create.  Client id needs to be updated in the login.html.

After creating and downloading your client_secrets.json file, move it to the itemcatalog directory so it is accessible to the itemcatalog application.
