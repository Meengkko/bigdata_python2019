from bs4 import BeautifulSoup

html = '''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/1. Basic Concept.nhn?code=158191" title="1987">한국 영화 1987
        </a>
    </div>
</td>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup)

tag = soup.td
print("\ntag=soup.td")
print(tag)

tag = soup.div
print("\ntag=soup.div")
print(tag)

tag = soup.a
print("\ntag=soup.a")
print(tag)

print('\ntag.name')
print(tag.name)

print('\ntag.attrs')
print(tag.attrs)

print('\ntag.text')
print(tag.text)
print('\ntag.string')
print(tag.string)
