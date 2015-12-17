# Rabbit MQ Stats Logging

Currently the RabbitMQ Admin Plugin only keeps up to the last days worth of stats.  This is to allow the gathering of RabbitMQ stats so that it can be retained for longer periods of time.  The stats are written to a file in json format and can later be parsed and/or input into systems like (Logstash, Elasticsearch...) for further analysis and graphing.

## Getting started

### Installation (Preferred)

```sh
$ pip installl rabbitmqStats
```

### Installation (Alternative)
Download .tar.gz file from /dist directory and pip install

```sh
$ wget https://raw.githubusercontent.com/CodeBleu/rabbitmqStats/develop/rabbitmqStats-VERSION.tar.gz

$ pip install rabbitmqStats-VERSION.tar.gz
```
After install run the following to see default opitions:

```sh
$ rbqstats --help
```


### Development

Want to contribute? Great!  No specifics at this point.  Just basic GitHub Fork and Pull request on the 'development' branch.

For further info, see [github guide] on contributing to opensource project.

After cloning your Forked branch locally, You can run the program by running the following:

```sh
$ ./main.py  --help
```

### Todos

 - Better documentation
 - Add config file for CLI
 - more testing

License
----

MIT [LICENSE.txt]

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [LICENSE.txt]: <https://github.com/CodeBleu/rabbitmqStats/LICENSE.txt>
   [Github Guide]: <https://guides.github.com/activities/contributing-to-open-source/>
   



