# XSS - Cross Site Scripting

XSS allows us to execute javascript code in the user's stead.

Three types:

- **Reflected**
- **Stored**
- **DOM-based**
---
## Reflected XSS

On e commerce website, user uses the search feature.

keyboard -> search

Page returned:

Search Results for **keboard**: -> **REFLECTION POINT**
blah blah blah
...

the search we used (keybaord, was then displayed by the html)

=> Might have Reflected XSS

![[Pasted image 20250710231323.png]]

Add the \<script> into the search.

---

## Stored XSS

More dangerous than reflected XSS.

Like reflected but stored in database or smth.

Everyone who loads the thing will also load my script.

No need to interact with the victim too.

If it was possible in comment for example, i submit the script, other ppl go to comments and they execute the script bcz database loaded it.

---
