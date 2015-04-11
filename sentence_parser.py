sentences = ['bring me a spanner', 'fetch a banana','give me a Wrench and a fruit']
map_verbs = dict()
nouns = {'spanner' : ['tool', 'wrench'], 'banana' : ['fruit', 'something to eat']}
verbs = {'bring': ['fetch','take','give'], 'rotate' : ['turn']}
def inverse(m):
  ret = dict()
  for word in m:
    ret[word] = word
    for synonim in m[word]:
      ret[synonim] = word
  return ret
def parse(sentence):
  nouns = []
  verbs = []
  for word in sentence.split():
    word = word.lower()
    if word in map_nouns:
      nouns.append(map_nouns[word])
    if word in map_verbs:
      verbs.append(map_verbs[word])
  return (verbs, nouns)
map_nouns = inverse(nouns)
map_verbs = inverse(verbs)
#print inverse(nouns), inverse
for s in sentences:
  print parse(s)
