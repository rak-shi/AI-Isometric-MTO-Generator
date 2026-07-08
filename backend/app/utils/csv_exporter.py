import pandas as pd
import os


def create_csv(items):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    path = "outputs/mto.csv"

    df = pd.DataFrame(
        items
    )

    df.to_csv(
        path,
        index=False
    )

    return path