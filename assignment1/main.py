import pandas as pd
import numpy as np


def read_excel(path):
    data_dict = {}
    # read raw data
    df = pd.read_excel(path, skiprows=[0])
    print(df.to_string())
    header = df.iloc[:, 0]
    df = df.iloc[:, 1:]
    row, column = df.shape
    # change column names
    names = ["Respondent {}".format(i) for i in range(1, column + 1)]
    df.columns = names
    # Extract information
    # gender
    df_gender = df.iloc[0, :]
    print(df_gender.to_string())
    data_dict.setdefault("Gender", df_gender)
    # Q1. Current uses
    df_current_uses = df.iloc[3:5, :]
    df_current_uses = df_current_uses.T
    print(df_current_uses.to_string())
    data_dict.setdefault("Current uses", df_current_uses)
    # Q2. Likes
    df_likes = df.iloc[6:12, :]
    df_likes = df_likes.T
    print(df_likes.to_string())
    data_dict.setdefault("Likes", df_likes)
    # Q3. Dislikes
    df_dislikes = df.iloc[12:17, :]
    df_dislikes = df_dislikes.T
    print(df_dislikes.to_string())
    data_dict.setdefault("Dislikes", df_dislikes)
    # Q4. Rate the current price of the product
    df_rate_price = df.iloc[18, :]
    df_rate_price = df_rate_price.T
    print(df_rate_price.to_string())
    data_dict.setdefault("Rate the current price", df_rate_price)
    # Q5. Rate the characteristics below.
    df_rate_characteristics = df.iloc[24:45, :]
    df_rate_characteristics = df_rate_characteristics.T
    df_rate_characteristics.columns = header.iloc[24:45]
    print(df_rate_characteristics.to_string())
    data_dict.setdefault("Rate the characteristics", df_rate_characteristics)
    # Q6. Rate the battery life
    df_rate_battery = df.iloc[47, :]
    df_rate_battery = df_rate_battery.T
    print(df_rate_battery.to_string())
    data_dict.setdefault("Rate the battery life", df_rate_battery)
    # How much for rechargeable?
    df_price_rechargeable = df.iloc[50, :]
    df_price_rechargeable = df_price_rechargeable.T
    print(df_price_rechargeable.to_string())
    data_dict.setdefault("How much for rechargeable", df_price_rechargeable)
    # Q7. Rate the look of the product
    df_rate_look = df.iloc[53, :]
    df_rate_look = df_rate_look.T
    print(df_rate_look.to_string())
    data_dict.setdefault("Rate the look of the product", df_rate_look)
    # Would unique colors and patterns improve product?
    df_color_pattern_impact = df.iloc[56, :]
    df_color_pattern_impact = df_color_pattern_impact.T
    print(df_color_pattern_impact.to_string())
    data_dict.setdefault("colors and patterns affect", df_color_pattern_impact)
    # How much more would you pay for cool style?
    df_price_for_coolStyle = df.iloc[59, :]
    df_price_for_coolStyle = df_price_for_coolStyle.T
    print(df_price_for_coolStyle.to_string())
    data_dict.setdefault("pay for cool style", df_price_for_coolStyle)
    # Q8. How much more would you pay for these features?
    df_price_new_features = df.iloc[62:77, :]
    df_price_new_features = df_price_new_features.T
    df_price_new_features.columns = header.iloc[62:77]
    print(df_price_new_features.to_string())
    data_dict.setdefault("pay for these features", df_price_new_features)
    # Which would you most like to have?
    df_desired_features = df.iloc[79:, :]
    df_desired_features = df_desired_features.T
    df_desired_features.columns = header.iloc[79:]
    print(df_desired_features.to_string())
    data_dict.setdefault("most like to have", df_desired_features)
    return data_dict


if __name__ == '__main__':
    # Merge clean data
    writer = pd.ExcelWriter("cleaned_data.xlsx", engine="xlsxwriter")
    data_dict = read_excel("./Product_Survey_Results.xlsx")
    for key, value in data_dict.items():
        value.to_excel(writer, sheet_name=key)
    data_frames = data_dict.values()
    df_cleaned = pd.concat(data_frames, axis=1)
    df_cleaned.to_excel(writer, sheet_name="All data")
    writer.save()