import twstock
rt = twstock.realtime.get('2345')
if(rt['success']):
    print(rt)
else:
    print('error')