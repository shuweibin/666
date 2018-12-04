import jieba
excludes = {'什么','一个','我们','你们','如今','说道','老太太','知道','姑娘','起来',
            '这里','出来','众人','那里','奶奶','自己','太太','一面','只见','两个',
            '没有','怎么','不是','这个','听见','这样','进来','咱们','就是','不知',
            '东西','告诉','回来','只是','大家','老爷','只得','丫头','这些','他们',
            '不敢','出去','所以','不过','不好','姐姐','的话','一时','过来'
            }
txt=open("红楼梦.txt","r",enconding='GB18030').read()
words=jieba.lcut_for_search(txt)
counts={}
for word in words:
    if 1<len(word)<4:
        continue
    elif word=='凤姐'or word=='熙凤':
        rword='凤姐'
    elif word=='元春'or word=='贵妃':
        rword='元春'
    elif word=='黛玉'or word=='妹妹':
        rword='黛玉'
    else:
        rword=word
    counts[rword]=counts.get(word,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{o:<10}{1:>5}".format(word,count))
    
    
