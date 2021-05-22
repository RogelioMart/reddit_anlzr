'''
Just lists of words that I might want to filter out. I copied these lists from
https://github.com/Yoast/javascript/blob/develop/packages/yoastseo/src/researches/english/functionWords.js
I just needed the lists to make a program that can format these words. 
'''

articles = [ "the", "an", "a" ]

cardinalNumerals = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
	"fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "hundred", "hundreds", "thousand", "thousands",
	"million", "millions", "billion", "billions" ]

ordinalNumerals = [ "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
	"eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth",
	"nineteenth", "twentieth" ]
    
personalPronounsNominative = [ "i", "you", "he", "she", "it", "we", "they" ]

personalPronounsAccusative = [ "me", "him", "us", "them" ]

demonstrativePronouns = [ "this", "that", "these", "those" ]

possessivePronouns = [ "my", "your", "his", "her", "its", "their", "our", "mine", "yours", "hers", "theirs", "ours" ]

quantifiers = [ "all", "some", "many", "lot", "lots", "ton", "tons", "bit", "no", "every", "enough", "little",
	"much", "more", "most", "plenty", "several", "few", "fewer", "kind", "kinds" ]

reflexivePronouns = [ "myself", "yourself", "himself", "herself", "itself", "oneself", "ourselves", "yourselves", "themselves" ]

indefinitePronouns = [ "none", "nobody", "everyone", "everybody", "someone", "somebody", "anyone", "anybody", "nothing",
	"everything", "something", "anything", "each", "other", "whatever", "whichever", "whoever", "whomever",
	"whomsoever", "whosoever", "others", "neither", "both", "either", "any", "such" ]

indefinitePronounsPossessive  = [ "one's", "nobody's", "everyone's", "everybody's", "someone's", "somebody's", "anyone's",
	"anybody's", "nothing's", "everything's", "something's", "anything's", "whoever's", "others'", "other's", "another's",
	"neither's", "either's" ]

interrogativeDeterminers = [ "which", "what", "whose" ]

interrogativePronouns = [ "who", "whom" ]

interrogativeProAdverbs = [ "where", "how", "why", "whether", "wherever", "whyever", "wheresoever", "whensoever", "howsoever",
	"whysoever", "whatsoever", "whereso", "whomso", "whenso", "howso", "whyso", "whoso", "whatso" ]

pronominalAdverbs = [ "therefor", "therein", "hereby", "hereto", "wherein", "therewith", "herewith", "wherewith", "thereby" ]

locativeAdverbs = [ "there", "here", "whither", "thither", "hither", "whence", "thence" ]

adverbialGenitives = [ "always", "once", "twice", "thrice" ]

otherAuxiliaries = [ "can", "cannot", "can't", "could", "couldn't", "could've", "dare", "dares", "dared", "do",
	"don't", "does", "doesn't", "did", "didn't", "done", "have", "haven't", "had", "hadn't", "has", "hasn't",
	"i've", "you've", "we've", "they've", "i'd", "you'd", "he'd", "she'd", "it'd", "we'd", "they'd", "would", "wouldn't",
	"would've", "may", "might", "must", "need", "needn't", "needs", "ought", "shall", "shalln't", "shan't", "should",
	"shouldn't", "will", "won't", "i'll", "you'll", "he'll", "she'll", "it'll", "we'll", "they'll", "there's", "there're",
	"there'll", "here's", "here're", "there'll" ]

copula = [ "appear", "appears", "appeared", "become", "becomes", "became", "come", "comes", "came", "keep", "keeps", "kept",
	"remain", "remains", "remained", "stay", "stays", "stayed", "turn", "turns", "turned" ]

continuousVerbs = [ "doing", "daring", "having", "appearing", "becoming", "coming", "keeping", "remaining", "staying",
	"saying", "asking", "stating", "seeming", "letting", "making", "setting", "showing", "putting", "adding", "going", "using",
	"trying", "containing" ]

prepositions = [ "in", "from", "with", "under", "throughout", "atop", "for", "on", "of", "to", "aboard", "about",
	"above", "abreast", "absent", "across", "adjacent", "after", "against", "along", "alongside", "amid", "mid",
	"among", "apropos", "apud", "around", "as", "astride", "at", "ontop", "afore", "tofore", "behind", "ahind",
	"below", "ablow", "beneath", "neath", "beside", "between", "atween", "beyond", "ayond", "by", "chez",
	"circa", "spite", "down", "except", "into", "less", "like", "minus", "near", "nearer", "nearest", "anear", "notwithstanding",
	"off", "onto", "opposite", "out", "outen", "over", "past", "per", "pre", "qua", "sans", "sauf", "sithence", "through",
	"thru", "truout", "toward", "underneath", "up", "upon", "upside", "versus", "via", "vis-à-vis", "without", "ago",
	"apart", "aside", "aslant", "away", "withal", "towards", "amidst", "amongst", "midst", "whilst" ]

