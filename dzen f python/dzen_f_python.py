
a='''The Zen of Python, by Tim Peters 
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#a.find("$")
b=0
a.lower()
d=a
while(1):
    c=d.find("better")
    d=d[c+6:]
    if(c==-1):
        break
    b+=1
print(b)
d=a
b=0
while(1):
    c=d.find("never")
    d=d[c+5:]
    if(c==-1):
        break
    b+=1
print(b)
d=a
b=0
while(1):
    c=d.find("is")
    d=d[c+2:]
    if(c==-1):
        break
    b+=1
print(b)

d=a.lower()


print(d+"\n\n")
c=a.replace("i","&")
print(c)
