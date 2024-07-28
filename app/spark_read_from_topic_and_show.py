from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaWeatherDataConsumer") \
    .config("spark.ui.port", "4040") \
    .getOrCreate()

# Kafka topic to subscribe to
TOPIC_NAME = 'weather_data'

# Read data from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "172.25.0.12:9092,172.25.0.13:9092") \
    .option("subscribe", TOPIC_NAME) \
    .option("startingOffsets", "earliest") \
    .load()

# Select key and value from Kafka message and cast to string
df1 = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Write the data to the console
query = df1.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
