from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql+psycopg2://postgres:Chokhmah1@localhost:5432/customer_churn")


df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
#Total charges from object to numeric

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors = "coerce")

#Columns Work
df.columns = (
    df.columns.str.strip().str.lower().str.replace(" ","_")
)

df = df.rename(columns={
    "customerid":"customer_id",
    "seniorcitizen":"senior_citizen",
    "phoneservice":"phone_service",
    "multiplelines":"multiple_lines",
    "internetservice":"internet_service",
    "onlinesecurity":"online_security",
    "onlinebackup":"online_backup",
    "deviceprotection":"device_protection",
    "techsupport":"tech_support",
    "streamingtv":"streaming_tv",
    "streamingmovies":"streaming_movies",
    "paperlessbilling":"paperless_billing",
    "paymentmethod":"payment_method",
    "monthlycharges":"monthly_charges",
    "totalcharges":"total_charges"
})

#Tenure Group Creation

bins = [0,12,24,float("inf")]
labels = ["New", "Mid-term","Long-term"]

df["tenure_group"] = pd.cut(df["tenure"], bins=bins, labels=labels,right=True,include_lowest=True)

#Churn Group (1/0)
churn_group = {
    "Yes":1,
    "No":0
}

df["churn_numeric"] = df["churn"].map(churn_group)

#Monthly Charges Group

bins = [0,30,70,df["monthly_charges"].max()]
labels = ["Low","Medium","High"]

df["monthly_charges_group"] = pd.cut(df["monthly_charges"],bins=bins,labels=labels,include_lowest=True)


#Service Counts

service_cols = [
    "online_security",
    "online_backup",
    "device_protection",
    "tech_support",
    "streaming_tv",
    "streaming_movies"
]

df["service_count"] = df[service_cols].apply(lambda x:(x=="Yes").sum(),axis=1)


#Contract Lenght

contract_lenght = {
    "Month-to-month":1,
    "One year":12,
    "Two year":24
}

df["contract_lenght"] = df["contract"].map(contract_lenght)



#SQL connect

df.to_sql(
    name="churn",
    con=engine,
    if_exists="replace",
    index=False
)


print(df.columns)