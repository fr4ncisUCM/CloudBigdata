from pyspark import SparkConf, SparkContext
import sys

conf = SparkConf().setAppName('WebCount')
sc = SparkContext(conf=conf)


def covert_line(line):
    if line.find("GET") is not -1 or line.find("POST") is not -1 or line.find("HEAD") is not -1:
        return line.split('"')[1] \
            .split(" ")[1] + " " + line.split('"')[1].split(" ")[2]


sc.textFile(sys.argv[1]) \
    .flatMap(lambda line: covert_line(line)) \
    .map(lambda word: (word.lower(), 1)) \
    .reduceByKey(lambda a, b: a + b) \
    .saveAsTextFile(sys.argv[2])
