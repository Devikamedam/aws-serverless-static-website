# Project Screenshots

This directory contains implementation and validation evidence for the AWS Serverless Static Website project.

The screenshots document the complete deployment flow across:

- Amazon S3 private static website storage
- S3 Versioning and Block Public Access
- Amazon CloudFront distribution
- Origin Access Control (OAC)
- S3 bucket policy for CloudFront
- AWS Certificate Manager (ACM)
- Route 53 DNS and custom domain
- AWS WAF Web ACL and managed rule groups
- AWS Lambda
- IAM permissions
- S3 Event Notifications
- Automated CloudFront cache invalidation
- HTTPS website validation

## Implementation Evidence

Screenshots `01` through `26` follow the deployment sequence documented in:

`docs/implementation-guide.md`

The final screenshots demonstrate the complete event-driven update flow:

`S3 Object Update → Lambda → CloudFront Invalidation → Updated Website`
