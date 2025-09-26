from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.profile("mlops").clusterId("0923-045354-q6d90eed").getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
