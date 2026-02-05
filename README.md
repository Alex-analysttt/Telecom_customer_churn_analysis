# Telecom_customer_churn_analysis
Data analytics project showing customer_churn_analysis using Python,sql and powerbi
📌 Project Overview
Customer churn is a critical challenge for telecom companies, as losing customers directly impacts revenue and long-term growth.
This project analyzes customer churn data to understand why customers leave, which groups are most affected, and what actions the business can take to reduce churn.
The project was completed as a full end-to-end data analytics workflow, covering data cleaning, feature engineering, SQL-based business analysis, and interactive dashboard storytelling.
🎯 Business Objectives
Identify the overall churn rate
Understand how churn varies by:
Contract type
Tenure group
Payment method
Billing type
Senior citizen status
Provide data-driven insights and recommendations to help management reduce churn and protect revenue
🛠️ Tools & Technologies Used
Python (Pandas, NumPy)
Data cleaning
Feature engineering
PostgreSQL (SQL)
Business questions and churn analysis
Power BI
Interactive dashboard
Visual storytelling
Excel
Data source and initial structure review
📂 Dataset
Source: Telecom Customer Churn Dataset
Records: ~7,000 customers
Key Columns:
Customer demographics
Subscription details
Contract & payment information
Monthly and total charges
Churn status
🔄 Project Workflow
Phase 1: Problem Understanding
Defined churn as customers who stopped subscribing to telecom services
Identified churn as the target variable
Phase 2: Data Cleaning (Python)
Converted incorrect data types (e.g., TotalCharges)
Checked and confirmed:
No missing values
No duplicate records
Standardized column formats for analysis
Phase 3: Feature Engineering (Python)
New columns created to improve analysis:
Tenure Group
New (0–12 months)
Mid-term (13–24 months)
Long-term (25+ months)
Churn Numeric
Yes → 1
No → 0
These features enabled clearer segmentation and easier analysis in SQL and Power BI.
Phase 4: Data Loading
Cleaned and engineered dataset loaded into PostgreSQL
Table structured for efficient querying
Phase 5: Business Analysis (SQL)
Key questions answered using SQL:
What is the overall churn percentage?
Which contract types have the highest churn?
How does tenure affect churn?
How do payment methods and billing types relate to churn?
Do senior citizens churn more than non-senior citizens?
Phase 6: Visualization & Storytelling (Power BI)
Built an interactive dashboard with 9 visuals, including:
Overall churn rate KPI
Churn by contract type
Churn by tenure group
Churn by payment method
Churn by senior citizen status
Added slicers for:
Contract
Tenure group
Payment method
📈 Key Insights
Customers on month-to-month contracts churn significantly more than long-term contract customers
New customers are more likely to churn than long-term customers
Certain payment methods and billing types show higher churn patterns
Senior citizens exhibit slightly higher churn compared to non-senior citizens
💡 Recommendations
Encourage customers to move from month-to-month contracts to longer-term plans
Improve onboarding and engagement for new customers within the first year
Review payment and billing processes associated with higher churn
Design targeted retention strategies for high-risk customer segments
🚀 Key Takeaway
This project demonstrates the ability to:
Work across Python, SQL, and Power BI
Translate raw data into business insights
Communicate findings clearly through dashboards and storytelling
