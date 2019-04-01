def remove_html_markup(s):
    tag = False
    out = ""
    quote = False

    for c in s:
        #assert not tag #if condition is true, does nothing.
        #assert (tag or not quote)

        if c == "<" and not quote:        #start of markup
            tag = True
        elif c == ">" and not quote:      #end of markup
            tag = False
        elif c == '"' or c == "'" and tag:      #start of quote
            #assert False #Once we get in here, assertion should automatically fail
            quote = not quote
        elif not tag:       #elif tag == False:
            out = out + c

    assert out.find('<') == -1
    return out

# print(remove_html_markup('"foo"'))
# print(remove_html_markup("'foo'"))
# print(remove_html_markup("<b>foo</b>"))
# print(remove_html_markup('"<b>foo</b>"'))
# print(remove_html_markup("foo"))
# print(remove_html_markup('<a href=">">foo</a>'))

#print(remove_html_markup('<b>foo</b>'))
#print(remove_html_markup('<b>"foo"</b>'))
#print(remove_html_markup('"<b>foo</b>"'))
print(remove_html_markup("'<b>foo</b>'"))
