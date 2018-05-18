#!/usr/bin/env python

import sys,argparse,os
import requests


def main(argv):

    global target
    parser = argparse.ArgumentParser(
        description='Drupal Exploit with Subdomain ')
    parser.add_argument('-t', '--target', help='target url', required=True)
    args = parser.parse_args()

    target = args.target

if __name__ == "__main__":
    main(sys.argv[1:])

http_proxy = "138.201.223.250:31288"

proxyDict = {"http":http_proxy}

hostsearch = "http://api.hackertarget.com/hostsearch/?q=" + target

response = requests.get(hostsearch, headers={'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'},proxies=proxyDict)

hosts_ips = response.text

filename = "results.txt"

f = open(filename,'w')

f.write(hosts_ips)

f.close()

cwd = os.getcwd()

with open(filename) as file:

    content = file.readlines()

result = []

for line in content:

        result.append(line.split(',')[0])

print result

print ("Scan results -> {}/{}").format(cwd,filename)
