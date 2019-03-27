import os
import json

visited = set()
res = {
	"base": "http://127.0.0.1/p/archive/",
	"packages": []
}
for path in os.popen('git ls-files|grep /info.json'):
	path = path.split('/')[0]
	if path in visited:
		continue
	visited.add(path)
	info = json.load(open(path + '/info.json', 'rb'))
	del info['entry']
	info['path'] = path
	res['packages'].append(info)
	if os.path.isdir(path):
		os.system('cd %s; zip -r - . > ../archive/%s' % (path, path))


with open('plugins.json', 'wb') as f:
	json.dump(res, f)