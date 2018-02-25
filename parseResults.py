# with open('./testResults2.txt') as f:
#     for line in f:
#         words = line.strip().split(' ')
#         if words[0] == '-------------':
#             ne  = print words
#         print "-------------"




filne = "./testResults3.txt"
count = 0
with open('def.csv', 'wb') as writeFile:
    with open(filne, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            words = line.strip().split(' ')
            if words[0] == '-------------':
                lineINeed  = lines[i+1].strip().split(' ')
                ll = []
                ll.append(lineINeed[-2][lineINeed[-2].rfind('/') + 1: lineINeed[-2].rfind('.')])
                ll = ll + lineINeed[:-2]
                final = ','.join(ll)
                count += 1
                writeFile.write(final)
                writeFile.write('\n')



