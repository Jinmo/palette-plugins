import pkg.env as env
import urllib
import os

MSI_URL = 'https://github.com/keystone-engine/keystone/releases/download/0.9.1/keystone-0.9.1-python-win64.msi'
MSI_NAME = 'keystone-0.9.1-python-win64.msi'
try:
	from keystone import Ks
	print 'keystone-engine is already installed! Skipping...'
except ImportError:
	print 'Instaling keystone-engine...'
	if env.os == 'win':
		urllib.urlretrieve(MSI_URL, MSI_NAME)
		assert not os.system('msiexec /passive /i %s' % MSI_NAME)
	else:
		assert not os.system('pip install keystone-engine')
	from keystone import Ks
	pass