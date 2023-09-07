def getkey(phone):
    from urllib import request, parse
    import json
    import re
    data = parse.urlencode({"to": phone, "limit": 1}).encode()
    # this will make the method "POST"
    req = request.Request(
        "http://api.bonav.xyz:8888/index.php/recordretrieval", data=data)
    resp = request.urlopen(req)
    content = resp.read()
    jsoncontent = json.loads(content)
    msg = jsoncontent[0]['msg'].strip(" ")
    msg = re.sub(' +', ' ', msg)
    if len(msg) > 0:
        print("record found.")
        print("OTP: "+msg.split(" ")[1])
        return msg.split(" ")[1]
    else:
        print("no record.")
        return ""


getkey('67074050130')
