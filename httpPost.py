import json
import requests
webhook_url = 'https://hooks.slack.com/services/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'

class httpPost(object):

    @staticmethod
    def post(json_data):
        """Takes json data, and makes a post request to slack"""
        response = requests.post(
            webhook_url, data=json.dumps(json_data),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )