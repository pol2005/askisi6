import urllib, json
#function to count number of times that one number appears in json file at results array
def count(number,date):
    num_times=0
    k=0
    url = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/'+date+'.json'
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    for results in data['draws']['draw']:
        for i in range(0,20):
            if(data['draws']['draw'][k]['results'][i]==number):
                num_times+=1
        k+=1

    return num_times
date = raw_input("Input a date like 28-01-2016 for results: ")
#print all numbers how many times appear
for i in range(1,81):
    print 'Number ',i,' appears ',count(i,date),' times in results!'
