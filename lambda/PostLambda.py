
import requests
import socket
import time
import sys

def postToLambda(baseURL):
    print('Post To Lambda BEGIN');
    hostname = socket.gethostname()
    stage = 'dev'
    timestamp = int(round(time.time() * 1000))
    payload = {
        "sensorID": hostname,
        "notes": "From Python Program!",
        "temperature": 76.11,
        "humidity": 91.33,
        "timestamp": timestamp
    }

    try:
        #lambdaURL = f'{baseURL}/{stage}/sensors/{hostname}/collect'
        lambdaURL = '{}/{}/sensors/{}/collect'.format(baseURL,stage,hostname)
        print("lambdaURL=" + lambdaURL)
        #lambdaURL = '{},{:#5.2f},{:#5.2f},{}'.format(host,temperature,humidity,millis,timestamp)
        headers = {'content-type': 'application/json'}
        response = requests.post(lambdaURL,json=payload,headers=headers)
        #print(f'StatusCode={response.status_code}')
        print('StatusCode={}'.format(response.status_code))
        print('ResponseText={}'.format(response.text))
        #print(f'ResponseText={response.text}')
    except Exception as ex:
        print('Exception in POSTing To Lambda:{}.format(ex)')
        
    print('Post To Lambda END');
    
        
def main():
     print(f'Main Begin')
     baseURL = sys.argv[1]

     postToLambda(baseURL)
    
if __name__ == '__main__':
    main()