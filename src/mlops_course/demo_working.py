from databricks.connect import DatabricksSession

# Create session with cluster ID
spark = DatabricksSession.builder.profile("mlops").clusterId("0923-045354-q6d90eed").getOrCreate()

print("✅ Successfully connected to Databricks!")
print(f"Spark version: {spark.version}")

# Try a simple query that should be fast
df = spark.read.table("samples.nyctaxi.trips")
print(f"✅ Successfully read table. Row count: {df.count()}")

# Show just a small sample
print("\n📊 Sample data (first 3 rows):")
df.show(3)
