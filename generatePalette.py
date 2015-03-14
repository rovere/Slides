#!/usr/bin/env python

from collections import OrderedDict
import re, pprint

header = """
<!DOCTYPE html>
<html>
<body>

"""
current_class = ''
current_quantile = ''
current_color = ''
css = open('./assets/css/colorbrewer.css', 'r')
css_description = OrderedDict()

print header
for line in css.readlines():
    line = line.rstrip('\n ')
    m = re.match("^\.(.*) \.(.*) {$", line)
    if m:
        if m.group(1) != current_class:
            current_class = m.group(1)
            css_description.setdefault(current_class, OrderedDict())
        current_quantile = m.group(2)
    m = re.match("^\s+fill: (.*)", line)
    if m:
        current_color = m.group(1)
        css_description[current_class].setdefault(current_quantile, current_color)
#pprint.pprint(css_description)
#cl_sorted = sorted(css_description.keys())
print '<div id="All" style="width:%dpx">' % (len(css_description.keys())*((10+24+10)+(10+86+10)))
for cl in css_description.keys():
    print '<div id="%s" style="float: left; padding: 0px 10px 0px 10px;">' % cl
    print '  <svg width="24" height="%d">' % (len(css_description[cl].keys()) * 24)
#    quantile_sorted = sorted(css_description[cl].keys())
    distance = 0
    for i in css_description[cl].keys():
        print '    <rect fill="%s" width="24" height="24" y="%d"></rect>' % (css_description[cl][i], distance*24)
        distance += 1
    print '  </svg>'
    print '</div>'
    print '<div style="float: left; padding: 0px 10px 0px 10px;">'
    first = True
    for i in css_description[cl].keys():
        if first:
            first = False
            print '<textarea readonly style="line-height:24px; width:80px;height:%dpx">%s %s' % (len(css_description[cl].keys()) * 24,
                                                                                                 cl, 
                                                                                                 i)
        else:
            print "%s %s" % (cl, i)
    print '</textarea>'
    print '</div>'
print '</div>'
print '</body>'
print '</html>'
