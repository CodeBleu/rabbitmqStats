#!/usr/bin/python

import requests
import time
import json
import sys


class rabbitmqStats():

    """This is the class docstring"""

    # defined array to hold queue names
    r = []
    timestamp = ""

    def __init__(self, host, port, url, user, pwd):

        # Get epoch. can be formatted later
        self.timestamp = int(time.time())

        try:
            self.r = requests.get(
                'http://{0}:{1}{2}'.format(host, port, url), auth=(user, pwd)
            )

        except Exception as e:
            print "init: {0}". format(e)
            sys.exit()

    def fetch(self, host, port, url, user, pwd):
        return self.__init__(host, port, url, user, pwd)

    def queue_names(self):
        """Get queue names from rabbitmq and return a list"""
        qs = []

        {qs.append((str(queue['name']))) for queue in self.r.json()}

        return qs

    def __walk_json(self, node):
        stat_data = []
        for key, item in node.items():
            if isinstance(item, dict):
                if 'rate' in item:
                    stat_data.append(
                        ("{}:{}".format(key, item['rate'])).split(":")
                    )
                else:
                    self.__walk_json(item)
            else:
                stat_data.append(("{}:{}".format(key, item)).split(":"))

        return dict(stat_data)

    def queue_msg_stats(self, name):
        """Get metrics of rabbitmq queue"""
        num = self.queue_names().index(name)

        queue = self.r.json()[num]

        if 'message_stats' in queue:
            msg_stats = queue['message_stats']
            cleaned_msg_stats = self.__walk_json(msg_stats)
            cleaned_msg_stats['name'] = name
            return cleaned_msg_stats
        else:
            return "Queue '{}' does not have "\
                "any 'message_stats' available".format(name)


if __name__ == "__main__":

    internal_rbq = rabbitmqStats('localhost',
                                 '15672', '/api/queues', 'guest', 'guest')

    names = internal_rbq.queue_names()

    print "Queue Names: \n{}\n".format(names)
    print "Queue Stats:"

    for i in names:
        stats = internal_rbq.queue_msg_stats(i)
        if type(stats) is dict:
            stats['timestamp'] = time.strftime(
                '%a %d %b %H:%M:%S %Z %Y',
                time.localtime(internal_rbq.timestamp)
            )
            print "{}\n".format(stats)
        else:
            print "{}\n".format(stats)
