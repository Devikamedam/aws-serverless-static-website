# AWS Serverless Static Website – Implementation Guide

This document provides the step-by-step implementation of a secure serverless static website using Amazon S3, CloudFront, Route 53, ACM, and AWS Lambda.

## Architecture

The website content is stored in a private Amazon S3 bucket and delivered globally through Amazon CloudFront. Route 53 provides DNS resolution for the custom domain, while AWS Certificate Manager (ACM) provides HTTPS encryption.

AWS Lambda automatically creates a CloudFront cache invalidation when website content in the S3 bucket is updated.

## Implementation Phases

### Phase 1 – S3 Configuration

1. Created an Amazon S3 bucket to store the static website files.
2. Uploaded the website files, including `index.html`.
3. Enabled S3 Versioning to maintain previous versions of website objects.
4. Enabled Block Public Access to keep the S3 bucket private.
5. Configured the bucket to be accessed through Amazon CloudFront instead of allowing direct public access.
6. Added the required S3 bucket policy to allow CloudFront access through Origin Access Control (OAC).

#### Validation

- Verified that the website files were successfully uploaded.
- Verified that S3 Versioning was enabled.
- Confirmed that the S3 bucket remained private.

---

### Phase 2 – CloudFront and Origin Access Control

1. Created an Amazon CloudFront distribution.
2. Selected the private S3 bucket as the CloudFront origin.
3. Configured Origin Access Control (OAC).
4. Updated the S3 bucket policy to allow access from the CloudFront distribution.
5. Configured `index.html` as the Default Root Object.
6. Deployed the CloudFront distribution.
7. Verified that CloudFront could successfully retrieve the website files from the private S3 bucket.

#### Validation

- Verified that the CloudFront distribution was deployed successfully.
- Verified website access through the CloudFront distribution.
- Confirmed that direct public access to the S3 bucket was not required.

---

### Phase 3 – ACM and Route 53

1. Requested an SSL/TLS certificate using AWS Certificate Manager (ACM).
2. Added the custom domain name to the certificate request.
3. Selected DNS validation for certificate validation.
4. Created the required DNS validation record in Route 53.
5. Waited for the ACM certificate status to change to `Issued`.
6. Associated the ACM certificate with the CloudFront distribution.
7. Added the custom domain name to the CloudFront distribution.
8. Created a Route 53 Alias record pointing the custom domain to the CloudFront distribution.
9. Verified that the website was accessible through the custom domain using HTTPS.

#### Validation

- Confirmed that the ACM certificate status was `Issued`.
- Verified that the Route 53 Alias record pointed to CloudFront.
- Verified successful HTTPS access through the custom domain.

---

### Phase 4 – S3 Event Notification and Lambda

1. Created an AWS Lambda function using Python.
2. Used the AWS SDK for Python (`boto3`) to communicate with CloudFront.
3. Configured the Lambda function to call the CloudFront `CreateInvalidation` API.
4. Configured the invalidation path as `/*` so cached website files could be refreshed.
5. Created an S3 Event Notification for object upload/update events.
6. Configured the S3 Event Notification to invoke the Lambda function.
7. Uploaded or updated a website file in the S3 bucket to trigger the workflow.

#### Automation Flow

S3 Object Upload / Update  
↓  
S3 Event Notification  
↓  
AWS Lambda  
↓  
CloudFront `CreateInvalidation` API  
↓  
CloudFront Cache Refreshed

---

### Phase 5 – IAM Permissions

1. Created/configured an IAM execution role for the Lambda function.
2. Granted the Lambda function permission to create CloudFront invalidations.
3. Used the `cloudfront:CreateInvalidation` action for the required CloudFront distribution.
4. Attached the required permissions to the Lambda execution role.
5. Retested the Lambda function after updating the IAM permissions.

The example IAM policy used by this project is available in:

`iam/lambda-cloudfront-policy.json`

---

### Phase 6 – Testing and Validation

The complete workflow was tested after configuration.

1. Accessed the website using the custom domain.
2. Verified that HTTPS was working correctly.
3. Updated the website content in the S3 bucket.
4. Verified that the S3 event triggered the Lambda function.
5. Verified that Lambda successfully created a CloudFront invalidation.
6. Checked the CloudFront invalidation status.
7. Refreshed the website and verified that the updated content was delivered.

#### Final Request Flow

User / Browser  
↓  
Route 53  
↓  
CloudFront + ACM  
↓  
Origin Access Control (OAC)  
↓  
Private Amazon S3 Bucket

---

### Phase 7 – Troubleshooting

During testing, the Lambda function initially failed to create the CloudFront invalidation and returned an `AccessDenied` error.

The Lambda execution role did not have permission to perform:

`cloudfront:CreateInvalidation`

The IAM permissions were updated to allow the Lambda function to create invalidations for the required CloudFront distribution.

After updating the IAM policy, the Lambda function was tested again and the CloudFront invalidation was created successfully.

This troubleshooting process demonstrated the importance of IAM permissions when integrating AWS services.

---

## Final Result

The project successfully provides a secure serverless static website architecture using:

- Private Amazon S3 storage
- Amazon CloudFront content delivery
- Origin Access Control (OAC)
- Route 53 DNS
- ACM HTTPS certificate
- S3 Event Notifications
- AWS Lambda automation
- IAM access control
- Automatic CloudFront cache invalidation
