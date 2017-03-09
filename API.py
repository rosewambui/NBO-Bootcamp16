from urllib.request import urlopen
import json

def get_country_ISOcodes():
	url='http://ws.postcoder.com/pcw/PCW9J-6Q5RS-N76M8-7YCPJ/country'
	request=urlopen(url)
	figure=request.read().decode('utf')
	json_object=json.loads(figure)
	print(json.dumps(json_object))


get_country_ISOcodes()