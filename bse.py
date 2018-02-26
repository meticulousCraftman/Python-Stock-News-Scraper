import requests
import bs4
import pytz

# For this to work I need to convert the ticker symbol to security code
SEARCH_URL = "http://www.bseindia.com/corporates/ann.aspx?curpg=1&annflag=1&dt=&dur=D&dtto=&cat=&scrip=%s&anntype=C"
PREFIX_URL = "http://www.bseindia.com"


class BSE(object):

    def __init__(self, security_code):
        
        # Declaring all the instance variable for the class
        self.security_code = security_code
        self.a = []     # Stores the announcements listed on the given page
        self.more_anno_link = ""    # Link of the announcement page for the company
        self.more_news_link = ""    # Link of news page for the company
        self.template_next_a_page = ""     # For storing the link of the next page of the announcement
        self.a_page_links = []    # Stores the list of links all the announcement pages.
        self.link = ""      # Link to the front page of the company we are looking for on moneycontrol
        self.present_a_page = 0

        self.fetch_ticker()
        # self.__fetch_a_next_page_link()


    def fetch_ticker(self):
        try:
            self.link = SEARCH_URL % self.security_code
            r = requests.get(self.link)
            if r.status_code==200:
                print("Fetched page for ticker : "+self.security_code)
                # Creating a bs4 object to store the contents of the requested page
                self.soup = bs4.BeautifulSoup(r.content, 'html.parser')
                print("Fetched page successfully")

            elif r.status_code==404:
                print("Page not found")
            else:
                print("A different status code received : "+str(r.status_code))

        except requests.ConnectionError as ce:
            print("There is a network problem (DNS Failure, refused connectionn etc.). Error : "+str(ce))
            raise Exception
        
        except requests.Timeout as te:
            print("Request timed out. Error : "+str(te))
            raise Exception
        
        except requests.TooManyRedirects as tmre:
            print("The request exceeded the maximum no. of redirections. Error : "+str(tmre))
            raise Exception
        
        except requests. requests.exceptions.RequestException as oe:
            print("Any type of request related error : "+str(oe))
            raise Exception


    def __fetch_a_next_page_link(self):

        # Fetches the template URL for fetching different announcement pages
        r = requests.get(self.more_anno_link)
        announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        # Checking whether the link for the next page is available or not
        if len(announcement_soup.find("div", attrs={"class":"gray2_11"}).find_all("a")) > 0:
            a = announcement_soup.find("div", attrs={"class":"gray2_11"}).find_all("a")[0]["href"]
            self.template_next_a_page = PREFIX_URL + a[0:-1]    # Removing the page no. of the given link so that it becomes general link


    def fetch_a(self, page_no=1):

        if self.has_a(self.template_next_a_page + str(page_no)):

            # Clear all the previous data in "a" instance variable
            self.a = []

            r = requests.get(self.template_next_a_page + str(page_no))

            self.present_a_page = page_no

            announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
            raw_links = announcement_soup.find_all("a", attrs={"class":"bl_15"})
            
            # List of links of all the announcements on the given page
            list_of_links = []
            for x in raw_links:
                link = PREFIX_URL + x['href']
                list_of_links.append(link)
                a = requests.get(PREFIX_URL + x['href'])
                anno_page = bs4.BeautifulSoup(a.content, "html.parser")

                pdf_link = ""
                title = ""
                content = ""

                date = next(anno_page.find("p", attrs={"class":"gL_10"}).children)
                date = self.format_date(date)

                
                # Checking whether the title of the announcement is available or not
                if anno_page.find("span", attrs={"class":"bl_15"}):
                    title = anno_page.find("span", attrs={"class":"bl_15"}).text

                # Checking whether content is available or not
                if anno_page.find("p", attrs={"class":"PT10 b_12"}):
                    content = anno_page.find("p", attrs={"class":"PT10 b_12"}).text
                 
                # Checking whether the PDF link is availableor not
                if anno_page.find("p", attrs={"class":"PT5"}).find("a"):
                    pdf_link = PREFIX_URL + anno_page.find("p", attrs={"class":"PT5"}).find("a")["href"]


                anno = {"link":link, "pdf_link":pdf_link, "content":content, "title":title, "date":date}
                self.a.append(anno)

        else:
            self.a = []
        
        return self.a


    def has_a(self, link):
        result = False
        r = requests.get(link)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        a = soup.find_all("p", attrs={"class":"gL_10"})     # Finding the list of the all the dates available on the page
        if len(a)>0:
            result = True

        return result


    def fetch_all_a_pages(self):
        i = 2
        # fetch the announcement on first page only when this instance variable is empty
        if self.template_next_a_page == "":
            self.fetch_a()
        link = self.template_next_a_page+str(i)
        while self.has_a(link):
            link = self.template_next_a_page+str(i)
            print("Page added : "+str(i))
            self.a_page_links.append(link)
            i += 1  # Keep incrementing the value of i to check the next page
        return self.a_page_links

    def format_date(self,datetime):
        datetime = datetime.split(" ")
        
        date = datetime[0].split("-")
        time = datetime[1]

        date[0] = date[0][:-2]
        month = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12'
        }
        date[1] = month[date[1]]
        date.reverse()
        date = '-'.join(date)
        final = date+" "+time
        return final


