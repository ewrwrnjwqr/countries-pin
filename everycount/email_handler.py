import imaplib
obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
obj.login('ethansmitheron@gmail.com','atanqlrtwqhrlwfm')
obj.select()
obj.search(None,'UnSeen')

#interactive map
    #changes based on unread emails that linked via dict to country
        #if email from country map higlights country
