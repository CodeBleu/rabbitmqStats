#!/usr/bin/python
import click
from rabbitmqStats import rabbitmqStats
from _config import VERSION
import time
import sys


@click.command()
@click.option('--host', default='localhost',
              help='Specify RabbitMQ host (default = localhost)')
@click.option('--port', default='15672',
              help='Specify RabbitMQ port (default = 15672)')
@click.option('--url', default='/api/queues',
              help='Specify RabbitMQ api (default = /api/queues)')
@click.option('--user', default='guest',
              help='Specify RabbitMQ user (default = guest)')
@click.option('--pwd', default='guest',
              help='Specify RabbitMQ passwrd (default = guest)')
@click.option('--console/--no-console', default=True,
              help='Write output to console (default = --console)')
@click.option('--filename', help='Specify file to log to')
@click.version_option(version='', message="Version: {}".format(VERSION))
def main(host, port, url, user, pwd, filename, console):
    # Description for --help
    ""
    while True:
        try:
            rbq = rabbitmqStats(host, port, url, user, pwd)
        except Exception:
            print "ERROR: Invalid 'host' or 'port'"
            sys.exit()
        try:
            queues = rbq.queue_names()
        except Exception:
            print "ERROR: Invalid (one or more) 'url', 'user', 'pass' setting"
            sys.exit()

        time.sleep(1)

        for que in queues:
            if type(rbq.queue_msg_stats(que)) is not str:
                stats = rbq.queue_msg_stats(que)
                stats['timestamp'] = time.strftime(
                    '%a %d %b %H:%M:%S %Z %Y',
                    time.localtime(rbq.timestamp)
                )
                if filename:
                    with click.open_file(filename, 'a') as myfile:
                        myfile.write("{0}\n".format(stats))
                    if console:
                        print stats
                elif console is True:
                    print stats

if __name__ == '__main__':
    main()
