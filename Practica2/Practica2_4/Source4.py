from pyspark import SparkConf, SparkContext
import sys

conf = SparkConf().setAppName('Meteorites')
sc = SparkContext(conf=conf)

sc.textFile(sys.argv[1]) \
    .map(lambda line: line.split(",")) \
    .map(lambda line: (line[1], line[2])) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x, y: y) \
    .saveAsTextFile(sys.argv[2])
