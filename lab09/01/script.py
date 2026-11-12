d = {'sep': ',' , 'end': '\n'}
l = ['utopia', 14, 'vselennaya', 25]
print (l, d)
print (*l, d)
print (*l, *d)
print (*l, **d)