prepositionalAdverbs = [ "back", "within", "forward", "backward", "ahead" ]

coordinatingConjunctions = [ "and", "or", "and/or", "yet" ]

correlativeConjunctions = [ "sooner", "just", "only" ]

subordinatingConjunctions = [ "if", "even" ]

interviewVerbs = [ "say", "says", "said", "claimed", "ask", "asks", "asked", "stated", "explain", "explains", "explained",
	"think", "thinks", "talks", "talked", "announces", "announced", "tells", "told", "discusses", "discussed", "suggests",
	"suggested", "understands", "understood" ]
    
additionalTransitionWords = [ "again", "definitely", "eternally", "expressively", "instead",
	"expressly", "immediately", "including", "instantly", "namely", "naturally", "next", "notably", "now", "nowadays",
	"ordinarily", "positively", "truly", "ultimately", "uniquely", "usually", "almost", "maybe",
	"probably", "granted", "initially", "too", "actually", "already", "e.g", "i.e", "often", "regularly", "simply",
	"optionally", "perhaps", "sometimes", "likely", "never", "ever", "else", "inasmuch", "provided", "currently", "incidentally",
	"elsewhere", "particular", "recently", "relatively", "f.i", "clearly", "apparently" ]
    
intensifiers = [ "highly", "very", "really", "extremely", "absolutely", "completely", "totally", "utterly", "quite",
	"somewhat", "seriously", "fairly", "fully", "amazingly" ]

delexicalizedVerbs = [ "seem", "seems", "seemed", "let", "let's", "lets", "make", "makes", "made", "want", "showed", "shown",
	"go", "goes", "went", "gone", "take", "takes", "took", "taken",	"put", "puts", "use", "used", "try", "tries", "tried", "mean",
	"means", "meant", "called", "based", "add", "adds", "added", "contain", "contains", "contained", "consist", "consists",
	"consisted", "ensure", "ensures", "ensured" ]
    
generalAdjectivesAdverbs = [ "new", "newer", "newest", "old", "older", "oldest", "previous", "good", "well", "better", "best",
	"big", "bigger", "biggest", "easy", "easier", "easiest", "fast", "faster", "fastest", "far", "hard", "harder", "hardest",
	"least", "own", "large", "larger", "largest", "long", "longer", "longest", "low", "lower", "lowest", "high", "higher",
	"highest", "regular", "simple", "simpler", "simplest", "small", "smaller", "smallest", "tiny", "tinier", "tiniest",
	"short", "shorter", "shortest", "main", "actual", "nice", "nicer", "nicest", "real", "same", "able", "certain", "usual",
	"so-called", "mainly", "mostly", "recent", "anymore", "complete", "lately", "possible", "commonly", "constantly",
	"continually", "directly", "easily", "nearly", "slightly", "somewhere", "estimated", "latest", "different", "similar",
	"widely", "bad", "worse", "worst", "great", "specific",  "available", "average", "awful", "awesome", "basic", "beautiful",
	"busy", "current", "entire", "everywhere", "important", "major", "multiple", "normal", "necessary", "obvious", "partly",
	"special", "last", "early", "earlier", "earliest", "young", "younger", "youngest", "" ]
    
interjections = [ "oh", "wow", "tut-tut", "tsk-tsk", "ugh", "whew", "phew", "yeah", "yea", "shh", "oops", "ouch", "aha",
	"yikes" ]
    
recipeWords = [ "tbs", "tbsp", "spk", "lb", "qt", "pk", "bu", "oz", "pt", "mod", "doz", "hr", "f.g", "ml", "dl", "cl",
	"l", "mg", "g", "kg", "quart" ]

timeWords = [ "seconds", "minute", "minutes", "hour", "hours", "day", "days", "week", "weeks", "month", "months",
	"year", "years", "today", "tomorrow", "yesterday" ]
    
vagueNouns = [ "thing", "things", "way", "ways", "matter", "case", "likelihood", "ones", "piece", "pieces", "stuff", "times",
	"part", "parts", "percent", "instance", "instances", "aspect", "aspects", "item", "items", "idea", "theme", "person", "instance",
	"instances", "detail", "details", "factor", "factors", "difference", "differences" ]
    
miscellaneous = [ "not", "yes", "sure", "top", "bottom", "ok", "okay", "amen", "aka", "etc", "etcetera", "sorry", "please" ]

titlesPreceding = [ "ms", "mss", "mrs", "mr", "dr", "prof" ]

titlesFollowing = [ "jr", "sr" ]

