f = open('dork3.txt', "r")
line = f.read().split("\n")
print(line)
for i in range(200):
    
    print('    <item>\n     <property name="text">\n      <string>' + line[i] + '</string>\n     </property>\n    </item>')