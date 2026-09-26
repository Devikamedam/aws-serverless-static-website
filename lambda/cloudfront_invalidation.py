import boto3
import json
import os
from datetime import datetime, timezone

# Initialize CloudFront client
cloudfront = boto3.client("cloudfront")

# Get CloudFront Distribution ID from Lambda environment variable
DISTRIBUTION_ID = os.environ["CLOUDFRONT_DISTRIBUTION_ID"]   #give your cloudfront ID


def lambda_handler(event, context):
    """
    Creates a CloudFront invalidation when the Lambda function
    is triggered by an S3 object upload or update.
    """

    try:
        response = cloudfront.create_invalidation(
            DistributionId=DISTRIBUTION_ID,
            InvalidationBatch={
                "Paths": {
                    "Quantity": 1,
                    "Items": ["/*"]
                },
                "CallerReference": str(
                    datetime.now(timezone.utc).timestamp()
                )
            }
        )

        invalidation = response["Invalidation"]

        print(
            f"CloudFront invalidation created successfully: "
            f"{invalidation['Id']}"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "CloudFront invalidation created successfully",
                "invalidation_id": invalidation["Id"],
                "status": invalidation["Status"]
            })
        }

    except Exception as error:
        print(f"Error creating CloudFront invalidation: {error}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Failed to create CloudFront invalidation",
                "error": str(error)
            })
        }
