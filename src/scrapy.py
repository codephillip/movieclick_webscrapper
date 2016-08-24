from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/home/codephillip/Downloads/crapme/Movies 2016.html'), 'html.parser')

# print(soup.prettify())
# print(soup.title)

mylist = list()
for link in soup.find_all('a'):
    # print(link.string)
    mylist.append(link.string)

# print(mylist[40:580])
mylist2 = mylist[44:1232]
# print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
# print(mylist2)

mylist3 = list()
for x in mylist2:
    # print(x)
    if x:
        mylist3.append(x)

# for x in mylist3:
# 	print(x)

# remove '--> more info'
mylist4 = list()
for x in mylist3:
    # print(x)
    if x != '--> more info':
        mylist4.append(x)

# list with repeated movie titles
count = 0
for x in mylist4:
    count += 1
    print('Count: ' + str(count))
    print(x)

print('Count: ' + str(count))



