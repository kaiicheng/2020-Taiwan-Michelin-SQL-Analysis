import csv
import pandas as pd
import openpyxl

#  匯入餐廳名稱資料
df_star = pd.read_excel("米其林餐廳名稱.xlsx", sheet_name="米其林星等")
df_mid = pd.read_excel("米其林餐廳名稱.xlsx", sheet_name="餐盤中")
df_north = pd.read_excel("米其林餐廳名稱.xlsx", sheet_name="餐盤北")
df_Bi = pd.read_excel("米其林餐廳名稱.xlsx", sheet_name="必比登")
#print(df_mid.values())

rest_dict_star = {}                     # 將他們分為三類，星等、餐盤、必比登
rest_dict_dish = {}
rest_dict_Bib = {}

for i in range(df_star.shape[0]):
    name = df_star.iat[i, 0]
    rest_dict_star[name] = 0

for i in range(df_mid.shape[0]):
    name = df_mid.iat[i, 0]
    rest_dict_dish[name] = 0

for i in range(df_north.shape[0]):
    name = df_north.iat[i, 0]
    rest_dict_dish[name] = 0

for i in range(df_Bi.shape[0]):
    name = df_Bi.iat[i, 0]
    rest_dict_Bib[name] = 0

# 匯入 dcard_food 文章資料
file_name = "db2020_hw5_csv\db2020_dcard_food_score.csv"   # dcard_food 篩出的文章檔案
with open(file=file_name, mode="r", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    header = next(rows)                                  # 用next將 表頭存入 header 並 讓rows[0]跳到第一筆資料
    print(header)

    for row in rows:
        if len(row) != 11:
            continue
        for name in rest_dict_star.keys():
            if name in row[3] or (name in row[8]):              # 名稱出現在標題內
                rest_dict_star[name] += int(row[10])
        for name in rest_dict_dish.keys():
            if name == '澀':                                     # 針對個別作處理
                if ("Sur" in row[8]) and ("澀" in row[8]):
                    rest_dict_dish[name] += int(row[10])
            elif name == '潔':
                if ("ISAGI" in row[8]) or ("isagi" in row[8]):
                    rest_dict_dish[name] += int(row[10])
            elif name == "蘭":
                if ("Orchid" in row[8]) or ("蘭餐廳" in row[8]):
                    rest_dict_dish[name] += int(row[10])
            elif name in row[3] or (name in row[8]):
                rest_dict_dish[name] += int(row[10])
        for name in rest_dict_Bib.keys():
            if name in row[3] or (name in row[8]):
                rest_dict_Bib[name] += int(row[10])
    f.close()

    print(rest_dict_star)
    print("-------------------")
    print(rest_dict_dish)
    print("-------------------")
    print(rest_dict_Bib)

    with open(file="dcard_food_sentiment.csv", mode="w", newline="", encoding='utf-8') as f:  # w 表示為覆寫(會刪除原本的)
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["餐廳名稱", "好感度"])
        for key in rest_dict_star:
            writer.writerow([key, rest_dict_star[key]])
        for key in rest_dict_dish:
            writer.writerow([key, rest_dict_dish[key]])
        for key in rest_dict_Bib:
            writer.writerow([key, rest_dict_Bib[key]])
        f.close()
