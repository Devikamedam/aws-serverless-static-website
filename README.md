# AWS Serverless Static Website with CloudFront & Lambda

## Project Overview

This project demonstrates the deployment of a secure serverless static website on AWS using Amazon S3, Amazon CloudFront, Route 53, AWS Certificate Manager (ACM), and AWS Lambda.

The website content is stored in a private S3 bucket and delivered through CloudFront. Origin Access Control (OAC) is used to securely allow CloudFront to access the S3 bucket.

A custom domain is configured using Route 53, and an ACM certificate provides HTTPS encryption.

AWS Lambda is integrated with S3 Event Notifications to automatically create a CloudFront cache invalidation whenever website content is updated.

---

## Architecture

![AWS Serverless Static Website Architecture](architecture/architecture-diagram.png)

### Request Flow

User / Browser  
↓  
Route 53  
↓  
CloudFront + ACM  
↓  
Origin Access Control (OAC)  
↓  
Private Amazon S3 Bucket

### Content Update Flow

S3 Object Upload / Update  
↓  
S3 Event Notification  
↓  
AWS Lambda  
↓  
CloudFront CreateInvalidation API  
↓  
Updated content delivered to users

---

## AWS Services Used

- Amazon S3
- Amazon CloudFront
- Amazon Route 53
- AWS Certificate Manager (ACM)
- AWS Lambda
- AWS Identity and Access Management (IAM)

---

## Implementation

### Phase 1 – Amazon S3

- Created an S3 bucket for website files.
- Uploaded the static website content.
- Enabled S3 Versioning.
- Kept the S3 bucket private.

### Phase 2 – CloudFront & OAC

- Created a CloudFront distribution.
- Configured the S3 bucket as the CloudFront origin.
- Configured Origin Access Control (OAC).
- Added the required S3 bucket policy for CloudFront access.
- Configured `index.html` as the default root object.

### Phase 3 – ACM & Route 53

- Requested an SSL/TLS certificate using AWS Certificate Manager.
- Validated the certificate using DNS validation.
- Associated the ACM certificate with the CloudFront distribution.
- Configured the custom domain.
- Created a Route 53 Alias record pointing to CloudFront.
- Verified HTTPS access to the website.

### Phase 4 – Automated CloudFront Cache Invalidation

- Created an AWS Lambda function using Python and Boto3.
- Configured an S3 Event Notification to invoke Lambda when website files are updated.
- Granted Lambda permission to call `cloudfront:CreateInvalidation`.
- Configured Lambda to invalidate `/*`.
- Verified successful CloudFront invalidation after S3 content updates.
- 
### Phase 5 – AWS WAF Security

- Created an AWS WAF Web ACL.
- Configured security rules.
- Associated the Web ACL with the CloudFront distribution.
- Tested WAF protection.
---

## IAM Configuration

The Lambda execution role follows least-privilege principles by allowing the function to create invalidations for the required CloudFront distribution.

Example policy:

`iam/lambda-cloudfront-policy.json`

---

## Testing

The following functionality was tested:

- Website accessibility through the custom domain
- HTTPS certificate
- CloudFront distribution
- Private S3 access through CloudFront
- S3 object updates
- Lambda invocation
- Automatic CloudFront invalidation
- Updated website content after cache invalidation

---

## Troubleshooting

During implementation, the Lambda function initially received an `AccessDenied` error when calling the CloudFront `CreateInvalidation` API.

The issue was resolved by adding the required `cloudfront:CreateInvalidation` permission to the Lambda execution role.

This demonstrated the importance of configuring appropriate IAM permissions when integrating AWS services.

---

## Repository Structure

```text
aws-serverless-static-website/
├── README.md
├── architecture/
│   └── architecture-diagram.png
├── website/
│   └── index.html
├── lambda/
│   └── cloudfront_invalidation.py
├── iam/
│   └── lambda-cloudfront-policy.json
├── screenshots/
└── docs/
    └── implementation-guide.md

## Security Considerations

- Amazon S3 bucket is kept private and is not directly accessible from the internet.
- CloudFront securely accesses the S3 bucket using Origin Access Control (OAC).
- HTTPS is enabled using an SSL/TLS certificate from AWS Certificate Manager (ACM).
- IAM permissions are restricted to the actions required by the Lambda function.
- AWS credentials, access keys, secret keys, and other sensitive information are not stored in this repository.
- Website content is delivered to users through CloudFront instead of direct S3 access.

---

## Future Enhancements

- Integrate AWS WAF with CloudFront for additional web application security.
- Add Amazon CloudWatch monitoring, logs, and alarms.
- Implement a CI/CD pipeline for automated website deployment.
- Manage the AWS infrastructure using Terraform (Infrastructure as Code).
- Add additional security monitoring and alerting.

---

## Project Outcome

This project successfully demonstrates the deployment of a secure serverless static website on AWS using Amazon S3, CloudFront, Route 53, AWS Certificate Manager (ACM), IAM, and AWS Lambda.

The website content is stored in a private S3 bucket and securely delivered through CloudFront using Origin Access Control (OAC) and HTTPS.

S3 Event Notifications trigger an AWS Lambda function whenever website content is updated. The Lambda function automatically creates a CloudFront cache invalidation, allowing updated content to be delivered without manually creating an invalidation.

The project demonstrates practical experience with AWS serverless architecture, content delivery, DNS configuration, SSL/TLS, IAM permissions, event-driven automation, and troubleshooting.
