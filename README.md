# --- Work in progres ---
#
# PortfolioRedshift
##### Goal: set up similar project as PortfolioPipeline (see https://github.com/PatrycjaO/PipelineProject), but based on AWS
## 1. Create a minimum AWS stack using infrastructure as code - Pulumi
### VPC:
- S3
- Redshift
- EC2
- AWS Lambda
## 2. Create IAM roles to enable communication between Redshift/S3/EC2
## 3. Using pulumi, transfer relevant .csv files to S3 bucket (historical, static files first)
## 4. Connect GitHub to AWS
## 5. Prepare Redshift
- Create Schema
- Create Tables
- Load .csv files inside created tables etc.
## 6. Automate .csv file transfer from GitHub (from GitHub Actions on schedule) to AWS S3 bucket
## 7. Push and run scripts (on schedule) for automatic Redshift update to EC2 instance and automatically append DB
## 8. PostgreSQL
- Create Index, views, materialized views, perform some queries, check timestamp handling, etc.
## (9. streamlit)

