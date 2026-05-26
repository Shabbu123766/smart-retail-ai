import pandas as pd


def detect_sales_anomalies():

    df = pd.read_csv(
        "data/curated/curated_walmart.csv"
    )

    anomalies = df[
        df["Weekly_Sales"] > 2500000
    ]

    if anomalies.empty:

        return {
            "message": "No anomalies detected."
        }

    return anomalies[
        ["Store", "Weekly_Sales"]
    ].to_dict(
        orient="records"
    )