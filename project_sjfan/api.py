import os
os.chdir(r'E:\ucc\project_sjfan')
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
data = pd.read_csv('data/merged_global_terrorism_database.csv')

# 得到时间跨度、地区列表、国家列表
year_min,year_max = data['Year'].min(),data['Year'].max()
region_ls = data['Region'].unique().tolist()
country_ls = data['Country'].unique().tolist()


# 后面要统计这两列的值，所以对于空值我们假设没有伤亡
data[['Killed','Wounded']] = data[['Killed','Wounded']].fillna(0)

# df是专门为了画统计图而创的表单，根据地区、国家、年份聚合表单，得到某个国家某个年份的伤亡人数
# 另外计算得到一列AttackCount表示该年份该国家发生的攻击总数
df = data.groupby(['Region','Country','Year'])[['Killed','Wounded']].sum().reset_index()
attack_count = data.groupby(['Region', 'Country', 'Year']).size().reset_index(name='AttackCount')
df = pd.merge(df, attack_count, on=['Region', 'Country', 'Year'])

# 专门用于绘制piechart的表
df_pie = data.groupby(['Region','Country','Year','AttackType'])[['Killed','Wounded']].sum().reset_index()
attacktype_count = data.groupby(['Region', 'Country', 'Year','AttackType']).size().reset_index(name='Count')
df_pie = pd.merge(df_pie, attacktype_count, on=['Region', 'Country', 'Year','AttackType'])

def get_pie_data(region,country,span_year):
    df_filter = df_pie[
        (df_pie['Region']==region) & (df_pie['Country']==country) & (df_pie['Year']>=span_year[0]) & (df_pie['Year']<=span_year[1])
    ]
    pie_data = df_filter.groupby('AttackType')['Count'].sum().reset_index()
    return pie_data

# 专门用于绘制bar的表
df_bar = data.groupby(['Region','Country','Year'])[['Killed','Wounded']].sum().reset_index()
attack_count = data.groupby(['Region', 'Country', 'Year']).size().reset_index(name='AttackCount')
df_bar = pd.merge(df_bar, attack_count, on=['Region', 'Country', 'Year'])

def get_bar_data(region,country,span_year):

    df_filter = df_bar[
        (df_bar['Region']==region) & (df_bar['Country']==country) & (df_bar['Year']>=span_year[0]) & (df_bar['Year']<=span_year[1])
    ]
    filter_data_ls = df_filter[['Killed','Wounded','AttackCount']].values.T.tolist()
    return filter_data_ls

# 专门用于绘制mapchart的表
#根据Region','Country','Year','latitude','longitude聚合，得到伤亡人数、攻击次数、攻击类型
geo_df = data.groupby(['Region','Country','Year','latitude','longitude'])[['Killed','Wounded']].sum().reset_index()
attack_types = data.groupby(['Region','Country','Year','latitude','longitude'])['AttackType'].apply(list).reset_index(name='AttackTypes')
attack_count = data.groupby(['Region', 'Country', 'Year','latitude','longitude']).size().reset_index(name='AttackCount')
geo_df = pd.merge(geo_df, attack_types, on=['Region','Country','Year','latitude','longitude'])
geo_df = pd.merge(geo_df,attack_count,on=['Region','Country','Year','latitude','longitude'])

option_df = data[['Region','Country']].groupby('Region').agg({'Country':lambda x:list(set(x))}).reset_index()
options_series = option_df.apply(lambda x: {x['Region']:x['Country']},axis=1)
all_options = {}
for i in options_series.values:
    all_options.update(i)
