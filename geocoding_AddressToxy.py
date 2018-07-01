import  requests
import  json
import  re


fo = open(r'C:\Users\GYY20170605\AppData\Local\Programs\Python\Python36\python code\企业.txt','r',encoding= 'utf-8')
fw = open(r'C:\Users\GYY20170605\AppData\Local\Programs\Python\Python36\python code\out_企业.txt','w',  encoding= 'utf-8')
lines = fo.readlines()

for line in lines:
    try:
        id_resaddr = line.split('\t')
        id = id_resaddr[0]
        resaddr = id_resaddr[1].split('\n')
        res_addr = resaddr[0]
        url = 'http://api.map.baidu.com/geocoder/v2/?address=' + res_addr + '&city=郑州市&output=json&ak=nYeiVdUjQqGkOEWG0zaLtCj1eS4asjZj&callback=showLocation&qq-pf-to=pcqq.c2c'
        response = requests.get(url)
        response.encoding = 'utf-8'
        test = response.text
        print(test)
        r = test.split('(')
        r2 = r[1].split(')')
        dict = eval(r2[0])
        info = dict.get('result')
        location = info.get('location')
        lat = location.get('lat')
        lng = location.get('lng')
        confidence = info.get('confidence')
        precise = info.get('precise')
        fw.write(id)
        fw.write('\t')
        fw.write(res_addr)
        fw.write('\t')
        fw.write(str(lng))
        fw.write('\t')
        fw.write(str(lat))
        fw.write('\t')
        fw.write(str(precise))
        fw.write('\t')
        fw.write(str(confidence))
        fw.write('\n')
    except Exception:
        print (line)
        continue




