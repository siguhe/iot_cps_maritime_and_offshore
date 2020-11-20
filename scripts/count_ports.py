import shodan

SHODAN_API_KEY = "APIKEY"

api = shodan.Shodan(SHODAN_API_KEY)


# Wrap the request in a try/ except block to catch errors
# Search Shodan
results = api.search('isp:tampnet')

# Show the results
ports = dict()

print('Results found: {}'.format(results['total']))
for result in results['matches']:
    port = result['port']
    if(port not in ports):
        ports.update({port:0}) 
    prev_number = ports[port]
    ports.update({port:prev_number+1})

print({key: value for key, value in sorted(ports.items(), key=lambda item: item[1])})
