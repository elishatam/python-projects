def remove_html_markup(s):
    tag = False
    out = ""
    quote = False

    for c in s:
        if c == "<":        #start of markup
            tag = True
        elif c == ">":      #end of markup
            tag = False
        elif c == '"' or c == "'" and tag:      #start of quote
            quote = not quote
        elif not tag:       #elif tag == False:
            out = out + c

    return out

print(remove_html_markup('<a href=">">foo</a>'))

#"<b>foo</b>"