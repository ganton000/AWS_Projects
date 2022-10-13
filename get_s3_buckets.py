import boto3

from pprint import pprint

S3 = boto3.client('s3')


def get_s3_bucket_name(index):

	response = S3.list_buckets()
	buckets = response['Buckets']

	return buckets[index]['Name']

def get_bucket_objects(bucket_name):

	response = S3.list_objects_v2(
		Bucket=bucket_name
	)

	contents = response['Contents']

	return contents[0]['Key']

def add_object_to_bucket(bucket_name, key):

	response = S3.put_object(
		Bucket=bucket_name,
		Key=key #name of the object file
	)

	return response

def upload_file_to_bucket(bucket_name, file_name):

	response = S3.upload_file(
		Filename=file_name,
		Bucket=bucket_name,
		Key=file_name
	)

	return response

if __name__ == "__main__":
	#test_bucket_name = get_s3_bucket_name(13)
	#file_name = "hello.txt"
	#upload_file_to_bucket(test_bucket_name, file_name)
	first_member = PythonClass("Harry")
	second_member = PythonClass("Shawn")

	first_member.get_name()

	first_member.add_number_one_to_name()

	first_member.get_name()

	second_member.get_name()
