user = 'Lucas'
password = '1234'

dic = {}
dic[user] = password

import pickle
archive = open('data.txt', 'ab')
pickle.dump(dic, archive)
archive.close()

archive = open('data.txt', 'rb')
dic = pickle.load(archive)
archive.close()
print(dic[0])