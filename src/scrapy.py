from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/home/codephillip/Downloads/crapme/Movies 2016.html'), 'html.parser')


def get_movie_titles():
    mylist = list()
    for link in soup.find_all('a'):
        mylist.append(link.string)

    mylist2 = mylist[44:1232]

    mylist3 = list()
    for x in mylist2:
        # print(x)
        if x:
            mylist3.append(x)

    # remove '--> more info'
    mylist4 = list()
    for x in mylist3:
        if x != '--> more info':
            mylist4.append(x)

    # print list with repeated movie titles
    count = 0
    for x in mylist4:
        count += 1
        print('Count: ' + str(count))
        print(x)

    print('Count: ' + str(count))

    # remove repeated titles
    mylist5 = list()
    count = 0
    for x in mylist4:
        if count % 2 == 0:
            try:
                mylist5.append(str(mylist4[count]))
            except Exception:
                print(str(Exception))
        count += 2

    # print FINAL list with single movie titles
    count = 0
    for x in mylist5:
        print('list5: ' + str(count) + ' # ' + str(x))
        count += 1


def main():
    get_movie_titles()

if __name__ == '__main__':
    main()
