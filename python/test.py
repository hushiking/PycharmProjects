import re

a = {"a": 123, "b": "ccc", "c": True}
print(a.items())

m = re.findall('\.', 'a.c')
print(m)

m = re.findall('.', 'aa\nabbccc')
print(m)

m = re.findall('a[bcd]e', 'abeaceade')
print(m)

m = re.findall(r"<div>(.*)</div>", "<div>hello</div><div>world</div>")
print(m)

m = re.findall(r"<div>(.*?)</div>", "<div>hello</div><div>world</div>")
print(m)

s = '<div>hello\nworld</div>'
m = re.findall(r"<div>(.*)</div>", s)
print(m)
m = re.findall(r'<div>(.*)</div>', s, re.S)
print(m)

m = re.findall("\d", "abc1ab2c")
print(m)

m = re.findall("\D", "abc1ab2c")
print(m)

m = re.findall("(abc){2}", "abcabcabcabc")
print(m)
m = re.findall("abc$", "abcabc")
print(m)

m = re.findall("^abc", "abc\nabc")
print(m)
m = re.findall("^abc", "abc\nabc", re.M)
print(m)

s = "aabbbbabb"
m = re.findall("ab?", s)
print(m)
m = re.findall("ab+", s)
print(m)
m = re.findall("ab*", s)
print(m)

m = re.findall("\w+@\w+\.org", "7636874@qq.com;763687@qq.org")
print(m)
