# PortfolioRedshift
##### Goal: set up similar project as PortfolioPipeline (see https://github.com/PatrycjaO/PipelineProject), but using AWS Redshift & Prefect & perform some PostgreSQL queries
## 1. Create a minimum AWS stack using infrastructure as code - Pulumi
### VPC:
- S3
- Redshift
- EC2 
## 2. Create IAM roles to enable Redshift to S3 communication
## 3. Using pulumi, transfer relevant .csv files to S3 bucket
## 4. Inside Redshift
4.1. Create Schema
4.2. Create Tables
4.3. Load .csv files inside created tables
4.4. Create Index, views, materialized views, perform some queries, check timestamp handling
## 5. open access to RS from local
## 6. Create make-file for data ingestion into RS
## 7. Connect stack to GitHub and use GitHub Actions
## 8. Prefect for Orchestration
