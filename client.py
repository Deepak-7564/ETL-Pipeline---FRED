from dependencies.scraping.scraper import *
import dependencies.scraping.scraper


def main():

    # print("Hello, Welcome to ETL pipeline..\n\nTo start please input the API key \n")
    # print("get an 32 digits API key using https://fred.stlouisfed.org/docs/api/fred/category.html \n")
    # #key = input()

    print("Select an options from following options :- \n\n")
    print("1. Scrape Metadata and Data into exel file.\n")
    print("2. Scrape Metadata and Data into serialised json file.\n")
    print("3. Scrape Metadata and Data into both excel and serialised json file.\n\n")

    x = int(input())

    if (x == 1):
        print("Downloading data.....\n\n")
        scrape_excel()
        print("metadata and data Downloaded/n/n")

    elif (x == 2):
        print("Downloading data.....\n\n")
        scrape_json()
        print("metadata and data Downloaded/n/n")
        print("Checking for Serializing of jason datasets\n\n")
        check_json_serialize()

    elif (x == 3):
        print("Downloading data.....\n\n")
        scrape_both()
        print("metadata and data Downloaded/n/n")
        print("Checking for Serializing of jason datasets\n\n")
        check_json_serialize()

    else:
        print("please input correct option !!!")
        return x


if __name__ == '__main__':
        main()
        