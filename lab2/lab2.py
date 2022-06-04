from logic import *

sentences=[]
file = open("sent6.txt", encoding='utf8')
read = file.readlines()

for line in read:
	sentences.append(line.replace("\n", ""))

KB=And()

knowledge=Or()

for sentence in sentences:
	knowledge=Or()
	sent=(sentence.strip()).split("∨")
	for s in sent:
		if (s[0]=="¬"):
			knowledge.add(Not(Symbol(s[1:])))
			continue
		else:
			knowledge.add(Symbol(s))
	KB.add(knowledge)

#Newly derived logic sentences should be simplified if possible

print(KB.formula())
new=And()
KB_new_sentences=And()

for sentence in KB.conjuncts:
	for sentence2 in KB.conjuncts:
		new_sentence=Or()
		for d in sentence.disjuncts:
			for s in sentence2.disjuncts:
				if str(d.operand)==str(s.operand) and d!=s:
					for k in sentence.disjuncts:
						if k==d:
							continue
						new_sentence.add(k)
					for l in sentence2.disjuncts:
						if l==s:
							continue
						new_sentence.add(l)
					new_sentence.remove_duplicates()
					new_sentence.is_false()
					KB.add(new_sentence)
					new.add(new_sentence)

# No idea how to delete the duplicates from conjunctions
new.remove_duplicates()
print(len(new.conjuncts))
print(new.formula())

