hdfs dfs -mkdir /logs
hdfs dfs -put access_log.txt /logs
hdfs dfs -cat /logs/access_log.txt | head -n 50
hdfs dfs -rm /logs/access_log.txt
