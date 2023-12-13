import csv
import boto3
import json
import time
from datetime import datetime

# Name of your Kinesis Data Stream
kdsname = 'iot-input-stream'
region = 'eu-west-1'

# Initialize Kinesis client
clientkinesis = boto3.client('kinesis', region_name=region)

# # Function to convert timestamp to the required format
# def convert_timestamp(old_timestamp):
#     datetime_obj = datetime.strptime(old_timestamp, '%d-%m-%Y %H:%M')
#     return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

# Open the CSV file and read line-by-line, sending each line as a separate record to Kinesis
with open('IoT_2020_b_0.01_fs.csv', 'r') as file:
    csv_reader = csv.DictReader(file)  # Assumes first line contains headers
    
    for row in csv_reader:
        # Convert the timestamp in the 'tmstmp' field
        # if 'tmstmp' in row:
        #     row['tmstmp'] = convert_timestamp(row['tmstmp'])
        #     print (row['tmstmp'])
        # Convert the row to JSON string format
        json_data = json.dumps(row)

        # Send the JSON data as a record to Kinesis
        response = clientkinesis.put_record(
            StreamName=kdsname,
            Data=json_data,
            PartitionKey="1"  # You might want to use a more meaningful partition key
        )
        time.sleep(2)
        print(f"Sent record with sequence number: {response['SequenceNumber']}")

print("done")
