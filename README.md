# CloudGaurd-Disaster-Recovery
# PROJECT OVERVIEW

This project implements a cross-region disaster recovery system using AWS.
Files uploaded in the primary region are automatically backed up to another region with real-time email alerts.



#Services Used

Amazon S3

AWS Lambda

Amazon SNS



#Workflow

1. User uploads file to S3 (Mumbai)


2. Lambda triggers on upload


3. File is copied to S3 (Singapore)


4. SNS sends email notification


#Features

Cross-region backup

Automated file replication

Email alerts on success

S3 versioning enabled



#Conclusion

A simple serverless solution to ensure data backup, availability, and monitoring using AWS.
