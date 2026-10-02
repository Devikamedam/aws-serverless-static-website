# AWS WAF Configuration

## Overview

AWS WAF is associated with the Amazon CloudFront distribution to provide
application-layer protection for the static website before requests reach
the private Amazon S3 origin.

## Request Flow

User → Route 53 → AWS WAF → CloudFront → Origin Access Control (OAC) → Private S3

## Web ACL

The CloudFront distribution is protected by an AWS WAF Web ACL using
AWS Managed Rules.

### Managed Rule Groups

The following AWS Managed Rule Groups are enabled:

1. **AWSManagedRulesAmazonIpReputationList**
   - Helps identify and block requests originating from IP addresses
     associated with malicious activity.

2. **AWSManagedRulesCommonRuleSet**
   - Provides protection against commonly encountered web application
     attack patterns.

3. **AWSManagedRulesKnownBadInputsRuleSet**
   - Detects request patterns known to be associated with malicious
     or invalid inputs.

## Architecture Role

AWS WAF inspects incoming HTTP/HTTPS requests before CloudFront serves
content from the private S3 origin.

This adds an additional security layer while the S3 bucket remains
private and accessible only through CloudFront using Origin Access Control.

## Evidence

See:

- `../screenshots/15-waf-web-acl.png`
- `../screenshots/16-waf-managed-rules.png`

## Logging

AWS WAF request logging was not enabled in this implementation.
