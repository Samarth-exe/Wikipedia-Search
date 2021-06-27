import wikipedia
import time

ask = input('Would you like to get the summary/search for a page: ')
language = input('Please select language("French" or "English"): ')
low = language.lower()
wikipedia.set_lang(low[0:2])
if 'summary' in ask:
    ask1 = input('What would you like to get a summary for: ')
    summ = wikipedia.summary(ask1)
    print('Searching wikipedia...')
    time.sleep(2)
    print(summ)
elif 'page' in ask:
    ask3  = input('Which page would you like to search for: ')
    page = wikipedia.page(ask3)
    print('Searching wikipedia...')
    time.sleep(2)
    page.title
    print(page.content,)

else:
    print('What are you even thinking, Thats not even a valid option')