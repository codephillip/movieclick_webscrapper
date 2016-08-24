from bs4 import BeautifulSoup
from urllib2 import urlopen

# soup = BeautifulSoup(open('/home/codephillip/Downloads/crapme/Movies 2016.html'), 'html.parser')
soup = BeautifulSoup(urlopen('https://teaser-trailer.com/movies-2016.html'), 'lxml')


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


def get_movie_images():
    # get all img with 'src' attribute
    mylist = list()
    for link in soup.find_all('img'):
        print(link['src'])
        mylist.append(link['src'])

    # list without './Movies 2016_files/pixel.gif'
    mylist2 = list()
    for x in mylist:
        if x != './Movies 2016_files/pixel.gif':
            mylist2.append(x)

    count = 1
    for x in mylist2:
        print('count: ' + str(count))
        print(x)
        count += 1

    # remove last link but 19links are missing
    mylist3 = list()
    mylist3 = mylist2[0:98]
    for x in mylist3:
        print(x)


def get_movie_genre():
    # print(soup.prettify())
    # for x in soup.find_all('div'):
    #     print(x.get('moviedesc'))
    # print(soup.div.get_text())

    # contents = soup.find_all('div')[1].contents
    # data = []
    # for i, content in enumerate(contents):
    #     if content.name == "strong":
    #         data.append((content.string, contents[i + 1].string))
    # print data

    mylist = []
    for strong_tag in soup.find_all('strong'):
        tag = strong_tag.next_sibling
        # print tag
        mylist.append(tag)

        # if strong_tag.text.encode("utf-8").find('Genre'):
        #     mylist.append(strong_tag.text)
        # print strong_tag.text

    count = 30
    mylist2 = []
    for x in mylist:
        try:
            # print(mylist[count])
            substring = "Thriller"
            if substring in mylist[count]:
                print("THRILLER CODE")
                mylist2.append(mylist[count])
            count += 5
        except IndexError:
            print(str(IndexError))

    for x in mylist2:
        print(x)

        # print(mylist[3])
        # print(mylist[30])
        # print(mylist[35])
        # print(mylist[50])
        # print(mylist[100])


def main():
    # get_movie_titles()
    get_movie_images()
    # get_movie_genre()


if __name__ == '__main__':
    main()
