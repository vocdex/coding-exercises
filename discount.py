"""A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a non-negative real number preceded by a dollar sign.

For example, "$100", "$23", and "$6.75" represent prices while "100", "$", and "2$3" do not.
You are given a string sentence representing a sentence and an integer discount. For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.

Return a string representing the modified sentence."""
def discount(sentence, discount):
    return " ".join([word if not word.startswith('$') and not word[::-1].startswith('$') else '${:.2f}'.format(float(word[1:]) * (1 - discount / 100)) for word in sentence.split()])

sentence = "there are $1 $2 and 5$ candies in the shop"
discounts = 50
print(discount(sentence, discounts))
sentence2 ="1 2 $3 4 $5 $6 7 8$ $9 $10$"
discounts2 = 100
print(discount(sentence2, discounts2))