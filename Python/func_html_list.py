def html_list(list_items):
    """
    Function to return HTML list.

    list_items = string list.
    """ 
    HTML_str = "<ul>\n"
    
    for item in list_items:
        HTML_str += "<li>{}</li>\n".format(item)
    
    HTML_str += "</ul>"
    
    return HTML_str

list_items = ['1', '2','3']
print(html_list(list_items))