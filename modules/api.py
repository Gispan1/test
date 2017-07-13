import requests as req
import json

class api:
    def __init__(self):
        self.token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzY29wZXMiOlsicmlza19zY29yZSIsInJlc3RfYXBpIl0sImlhdCI6MTQ5OTkzMzEwNCwic3ViIjoiUFgyMDAzIiwianRpIjoiOTE0ZTM5NzItNjRjNy00M2Q0LWE5OTktNmQwMjZmYjNiODEzIn0.uwO9XSNEX5GQIL6nyZFi1ZHQ9x__Sd0s38XPxuSzNfY"

    def get_report(self,api_type,value,start_time,end_time,threshold,valid_call=True, api_url='http://portal-stg.perimeterx.com/report/v1/ip'):
        headers = {"Authorization": self.token,"Content-type": "application/json"}
        #post_data = dict(type=api_type, value=value,start_time=start_time,end_time=end_time,threshold=threshold)
        post_data = {"report":{"type": api_type, "value":value,"time":{"type":"range","start_time":start_time, "end_time":end_time}, "threshold":threshold}}
        response = req.post(api_url, data=post_data, headers=headers)
        print response.text
        self.check_api_response(response=response.text,positive_test=valid_call)
        return response.text

    def check_api_response(self,response,positive_test=True):
        response_data = json.loads(response)
        if positive_test == True:
            assert response_data["result"] == True
        else:
            assert response_data["result"] == False