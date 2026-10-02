import boto3
import os
import time

cloudfront = boto3.client("cloudfront")

# CloudFront distribution ID is supplied through a Lambda environment variable.
DISTRIBUTION_ID = os.environ["CLOUDFRONT_DISTRIBUTION_ID"]


def lambda_handler(event, context):
    try:
        response = cloudfront.create_invalidation(
            DistributionId=DISTRIBUTION_ID,
            InvalidationBatch={
                "Paths": {
                    "Quantity": 1,
                    "Items": ["/*"]
                },
                "CallerReference": str(time.time())
            }
        )

        invalidation_id = response["Invalidation"]["Id"]

        print(
            f"CloudFront invalidation created successfully: "
            f"{invalidation_id}"
        )

        return {
            "statusCode": 200,
            "body": f"Invalidation created: {invalidation_id}"
        }

    except Exception as e:
        print(f"Error creating invalidation: {str(e)}")
        raise
