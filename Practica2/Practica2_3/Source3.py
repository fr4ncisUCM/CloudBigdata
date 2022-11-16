from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType

spark_app = SparkSession.builder.appName('CloseCount').getOrCreate()

df = spark_app.read.format("csv").option("header", "true").load("GOOGLE.csv")

df3 = df.drop('Open').drop('High').drop('Low').drop('Adj Close').drop('Volume') \
    .withColumns({'Date': df.Date[0:4]}) \
    .withColumns({'Close': df.Close.cast(IntegerType())}) \
    .groupBy('Date').avg('Close')

df3.show()






# sc.textFile(sys.argv[1]) \
#   .map(lambda line: line.split(",")) \
#  .map(lambda line: (line[0].split("-")[0], line[4])) \
# .reduceByKey(lambda x, y: x+y) \
# .saveAsTextFile(sys.argv[2])