noHyphenAux = ["cant", "couldnt", "couldve", "dont", "doesnt", "didnt", "havent", "hadnt", "hasnt", "ive", "youve", "youre", "weve", "theyve", 
    "id", "youd", "hed", "shed", "itd", "wed", "theyd", "wouldnt", "wouldve", "neednt", "shallnt", "shant", "shouldnt", "wont", 
    "ill", "youll", "hell", "shell", "itll", "well", "theyll", "theres", "therere", "therell", "heres", "herere", "therell", "thats"]

unwanted_words = ["the", "an", "a", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
	"fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "hundred", "hundreds", "thousand", "thousands", "million", 
    "millions", "billion", "billions", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", 
    "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "i", "you", "he", "she", 
    "it", "we", "they", "me", "him", "us", "them", "this", "that", "these", "those", "my", "your", "his", "her", "its", "their", "our", "mine", "yours",
    "hers", "theirs", "ours", "all", "some", "many", "lot", "lots", "ton", "tons", "bit", "no", "every", "enough", "little", "much", "more", "most", 
    "plenty", "several", "few", "fewer", "kind", "kinds", "myself", "yourself", "himself", "herself", "itself", "oneself", "ourselves", "yourselves", 
    "themselves", "none", "nobody", "everyone", "everybody", "someone", "somebody", "anyone", "anybody", "nothing", "everything", "something", 
    "anything", "each", "other", "whatever", "whichever", "whoever", "whomever",	"whomsoever", "whosoever", "others", "neither", "both", "either", 
    "any", "such", "one's", "nobody's", "everyone's", "everybody's", "someone's", "somebody's", "anyone's",	"anybody's", "nothing's", "everything's", 
    "something's", "anything's", "whoever's", "others'", "other's", "another's", "neither's", "either's", "which", "what", "whose", "who", "whom", 
    "where", "how", "why", "whether", "wherever", "whyever", "wheresoever", "whensoever", "howsoever", "whysoever", "whatsoever", "whereso", "whomso", 
    "whenso", "howso", "whyso", "whoso", "whatso", "therefor", "therein", "hereby", "hereto", "wherein", "therewith", "herewith", "wherewith", "thereby",
    "there", "here", "whither", "thither", "hither", "whence", "thence", "always", "once", "twice", "thrice", "can", "cannot", "can't", "could", 
    "couldn't", "could've", "dare", "dares", "dared", "do", "don't", "does", "doesn't", "did", "didn't", "done", "have", "haven't", "had", "hadn't", 
    "has", "hasn't", "i've", "you've", "we've", "they've", "i'd", "you'd", "he'd", "she'd", "it'd", "we'd", "they'd", "would", "wouldn't",	"would've", 
    "may", "might", "must", "need", "needn't", "needs", "ought", "shall", "shalln't", "shan't", "should", "shouldn't", "will", "won't", "i'll", "you'll",
    "he'll", "she'll", "it'll", "we'll", "they'll", "there's", "there're", "there'll", "here's", "here're", "there'll", "appear", "appears", "appeared",
    "become", "becomes", "became", "come", "comes", "came", "keep", "keeps", "kept", "remain", "remains", "remained", "stay", "stays", "stayed", "turn",
    "turns", "turned", "doing", "daring", "having", "appearing", "becoming", "coming", "keeping", "remaining", "staying", "saying", "asking", "stating",
    "seeming", "letting", "making", "setting", "showing", "putting", "adding", "going", "using", "trying", "containing", "in", "from", "with", "under",
    "throughout", "atop", "for", "on", "of", "to", "aboard", "about", "above", "abreast", "absent", "across", "adjacent", "after", "against", "along",
    "alongside", "amid", "mid", "among", "apropos", "apud", "around", "as", "astride", "at", "ontop", "afore", "tofore", "behind", "ahind", "below",
    "ablow", "beneath", "neath", "beside", "between", "atween", "beyond", "ayond", "by", "chez", "circa", "spite", "down", "except", "into", "less",
    "like", "minus", "near", "nearer", "nearest", "anear", "notwithstanding", "off", "onto", "opposite", "out", "outen", "over", "past", "per", "pre", 
    "qua", "sans", "sauf", "sithence", "through", "thru", "truout", "toward", "underneath", "up", "upon", "upside", "versus", "via", "vis-à-vis",
    "without", "ago", "apart", "aside", "aslant", "away", "withal", "towards", "amidst", "amongst", "midst", "whilst", "back", "within", "forward", 
    "backward", "ahead", "and", "or", "and/or", "yet", "sooner", "just", "only", "if", "even", "say", "says", "said", "claimed", "ask", "asks", "asked", 
    "stated", "explain", "explains", "explained", "think", "thinks", "talks", "talked", "announces", "announced", "tells", "told", "discusses", 
    "discussed", "suggests", "suggested", "understands", "understood", "again", "definitely", "eternally", "expressively", "instead", "expressly", 
    "immediately", "including", "instantly", "namely", "naturally", "next", "notably", "now", "nowadays", "ordinarily", "positively", "truly", 
    "ultimately", "uniquely", "usually", "almost", "maybe", "probably", "granted", "initially", "too", "actually", "already", "e.g", "i.e", "often",
    "regularly", "simply", "optionally", "perhaps", "sometimes", "likely", "never", "ever", "else", "inasmuch", "provided", "currently", "incidentally",
	"elsewhere", "particular", "recently", "relatively", "f.i", "clearly", "apparently", "highly", "very", "really", "extremely", "absolutely",
    "completely", "totally", "utterly", "quite", "somewhat", "seriously", "fairly", "fully", "amazingly", "seem", "seems", "seemed", "let", "let's", 
    "lets", "make", "makes", "made", "want", "showed", "shown",	"go", "goes", "went", "gone", "take", "takes", "took", "taken",	"put", "puts", "use",
    "used", "try", "tries", "tried", "mean", "means", "meant", "called", "based", "add", "adds", "added", "contain", "contains", "contained",
    "consist", "consists", "consisted", "ensure", "ensures", "ensured", "new", "newer", "newest", "old", "older", "oldest", "previous", "good", "well",
    "better", "best", "big", "bigger", "biggest", "easy", "easier", "easiest", "fast", "faster", "fastest", "far", "hard", "harder", "hardest",	
    "least", "own", "large", "larger", "largest", "long", "longer", "longest", "low", "lower", "lowest", "high", "higher", "highest", "regular", 
    "simple", "simpler", "simplest", "small", "smaller", "smallest", "tiny", "tinier", "tiniest", "short", "shorter", "shortest", "main", "actual", 
    "nice", "nicer", "nicest", "real", "same", "able", "certain", "usual", "so-called", "mainly", "mostly", "recent", "anymore", "complete", "lately",
    "possible", "commonly", "constantly", "continually", "directly", "easily", "nearly", "slightly", "somewhere", "estimated", "latest", "different", 
    "similar", "widely", "bad", "worse", "worst", "great", "specific",  "available", "average", "awful", "awesome", "basic", "beautiful", "busy",
    "current", "entire", "everywhere", "important", "major", "multiple", "normal", "necessary", "obvious", "partly", "special", "last", "early", 
    "earlier", "earliest", "young", "younger", "youngest", "", "oh", "wow", "tut-tut", "tsk-tsk", "ugh", "whew", "phew", "yeah", "yea", "shh", "oops",
    "ouch", "aha", "yikes", "tbs", "tbsp", "spk", "lb", "qt", "pk", "bu", "oz", "pt", "mod", "doz", "hr", "f.g", "ml", "dl", "cl",
	"l", "mg", "g", "kg", "quart", "seconds", "minute", "minutes", "hour", "hours", "day", "days", "week", "weeks", "month", "months",
	"year", "years", "today", "tomorrow", "yesterday", "thing", "things", "way", "ways", "matter", "case", "likelihood", "ones", "piece", "pieces",
    "stuff", "times", "part", "parts", "percent", "instance", "instances", "aspect", "aspects", "item", "items", "idea", "theme", "person", "instance",
	"instances", "detail", "details", "factor", "factors", "difference", "differences", "not", "yes", "sure", "top", "bottom", "ok", "okay", "amen", 
    "aka", "etc", "etcetera", "sorry", "please", "ms", "mss", "mrs", "mr", "dr", "prof", "jr", "sr", "cant", "couldnt", "couldve", "dont", "doesnt", 
    "didnt", "havent", "hadnt", "hasnt", "ive", "youve", "youre", "weve", "theyve", "id", "youd", "hed", "shed", "itd", "wed", "theyd", "wouldnt", 
    "wouldve", "neednt", "shallnt", "shant", "shouldnt", "wont", "ill", "youll", "hell", "shell", "itll", "well", "theyll", "theres", "therere", 
    "therell", "heres", "herere", "therell", "thats"]
    
def make_py_dict(table_name, iter_list):

    ret_str = table_name + " = {"
    
    spaces = ""
    
    for iter1 in ret_str:
        spaces = spaces + " "
    
    ret_str = ret_str + "\n" + spaces
    
    for iter2 in iter_list:
        
        if(iter2 != iter_list[-1]):
            ret_str = ret_str + "\"" + iter2 + "\" : True,\n" + spaces
        else:
            ret_str = ret_str + "\"" + iter2 + "\" : True\n"+ spaces +"\b}"
            
    return(ret_str)
    
print(make_py_dict("unwanted_words", unwanted_words))