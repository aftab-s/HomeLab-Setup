import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv
import csv

# Load environment variables from .env file
load_dotenv()

# Initialize InfluxDB client
InfluxAPI_Token = os.getenv("InfluxAPI")
Influx_ORG = os.getenv("InfluxORG") 
Influx_Bucket = os.getenv("InfluxBucket")

print("Influx Organization:", Influx_ORG)  # Debugging statement

client = InfluxDBClient(url="http://localhost:8086", token=InfluxAPI_Token, org=Influx_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Read data from CSV and insert into InfluxDB
with open('Emission.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Create InfluxDB data point
        point = Point("emission_measurement") \
            .tag("scope", row['Scope ']) \
            .tag("category", row['Category']) \
            .field("GHG_Emissions", int(row['GHG Emissions'])) \
            .field("date", row['Date']) \
            .tag("country", row['Country']) \
            .tag("region", row['Region']) \
            .time(row['Date'], WritePrecision.NS)

        # Write data point to InfluxDB
        write_api.write(bucket=Influx_Bucket, record=point)

# Close InfluxDB client
client.close()
