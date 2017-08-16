def html_list(url_list):
    r"""Return HTML list from a list of strings.

    url_list -- string list.
    """ 

    HTML_str = "<ul>\n"
    
    for item in url_list:
        HTML_str += "<li>{}</li>\n".format(item)
    
    HTML_str += "</ul>"
    
    return HTML_str



url_list = ['https://www.google.com/', 'https://www.facebook.com/','https://twitter.com/']

print(html_list(url_list))