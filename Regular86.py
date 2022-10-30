import re

strs = """ASCII Make \w, \W, \B, \d, \D, \s and \S perform ASCII-only matching instead of full Unicode matching. 
This is only meaningful for Unicode patterns, and is ignored for byte patterns. Corresponds to the inline flag (?a). 

Note that for backward compatibility, the re.U flag still exists (as well as its synonym re.UNICODE and its embedded 
counterpart (?u)), but these are redundant in Python 3 since matches are Unicode by default for strings (and Unicode 
matching isn’t allowed for bytes). 

re.DEBUG
Display debug information about compiled expression. No corresponding inline flag.700-88888
+91-8888877097
+91-7058316557
+91-9650017923
re.I re.IGNORECASE Perform case-insensitive matching; expressions like [A-Z] will also match lowercase letters. Full 
Unicode matching (such as Ü matching ü) also works unless the re.ASCII flag is used to disable non-ASCII matches. The 
current locale does not change the effect of this flag unless the re.LOCALE flag is also used. Corresponds to the 
inline flag (?i). 

Note that when the Unicode patterns aa [a-z] ai or [A-Z] are used in combination with the IGNORECASE flag, they will match 
the 52 ASCII letters and 4 additional non-ASCII letters: ‘İ’ (U+0130, Latin capital letter I with dot above), 
‘ı’ (U+0131, Latin small letter dotless i), ‘ſ’ (U+017F, Latin small letter long s) and ‘K’ (U+212A, Kelvin sign). If 
the ASCII flag is used, only letters ‘a’ to ‘z’ and ‘A’ to ‘Z’ are matched"""
# patt = re.compile(r"DEBUG")
# patt = re.compile(r".nico")
# patt = re.compile(r"^ASCII")
# patt = re.compile(r"tched$")
# patt = re.compile(r"ai*")
# patt = re.compile(r"ai+")
# patt = re.compile(r"a{2}")
# patt = re.compile(r"(a){1}")
# patt = re.compile(r"s|dd")

# --------------special sequences___________

# patt = re.compile(r"\AAS")
# patt = re.compile(r"\bAS")
# patt = re.compile(r"ag\b")
# patt = re.compile(r"\d{3}-\d{5}")
# patt = re.compile(r"\b91")
patt = re.compile(r"\+91-\d{10}\b")

matches = patt.finditer(strs)
# print(matches)
for match in matches:
    print(match)
# code on file MetaRe.txt_________________
