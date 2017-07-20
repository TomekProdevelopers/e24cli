import boto3
ec2 = boto3.resource('ec2',
                    aws_access_key_id='test',
                    aws_secret_access_key='test',
                    region_name = 'eu-poland-1poznan',
                    endpoint_url ='https://eu-poland-1poznan.api.e24cloud.com')

ins = ec2.create_instances(ImageId='ami-000008dc', MinCount =  1, MaxCount = 1, InstanceType='m1.small')#m1.small
