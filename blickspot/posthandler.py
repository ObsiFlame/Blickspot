from datetime import datetime
from blickspot.wikiData import hack_dict

h_post = hack_dict

"""
 {
    '2000': 'ILOVEYOU (Reonel Ramones and Onel de Guzman)',
    '2013': 'Tumblr (65,469,298 unique emails and passwords were leaked from Tumblr) ',
    '2018' : 'Facebook Data Scandel'
}

"""

def getDate():
    curDate = datetime.now().date()
    return  curDate.today()

# data_keys = h_post.keys()
# data_values = h_post.values()
# empty_K = []
# empty_V = []

# for i in data_keys:
#     empty_K.append(i)
# for k in data_values:
#     empty_V.append(k)

# destin_K = sorted(empty_K)
# destin_V = sorted(empty_V)
# # New Dictionary 
# hacks_post = {}

# for i,j in zip(destin_K ,destin_V) :
#     strData = {i : f"{j}"}
#     hacks_post.update(strData)

# print(hacks_post) 
# print(getDate())