# -*- coding: utf-8 -*-
from MaltegoTransform import *
import requests
import json

apikey = "<Your API Key>"
secret = "<Your Secret>"
apiurl = "https://" + apikey + ":" + secret + "@www.hybrid-analysis.com/api/"


# hash_to_c2host
def hash_to_c2host():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'domains' in r:
                    for item in r['domains']:
                        me = mt.addEntity("maltego.Domain", '%s' % item)
                        me.setLinkLabel("HA")

    except:
        pass

    return mt

# hash_to_c2ip
def hash_to_c2ip():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'hosts' in r:
                    for item in r['hosts']:
                        me = mt.addEntity("maltego.IPv4Address", '%s' % item)
                        me.setLinkLabel("HA")

    except:
        pass

    return mt

# hash_to_filename
def hash_to_filename():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'submitname' in r:
                    me = mt.addEntity("maltego.Phrase", '%s' % r['submitname'].encode("utf-8"))
                    me.setLinkLabel("HA")

    except:
        pass

    return mt

# hash_to_md5
def hash_to_md5():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'md5' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['md5'])
                    me.setLinkLabel("HA")

    except:
        pass

    return mt

# hash_to_sha256
def hash_to_sha256():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA")

    except:
        pass

    return mt

# hash_to_label
def hash_to_label():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'vxfamily' in r:
                    me = mt.addEntity("maltego.Avdetection", '%s' % r['vxfamily'])
                    me.setLinkLabel("HA Label")

    except:
        pass

    return mt

# hash_to_threatscore
def hash_to_threatscore():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'threatscore' in r:
                    me = mt.addEntity("maltego.Phrase", '%s' % r['threatscore'])
                    me.setLinkLabel("HA Threat Score")

    except:
        pass

    return mt

# hash_to_tag
def hash_to_tag():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'classification_tags' in r:
                    for item in r['classification_tags']:
                        me = mt.addEntity("maltego.Phrase", '%s' % item)
                        me.setLinkLabel("HA Tag")

    except:
        pass

    return mt

# hash_to_filetype
def hash_to_filetype():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'type' in r:
                    me = mt.addEntity("maltego.Phrase", '%s' % r['type'])
                    me.setLinkLabel("HA")

    except:
        pass

    return mt


# hash_to_similar
def hash_to_similar():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'search?query=similar-to:' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']['result']:
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA similar-to")

    except:
        pass

    return mt

# c2host_to_hash
def c2host_to_hash():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'search?query=domain:' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']['result']:
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA")

    except:
        pass

    return mt

# c2ip_to_hash
def c2ip_to_hash():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'search?query=host:' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']['result']:
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA")

    except:
        pass

    return mt

# label_to_hash
def label_to_hash():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'search?query=vxfamily:' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']['result']:
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA")

    except:
        pass

    return mt

# authentihash_to_hash
def authentihash_to_hash():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'search?query=authentihash:' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']['result']:
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA")

    except:
        pass

    return mt

# tag_to_hash
def tag_to_hash():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'search?query=tag:' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 0:
            for r in response_json['response']['result']:
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA")

    except:
        pass

    return mt

# hash_to_all
def hash_to_all():
    try:
        headers = {'User-Agent': 'Falcon'}
        response = requests.get(apiurl + 'scan/' + data, headers=headers)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        response2 = requests.get(apiurl + 'search?query=similar-to:' + data, headers=headers)
        response_json2 = response2.json()
        respcode2 = int(response_json2['response_code'])

        if respcode == 0:
            for r in response_json['response']:
                if 'domains' in r:
                    for item in r['domains']:
                        me = mt.addEntity("maltego.Domain", '%s' % item)
                        me.setLinkLabel("HA")
                if 'hosts' in r:
                    for item in r['hosts']:
                        me = mt.addEntity("maltego.IPv4Address", '%s' % item)
                        me.setLinkLabel("HA")
                if 'submitname' in r:
                    me = mt.addEntity("maltego.Phrase", '%s' % r['submitname'].encode("utf-8"))
                    me.setLinkLabel("HA")
                if 'md5' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['md5'])
                    me.setLinkLabel("HA")
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA")
                if 'vxfamily' in r:
                    me = mt.addEntity("maltego.Avdetection", '%s' % r['vxfamily'])
                    me.setLinkLabel("HA Label")
                if 'threatscore' in r:
                    me = mt.addEntity("maltego.Phrase", '%s' % r['threatscore'])
                    me.setLinkLabel("HA Threat Score")
                if 'classification_tags' in r:
                    for item in r['classification_tags']:
                        me = mt.addEntity("maltego.Phrase", '%s' % item)
                        me.setLinkLabel("HA Tag")
                if 'type' in r:
                    me = mt.addEntity("maltego.Phrase", '%s' % r['type'])
                    me.setLinkLabel("HA")

        if respcode2 == 0:
            for r in response_json2['response']['result']:
                if 'sha256' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['sha256'])
                    me.setLinkLabel("HA similar-to")

    except:
        pass

    return mt



# main
func = sys.argv[1]
data = sys.argv[2]

mt = MaltegoTransform()
mresult = eval(func)()
mresult.returnOutput()

