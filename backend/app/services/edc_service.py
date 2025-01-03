import boto3
from botocore.exceptions import BotoCoreError, ClientError
from app.models.edc import EDCRequest, EDCResponse, EDCDeleteResponse


class EDCService:
    def __init__(self, region_name: str = "eu-central-1"):
        self.ec2 = boto3.client("ec2", region_name)

    def create_edc_instance(self, edc_request: EDCRequest) -> EDCResponse:
        """
        Allocate an EC2 instance and set up EDC.
        """
        try:
            response = self.ec2.run_instances(
                ImageId="ami-0abcdef1234567890",  # Replace with the AMI ID for your EDC setup
                InstanceType=edc_request.instance_type,
                KeyName=edc_request.key_name,
                MinCount=1,
                MaxCount=1,
                TagSpecifications=[
                    {
                        "ResourceType": "instance",
                        "Tags": [
                            {"Key": "User", "Value": edc_request.user_id},
                            {"Key": "Purpose", "Value": "EDC"},
                        ],
                    }
                ],
            )
            instance = response["Instances"][0]
            return EDCResponse(
                instance_id=instance["InstanceId"],
                public_ip=instance.get("PublicIpAddress"),
                state=instance["State"]["Name"],
            )
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(f"Error creating EDC instance: {str(e)}")
            return EDCResponse(
                instance_id=instance["InstanceId"],
                public_ip=instance.get("PublicIpAddress"),
                state=instance["State"]["Name"],
            )

    def delete_edc_instance(self, instance_id: str) -> EDCDeleteResponse:
        """
        Terminate an EC2 instance.
        """
        try:
            self.ec2.terminate_instances(InstanceIds=[instance_id])
            return EDCDeleteResponse(instance_id=instance_id, status="terminated")
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(f"Error deleting EDC instance: {str(e)}")

    def deallocate_edc_instance(self, instance_id: str) -> EDCResponse:
        """
        Stop an EC2 instance.
        """
        try:
            self.ec2.stop_instances(InstanceIds=[instance_id])
            instance_info = self.ec2.describe_instances(InstanceIds=[instance_id])[
                "Reservations"
            ][0]["Instances"][0]
            return EDCResponse(
                instance_id=instance_info["InstanceId"],
                public_ip=instance_info.get("PublicIpAddress"),
                state=instance_info["State"]["Name"],
            )
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(f"Error deallocating EDC instance: {str(e)}")
