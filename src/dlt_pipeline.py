import dlt
from pyspark.sql.functions import col

@dlt.table(name="raw_data")
def load_data():
    return spark.read.format("json").load("/databricks-datasets/iot-stream/data-device/")

@dlt.table(name="filtered_data")
def filter_data():
    df = dlt.read("raw_data")
    return df.filter(col("model") == "model-1")
