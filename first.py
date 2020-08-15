# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:35:12 2020
@author: Robbie Cunningham
"""

import json
import pandas as pd
pd.options.display.max_columns = 10
pd.options.display.max_rows = 50
pd.options.display.max_colwidth = 50
pd.options.display.width = 180
import numpy as np


with open('ghostInspector.postman_collection.json') as fp:
    spec = json.load(fp)
    
# for k,v in spec.items():
#     print(k,str(v)[:50])
    
# for d in spec['item']:
#     for k,v in d.items():
#         print(k,str(v)[:50])
reqs = []
for resource in spec['item']:
    # resource['name'] 'Folders'
    # resource['item'] [{'name':'List Folders',...}]
    for item in resource['item']:
        req = {}
        req.update(res=resource['name'])
        # print(resource['name'], en1d=' ')
        req.update(name=item['name'])
        req.update(method=item['request']['method'])
        # print(item['name'])
        req.update(url=item['request']['url']['raw'])
        req.update(desc=item['request']['description'])
        reqs.append(req)
        
df = pd.DataFrame(reqs)
df = df.join(\
    df.url.str.extractall(r'({{\w+}})')\
    .unstack()\
    .rename(lambda x: f'var_{x}',axis=1)\
    .var_0\
)
# print(df)

df.res = df.res.str.replace(' ','')
df.url = "'" + df.url
df.url = df.url.str.replace('{{',"'+").str.replace('}}',"+'")
df.url = df.url.apply(lambda s: s[:-2] if s[-2:]=="+'" else s)
df.desc = df.desc.str.replace('\r\n','\n')
df.method = df.method.str.lower()
df['func_name'] = df.name.str.replace(' ','_').str.lower()

for i in range(3):
    df[f'var_{i}'] = df[f'var_{i}'].str.replace('{{','').str.replace('}}','').replace('apiKey',np.nan)


df = df.join(pd.DataFrame({'signature':[s.replace("'",'') for s in [str(tuple(x)).replace(', nan','') for x in df.filter(like='var').values]]}))
df.signature = df.signature.str.replace('nan','')

r = df.iloc[0]



def funcDef(r):
    funcDef = \
f"""
# {r.res}, {r['name']}
def {r['func_name']}{r.signature}:
    \"""
    {r.desc}
    \"""
    res = requests.{r.method}({r.url})
    return res

"""
    return funcDef



for name,g in df.groupby('res'):
    with open(f'ghostInspector/{name}.py','w') as file:
        header = \
f"""
# -*- coding: utf-8 -*-
\"""
Created on Thu Aug 13 23:35:12 2020
@author: Robbie Cunningham

Here are the available calls for this resource:
{g.func_name.unique().tolist().__repr__()}
\"""

apiKey = '5ddf30aae9f01cae849e738479727c2dfd42b072'
import requests
"""

        file.write(header)
        for _,r in g.iterrows():
            file.write(funcDef(r))

