--Q1.What percentage of customers have churned
Select Count(*) as total_customers,sum(churn_numeric) as churned_chustomers,
Round(sum(churn_numeric)::decimal / count(*) *100,2) as churn_percentage from churn
--Q2.Which customer segment churn the most
Select contract, Count(*) as total_customers,sum(churn_numeric) as churned_chustomers,
Round(sum(churn_numeric)::decimal / count(*) *100,2) as churn_percentage from churn
group by contract
order by churn_percentage desc
--Q3. How does customer tenure affect churn?
Select tenure_group, Count(*) as total_customers,sum(churn_numeric) as churned_chustomers,
Round(sum(churn_numeric)::decimal / count(*) *100,2) as churn_percentage from churn
group by tenure_group
order by churn_percentage desc
--Q4. How do payment methods and billing types relate to customer churn?
--Part A
Select payment_method, Count(*) as total_customers,sum(churn_numeric) as churned_chustomers,
Round(sum(churn_numeric)::decimal / count(*) *100,2) as churn_percentage from churn
group by payment_method
order by churn_percentage desc
--Part B
Select paperless_billing, Count(*) as total_customers,sum(churn_numeric) as churned_chustomers,
Round(sum(churn_numeric)::decimal / count(*) *100,2) as churn_percentage from churn
group by paperless_billing
order by churn_percentage desc
--Q5. How do customer demographics and tenure influence churn?
--Part A
Select senior_citizen, Count(*) as total_customers,sum(churn_numeric) as churned_chustomers,
Round(sum(churn_numeric)::decimal / count(*) *100,2) as churn_percentage from churn
group by senior_citizen
order by churn_percentage desc
--Part B
Select tenure_group, Count(*) as total_customers,sum(churn_numeric) as churned_chustomers,
Round(sum(churn_numeric)::decimal / count(*) *100,2) as churn_percentage from churn
group by tenure_group
order by churn_percentage desc
--Part C
Select churn_numeric,
round(avg(monthly_charges)::decimal,2) as avg_monthly_charges,
round(avg(total_charges)::decimal,2)as avg_total_charges
from churn
group by churn_numeric

