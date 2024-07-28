docker-compose down
docker-compose build
docker-compose up -d

one terminal

docker-compose exec spark bash
cd /app
pip install kafka-python
python create_topic_send_data.py



second terminal


docker-compose exec spark bash
cd /app
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5 --jars kafka-clients-2.2.0.jar --driver-class-path kafka-clients-2.2.0.jar spark_read_from_topic_and_show.py


docker-kafka-spark-master/
├── app/
│   ├── create_topic_send_data.py
│   ├── kafka-clients-2.2.0.jar
│   ├── spark_read_from_topic_and_show.py
│   └── spark-sql-kafka-0-10_2.11-2.4.5.jar
├── Dockerfile.kafka_producer
└── docker-compose.yml

http://localhost:9000  --for kafka 
http://localhost:4040  -- spark


Reference 

https://github.com/asaf-erlich/docker-kafka-spark













