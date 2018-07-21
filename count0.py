with open('report.txt','r') as f:
    L0 = f.readlines()
L1 = [i.split() for i in L0[:] if i != 0]
L2 = []
#个人总分以及平均分
for i in L1[1:]:
    agg = 0
    for a in i[1:]:
        agg += int(a)
    L2 += [i + [str(agg)] + ['%.2f'%(agg/len(i[1:]))]]
#排序
L2 = sorted(L2,key=lambda x:x[-1],reverse=True)

L2.insert(0,['平均'])
#各科平均值
for n in range(1,len(L2[1])):
    a = 0
    for i in L2[1:]:
        a += float(i[n])
    L2[0] += ['%.2f'%(a/len(L2[1:]))]

for i in L2[1:]:
    for n in range(1,len(i)-2):
        if int(i[n]) < 60:
            i[n] = '不及格'

for i in range(len(L2)):
    L2[i].insert(0,str(i))

L1[0].insert(0,'名次')
L2.insert(0,L1[0] + ['总分'] + ['平均分'])
#排版
L0 = ''
for i in L2:
    for n in i:
        #检查是否是汉字,折腾了好久(T-T)
        m = 8
        if u'\u4e00' <= u'%s'%(str(n)) <= u'\u9fcb':
            m = 8-len(str(n))
        L0 += '{0:^{1}}'.format(str(n),m)
    L0 += '\n'

with open('report0.txt','w') as f:
    f.write(L0)
print(L0)



