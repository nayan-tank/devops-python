import boto3

def check_security_groups(region, security_group_ids):
    # Create a boto3 client for EC2 service
    ec2_client = boto3.client('ec2', region_name=region)

    # Iterate over each security group ID in the list
    for security_group_id in security_group_ids:
        # Describe the specified security group
        response = ec2_client.describe_security_groups(GroupIds=[security_group_id])

        # Extract inbound rules
        inbound_rules = response['SecurityGroups'][0]['IpPermissions']

        # Check if any inbound rule allows traffic from all sources
        allow_all_traffic = False
        for rule in inbound_rules:
            if (
                (
                    {'CidrIp': '0.0.0.0/0'} in rule.get('IpRanges', []) or
                    {'CidrIpv6': '::/0'} in rule.get('Ipv6Ranges', [])
                ) and
                rule.get('IpProtocol') != '-1'  # Ignore all traffic rule
            ):
                # print(f"Security group {security_group_id} allows inbound traffic from all sources.")
                print(f"{security_group_id}")
                # allow_all_traffic = True
                break

        # if not allow_all_traffic:
        #     print(f"Security group {security_group_id} does not allow inbound traffic from all sources.")

if __name__ == "__main__":
    region = 'ap-south-1'  # Specify your AWS region here
    security_group_ids = ['sg-074bbc55523853f6f', 'sg-04dfb510f0039d14c', 'sg-00788fc8d8943221a', 'sg-07db0c095b5f186b0', 'sg-086a6cffd73ba015c', 'sg-035815bc4f77153b1', 'sg-0c9b4487bd7fbfc7e', 'sg-0c08fd833c65cf8dd', 'sg-0e2f20d02595f4f35', 'sg-0b64bc7d969b64268', 'sg-0f9ccfe00f310b4c5', 'sg-08ba3fe121fc1a594', 'sg-065f00bd2f22c72f9', 'sg-0ea92719d1f2c54bc', 'sg-0dc2c959f1af91170', 'sg-02c6c0beefd1a3643', 'sg-019d82359c29b8d1c']  # Specify your security group ID here

    check_security_groups(region, security_group_ids)

