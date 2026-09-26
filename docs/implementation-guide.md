# AWS Serverless Static Website – Implementation Guide

This document provides the step-by-step implementation of a secure serverless static website using Amazon S3, CloudFront, Route 53, ACM, and AWS Lambda.

## Architecture

The website content is stored in a private Amazon S3 bucket and delivered globally through Amazon CloudFront. Route 53 provides DNS resolution for the custom domain, while AWS Certificate Manager (ACM) provides HTTPS encryption.

AWS Lambda automatically creates a CloudFront cache invalidation when website content in the S3 bucket is updated.

## Implementation Phases

### Phase 1 – S3 Configuration

### Phase 2 – CloudFront and Origin Access Control

### Phase 3 – ACM and Route 53

### Phase 4 – S3 Event Notification and Lambda

### Phase 5 – IAM Permissions

### Phase 6 – Testing and Validation

### Phase 7 – Troubleshooting
