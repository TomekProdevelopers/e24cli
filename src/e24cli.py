import boto3
client = boto3.client('ec2',endpoint_url='https://eu-poland-1poznan.api.e24cloud.com')

f = open('out.txt','w')
#response =client.describe_images()

#for inst in response['Images']:
#    print(str(inst))

#response =client.describe_instances()
#print(response)
#for inst in response['Images']:
#    print(str(inst))


response = client.describe_instance_attribute(
    Attribute='instanceType',
    DryRun=True,
    InstanceId='34ba1395-c2fd-4a07-ac7a-4cc554509ce5'
)
print(response)

print('end')