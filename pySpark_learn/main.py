# auth ： xiaokou
# date ： 2023/5/26 16:23

from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)

# print(sc.version)
# rdd1 = sc.parallelize([1,2,3,4,5])
# rdd2 = sc.parallelize((1,2,3,4,5))
# rdd3 = sc.parallelize("12345")
# rdd4 = sc.parallelize({1,2,3,4,5})
# rdd5 = sc.parallelize({"key1":"1","key2":"2"})
#
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

sc.textFile()

sc.stop()
