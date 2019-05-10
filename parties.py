import csv
import pprint
from collections import defaultdict


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    del bar_list[0]
    return bar_list


def print_data(data):
    for entry in data:
        print(entry)
        pprint.pprint(entry)


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    noisiest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    ##count calls
    num_city_calls = defaultdict(int)
    num_borough_calls= defaultdict(int)
    for d in data:
      num_city_calls[d['city']] += int((d['num_calls']))
      num_borough_calls[d['borough']] += int((d['num_calls']))

    ##get noisiest_city_and_borough
    for k, v in num_city_calls.items():
      max_city_value = max(num_city_calls.values())
      if v == max_city_value :
        max_city_key = k

    for k,v in num_borough_calls.items():
      max_borough_value = max(num_borough_calls.values())
      if v == max_borough_value :
        max_borough_key = k

    noisiest_city_and_borough['city']=max_city_key
    noisiest_city_and_borough['borough'] = max_borough_key
    noisiest_city_and_borough['num_city_calls']=max_city_value
    noisiest_city_and_borough['num_borough_calls']= max_borough_value

    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    quietest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the quietest city and borough and their respective metrics

    num_city_calls = defaultdict(int)
    num_borough_calls= defaultdict(int)
    for d in bar_data:
      num_city_calls[d['city']] += int(d['num_calls'])
      num_borough_calls[d['borough']] += int(d['num_calls'])

    for k, v in num_city_calls.items():
      min_city_value = min(num_city_calls.values())
      if v == min_city_value :
        min_city_key = k

    for k,v in num_borough_calls.items():
      min_borough_value = min(num_borough_calls.values())
      if v == min_borough_value :
        min_borough_key = k

    quietest_city_and_borough['city']=min_city_key
    quietest_city_and_borough['borough'] = min_borough_key
    quietest_city_and_borough['num_city_calls']=min_city_value
    quietest_city_and_borough['num_borough_calls']= min_borough_value

    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    #print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
