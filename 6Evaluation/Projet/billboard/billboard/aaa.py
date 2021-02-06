import re
import numpy as np
import pandas as pd




# response.css('a::attr(href)')[18].extract()
# a = re.findall(r"q=(\D+lyrics)",'/url?q=https://genius.com/Adele-hello-lyrics&sa=U&ved=2ahUKEwjTlaW43cbuAhW6C2MBHa42Cu8QFjAAegQIAxAB&usg=AOvVaw1syr29ksVk4DUIepciQe4F')
# print(a)



# response.css('div.Lyrics__Container-sc-1ynbvzw-2.jgQsqn').get()
# b = re.sub(r"<.*?>"," ",'<div class="Lyrics__Container-sc-1ynbvzw-2 jgQsqn">[Verse 1]<br><a href="/7996726/Adele-hello/Hello-its-me" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">Hello, it\'s me</span></a><br><a href="/8379629/Adele-hello/I-was-wondering-if-after-all-these-years-youd-like-to-meet-to-go-over-everything" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">I was wondering if after all these years you\'d like to meet<br>To go over everything</span></a><br><a href="/7996753/Adele-hello/They-say-that-times-supposed-to-heal-ya-but-i-aint-done-much-healing" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">They say that time\'s supposed to heal ya, but I ain\'t done much healing</span></a><br><a href="/11059314/Adele-hello/Hello-can-you-hear-me" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">Hello, can you hear me?</span></a><br><a href="/8027128/Adele-hello/Im-in-california-dreaming-about-who-we-used-to-be-when-we-were-younger-and-free" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">I\'m in California dreaming about who we used to be<br>When we were younger and free</span></a><br><a href="/8028881/Adele-hello/Ive-forgotten-how-it-felt-before-the-world-fell-at-our-feet-pre-chorus-theres-such-a-difference-between-us-and-a-million-miles" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">I\'ve forgotten how it felt before the world fell at our feet<br><br>[Pre-Chorus]<br>There\'s such a difference between us<br>And a million miles</span></a><br><br>[Chorus]<br><a href="/8026944/Adele-hello/Hello-from-the-other-side-i-mustve-called-a-thousand-times-to-tell-you-im-sorry-for-everything-that-ive-done-but-when-i-call-you-never-seem-to-be-home" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">Hello from the other side<br>I must\'ve called a thousand times<br>To tell you I\'m sorry for everything that I\'ve done<br>But when I call, you never seem to be home</span></a><br><a href="/8026981/Adele-hello/Hello-from-the-outside-at-least-i-can-say-that-ive-tried-to-tell-you-im-sorry-for-breaking-your-heart-but-it-dont-matter-it-clearly-doesnt-tear-you-apart-anymore" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">Hello from the outside<br>At least, I can say that I\'ve tried<br>To tell you I\'m sorry for breaking your heart<br>But it don\'t matter, it clearly doesn\'t tear you apart anymore</span></a><br><br>[Verse 2]<br><a href="/8027026/Adele-hello/Hello-how-are-you-its-so-typical-of-me-to-talk-about-myself-im-sorry-i-hope-that-youre-well-did-you-ever-make-it-out-of-that-town-where-nothing-ever-happened" class="ReferentFragment__ClickTarget-oqvzi6-0 BjqYT"><span class="ReferentFragment__Highlight-oqvzi6-1 gWpCZc">Hello, how are you?<br>It\'s so typical of me to talk about myself, I\'m sorry<br>I hope that you\'re well<br>Did you ever make it out of that town where nothing ever happened?</span></a><br></div>')
# print(b)

data = pd.read_csv('D:/GITHUB/BillboardGP/6Evaluation/Projet/billboard/billboard/out.csv')

data = data.drop(['date', 'rank', 'last_week', 'peak', 'weeks'], axis=1)
data = data.drop_duplicates()
data = data[['artist', 'title']]
data = data.fillna("")

for i in range(len(data['artist'])):
    data['artist'][i] = re.sub(r"\s", "-",data['artist'][i])
    data['title'][i] = re.sub(r"\s", "-",data['title'][i])

data.to_csv('dataGoogle.csv', index=False)