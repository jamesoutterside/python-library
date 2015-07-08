import json

from urbanairship import common


class StaticList(object):
    def __init__(self, airship, name):
        self.airship = airship
        self.name = name

    def create(self, description=None, extras=None):
        """Create a static list

        :param description: An optional user-provided description of the list.
            Maximum length of 1000 characters
        :param extras: An optional user-provided JSON map of string values associated
            with a list. A key has a maximum length of 64 characters, while a value can
            be up to 1024 characters. You may add up to 100 key-value pairs.
        :return:
        """

        payload = {'name': self.name}
        if description is not None:
            payload['description'] = description
        if extras is not None:
            payload['extras'] = extras

        body = json.dumps(payload).encode('utf-8')
        url = common.LISTS_URL
        response = self.airship._request('POST', body, url, 'application/json', version=3)
        return response.json()

    def upload(self, csv_file):
        """Upload a CSV file to a static list

        :param csv_file: two column format: identifier_type, identifier
        :return: http response
        """

        url = common.LISTS_URL + self.name + 'csv/'
        response = self.airship._request(method='PUT', url=url, version=3, file=csv_file)
        return response.json

    def lookup(self):
        """Retrieve information about the static list
        :return:
        """

        url = common.LISTS_URL + self.name
        response = self.airship._request('GET', None, url, version=3, params=None)
        return response.json()

