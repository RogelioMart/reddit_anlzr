
'''
TODO:
    actually scrape reddit.
    change the hash tables to better hash tables or do a is_in function
    add a GUI
    (maybe) add a feature to also read in memes.
'''

unwanted_words = {
                  "the" : True,
                  "an" : True,
                  "a" : True,
                  "one" : True,
                  "two" : True,
                  "three" : True,
                  "four" : True,
                  "five" : True,
                  "six" : True,
                  "seven" : True,
                  "eight" : True,
                  "nine" : True,
                  "ten" : True,
                  "eleven" : True,
                  "twelve" : True,
                  "thirteen" : True,
                  "fourteen" : True,
                  "fifteen" : True,
                  "sixteen" : True,
                  "seventeen" : True,
                  "eighteen" : True,
                  "nineteen" : True,
                  "twenty" : True,
                  "hundred" : True,
                  "hundreds" : True,
                  "thousand" : True,
                  "thousands" : True,
                  "million" : True,
                  "millions" : True,
                  "billion" : True,
                  "billions" : True,
                  "first" : True,
                  "second" : True,
                  "third" : True,
                  "fourth" : True,
                  "fifth" : True,
                  "sixth" : True,
                  "seventh" : True,
                  "eighth" : True,
                  "ninth" : True,
                  "tenth" : True,
                  "eleventh" : True,
                  "twelfth" : True,
                  "thirteenth" : True,
                  "fourteenth" : True,
                  "fifteenth" : True,
                  "sixteenth" : True,
                  "seventeenth" : True,
                  "eighteenth" : True,
                  "nineteenth" : True,
                  "twentieth" : True,
                  "i" : True,
                  "you" : True,
                  "he" : True,
                  "she" : True,
                  "it" : True,
                  "we" : True,
                  "they" : True,
                  "me" : True,
                  "him" : True,
                  "us" : True,
                  "them" : True,
                  "this" : True,
                  "that" : True,
                  "these" : True,
                  "those" : True,
                  "my" : True,
                  "your" : True,
                  "his" : True,
                  "her" : True,
                  "its" : True,
                  "their" : True,
                  "our" : True,
                  "mine" : True,
                  "yours" : True,
                  "hers" : True,
                  "theirs" : True,
                  "ours" : True,
                  "all" : True,
                  "some" : True,
                  "many" : True,
                  "lot" : True,
                  "lots" : True,
                  "ton" : True,
                  "tons" : True,
                  "bit" : True,
                  "no" : True,
                  "every" : True,
                  "enough" : True,
                  "little" : True,
                  "much" : True,
                  "more" : True,
                  "most" : True,
                  "plenty" : True,
                  "several" : True,
                  "few" : True,
                  "fewer" : True,
                  "kind" : True,
                  "kinds" : True,
                  "myself" : True,
                  "yourself" : True,
                  "himself" : True,
                  "herself" : True,
                  "itself" : True,
                  "oneself" : True,
                  "ourselves" : True,
                  "yourselves" : True,
                  "themselves" : True,
                  "none" : True,
                  "nobody" : True,
                  "everyone" : True,
                  "everybody" : True,
                  "someone" : True,
                  "somebody" : True,
                  "anyone" : True,
                  "anybody" : True,
                  "nothing" : True,
                  "everything" : True,
                  "something" : True,
                  "anything" : True,
                  "each" : True,
                  "other" : True,
                  "whatever" : True,
                  "whichever" : True,
                  "whoever" : True,
                  "whomever" : True,
                  "whomsoever" : True,
                  "whosoever" : True,
                  "others" : True,
                  "neither" : True,
                  "both" : True,
                  "either" : True,
                  "any" : True,
                  "such" : True,
                  "one's" : True,
                  "nobody's" : True,
                  "everyone's" : True,
                  "everybody's" : True,
                  "someone's" : True,
                  "somebody's" : True,
                  "anyone's" : True,
                  "anybody's" : True,
                  "nothing's" : True,
                  "everything's" : True,
                  "something's" : True,
                  "anything's" : True,
                  "whoever's" : True,
                  "others'" : True,
                  "other's" : True,
                  "another's" : True,
                  "neither's" : True,
                  "either's" : True,
                  "which" : True,
                  "what" : True,
                  "whose" : True,
                  "who" : True,
                  "whom" : True,
                  "where" : True,
                  "how" : True,
                  "why" : True,
                  "whether" : True,
                  "wherever" : True,
                  "whyever" : True,
                  "wheresoever" : True,
                  "whensoever" : True,
                  "howsoever" : True,
                  "whysoever" : True,
                  "whatsoever" : True,
                  "whereso" : True,
                  "whomso" : True,
                  "whenso" : True,
                  "howso" : True,
                  "whyso" : True,
                  "whoso" : True,
                  "whatso" : True,
                  "therefor" : True,
                  "therein" : True,
                  "hereby" : True,
                  "hereto" : True,
                  "wherein" : True,
                  "therewith" : True,
                  "herewith" : True,
                  "wherewith" : True,
                  "thereby" : True,
                  "there" : True,
                  "here" : True,
                  "whither" : True,
                  "thither" : True,
                  "hither" : True,
                  "whence" : True,
                  "thence" : True,
                  "always" : True,
                  "once" : True,
                  "twice" : True,
                  "thrice" : True,
                  "can" : True,
                  "cannot" : True,
                  "can't" : True,
                  "could" : True,
                  "couldn't" : True,
                  "could've" : True,
                  "dare" : True,
                  "dares" : True,
                  "dared" : True,
                  "do" : True,
                  "don't" : True,
                  "does" : True,
                  "doesn't" : True,
                  "did" : True,
                  "didn't" : True,
                  "done" : True,
                  "have" : True,
                  "haven't" : True,
                  "had" : True,
                  "hadn't" : True,
                  "has" : True,
                  "hasn't" : True,
                  "i've" : True,
                  "you've" : True,
                  "we've" : True,
                  "they've" : True,
                  "i'd" : True,
                  "you'd" : True,
                  "he'd" : True,
                  "she'd" : True,
                  "it'd" : True,
                  "we'd" : True,
                  "they'd" : True,
                  "would" : True,
                  "wouldn't" : True,
                  "would've" : True,
                  "may" : True,
                  "might" : True,
                  "must" : True,
                  "need" : True,
                  "needn't" : True,
                  "needs" : True,
                  "ought" : True,
                  "shall" : True,
                  "shalln't" : True,
                  "shan't" : True,
                  "should" : True,
                  "shouldn't" : True,
                  "will" : True,
                  "won't" : True,
                  "i'll" : True,
                  "you'll" : True,
                  "he'll" : True,
                  "she'll" : True,
                  "it'll" : True,
                  "we'll" : True,
                  "they'll" : True,
                  "there's" : True,
                  "there're" : True,
                  "there'll" : True,
                  "here's" : True,
                  "here're" : True,
                  "there'll" : True,
                  "appear" : True,
                  "appears" : True,
                  "appeared" : True,
                  "become" : True,
                  "becomes" : True,
                  "became" : True,
                  "come" : True,
                  "comes" : True,
                  "came" : True,
                  "keep" : True,
                  "keeps" : True,
                  "kept" : True,
                  "remain" : True,
                  "remains" : True,
                  "remained" : True,
                  "stay" : True,
                  "stays" : True,
                  "stayed" : True,
                  "turn" : True,
                  "turns" : True,
                  "turned" : True,
                  "doing" : True,
                  "daring" : True,
                  "having" : True,
                  "appearing" : True,
                  "becoming" : True,
                  "coming" : True,
                  "keeping" : True,
                  "remaining" : True,
                  "staying" : True,
                  "saying" : True,
                  "asking" : True,
                  "stating" : True,
                  "seeming" : True,
                  "letting" : True,
                  "making" : True,
                  "setting" : True,
                  "showing" : True,
                  "putting" : True,
                  "adding" : True,
                  "going" : True,
                  "using" : True,
                  "trying" : True,
                  "containing" : True,
                  "in" : True,
                  "from" : True,
                  "with" : True,
                  "under" : True,
                  "throughout" : True,
                  "atop" : True,
                  "for" : True,
                  "on" : True,
                  "of" : True,
                  "to" : True,
                  "aboard" : True,
                  "about" : True,
                  "above" : True,
                  "abreast" : True,
                  "absent" : True,
                  "across" : True,
                  "adjacent" : True,
                  "after" : True,
                  "against" : True,
                  "along" : True,
                  "alongside" : True,
                  "amid" : True,
                  "mid" : True,
                  "among" : True,
                  "apropos" : True,
                  "apud" : True,
                  "around" : True,
                  "as" : True,
                  "astride" : True,
                  "at" : True,
                  "ontop" : True,
                  "afore" : True,
                  "tofore" : True,
                  "behind" : True,
                  "ahind" : True,
                  "below" : True,
                  "ablow" : True,
                  "beneath" : True,
                  "neath" : True,
                  "beside" : True,
                  "between" : True,
                  "atween" : True,
                  "beyond" : True,
                  "ayond" : True,
                  "by" : True,
                  "chez" : True,
                  "circa" : True,
                  "spite" : True,
                  "down" : True,
                  "except" : True,
                  "into" : True,
                  "less" : True,
                  "like" : True,
                  "minus" : True,
                  "near" : True,
                  "nearer" : True,
                  "nearest" : True,
                  "anear" : True,
                  "notwithstanding" : True,
                  "off" : True,
                  "onto" : True,
                  "opposite" : True,
                  "out" : True,
                  "outen" : True,
                  "over" : True,
                  "past" : True,
                  "per" : True,
                  "pre" : True,
                  "qua" : True,
                  "sans" : True,
                  "sauf" : True,
                  "sithence" : True,
                  "through" : True,
                  "thru" : True,
                  "truout" : True,
                  "toward" : True,
                  "underneath" : True,
                  "up" : True,
                  "upon" : True,
                  "upside" : True,
                  "versus" : True,
                  "via" : True,
                  "vis-??-vis" : True,
                  "without" : True,
                  "ago" : True,
                  "apart" : True,
                  "aside" : True,
                  "aslant" : True,
                  "away" : True,
                  "withal" : True,
                  "towards" : True,
                  "amidst" : True,
                  "amongst" : True,
                  "midst" : True,
                  "whilst" : True,
                  "back" : True,
                  "within" : True,
                  "forward" : True,
                  "backward" : True,
                  "ahead" : True,
                  "and" : True,
                  "or" : True,
                  "and/or" : True,
                  "yet" : True,
                  "sooner" : True,
                  "just" : True,
                  "only" : True,
                  "if" : True,
                  "even" : True,
                  "say" : True,
                  "says" : True,
                  "said" : True,
                  "claimed" : True,
                  "ask" : True,
                  "asks" : True,
                  "asked" : True,
                  "stated" : True,
                  "explain" : True,
                  "explains" : True,
                  "explained" : True,
                  "think" : True,
                  "thinks" : True,
                  "talks" : True,
                  "talked" : True,
                  "announces" : True,
                  "announced" : True,
                  "tells" : True,
                  "told" : True,
                  "discusses" : True,
                  "discussed" : True,
                  "suggests" : True,
                  "suggested" : True,
                  "understands" : True,
                  "understood" : True,
                  "again" : True,
                  "definitely" : True,
                  "eternally" : True,
                  "expressively" : True,
                  "instead" : True,
                  "expressly" : True,
                  "immediately" : True,
                  "including" : True,
                  "instantly" : True,
                  "namely" : True,
                  "naturally" : True,
                  "next" : True,
                  "notably" : True,
                  "now" : True,
                  "nowadays" : True,
                  "ordinarily" : True,
                  "positively" : True,
                  "truly" : True,
                  "ultimately" : True,
                  "uniquely" : True,
                  "usually" : True,
                  "almost" : True,
                  "maybe" : True,
                  "probably" : True,
                  "granted" : True,
                  "initially" : True,
                  "too" : True,
                  "actually" : True,
                  "already" : True,
                  "e.g" : True,
                  "i.e" : True,
                  "often" : True,
                  "regularly" : True,
                  "simply" : True,
                  "optionally" : True,
                  "perhaps" : True,
                  "sometimes" : True,
                  "likely" : True,
                  "never" : True,
                  "ever" : True,
                  "else" : True,
                  "inasmuch" : True,
                  "provided" : True,
                  "currently" : True,
                  "incidentally" : True,
                  "elsewhere" : True,
                  "particular" : True,
                  "recently" : True,
                  "relatively" : True,
                  "f.i" : True,
                  "clearly" : True,
                  "apparently" : True,
                  "highly" : True,
                  "very" : True,
                  "really" : True,
                  "extremely" : True,
                  "absolutely" : True,
                  "completely" : True,
                  "totally" : True,
                  "utterly" : True,
                  "quite" : True,
                  "somewhat" : True,
                  "seriously" : True,
                  "fairly" : True,
                  "fully" : True,
                  "amazingly" : True,
                  "seem" : True,
                  "seems" : True,
                  "seemed" : True,
                  "let" : True,
                  "let's" : True,
                  "lets" : True,
                  "make" : True,
                  "makes" : True,
                  "made" : True,
                  "want" : True,
                  "showed" : True,
                  "shown" : True,
                  "go" : True,
                  "goes" : True,
                  "went" : True,
                  "gone" : True,
                  "take" : True,
                  "takes" : True,
                  "took" : True,
                  "taken" : True,
                  "put" : True,
                  "puts" : True,
                  "use" : True,
                  "used" : True,
                  "try" : True,
                  "tries" : True,
                  "tried" : True,
                  "mean" : True,
                  "means" : True,
                  "meant" : True,
                  "called" : True,
                  "based" : True,
                  "add" : True,
                  "adds" : True,
                  "added" : True,
                  "contain" : True,
                  "contains" : True,
                  "contained" : True,
                  "consist" : True,
                  "consists" : True,
                  "consisted" : True,
                  "ensure" : True,
                  "ensures" : True,
                  "ensured" : True,
                  "new" : True,
                  "newer" : True,
                  "newest" : True,
                  "old" : True,
                  "older" : True,
                  "oldest" : True,
                  "previous" : True,
                  "good" : True,
                  "well" : True,
                  "better" : True,
                  "best" : True,
                  "big" : True,
                  "bigger" : True,
                  "biggest" : True,
                  "easy" : True,
                  "easier" : True,
                  "easiest" : True,
                  "fast" : True,
                  "faster" : True,
                  "fastest" : True,
                  "far" : True,
                  "hard" : True,
                  "harder" : True,
                  "hardest" : True,
                  "least" : True,
                  "own" : True,
                  "large" : True,
                  "larger" : True,
                  "largest" : True,
                  "long" : True,
                  "longer" : True,
                  "longest" : True,
                  "low" : True,
                  "lower" : True,
                  "lowest" : True,
                  "high" : True,
                  "higher" : True,
                  "highest" : True,
                  "regular" : True,
                  "simple" : True,
                  "simpler" : True,
                  "simplest" : True,
                  "small" : True,
                  "smaller" : True,
                  "smallest" : True,
                  "tiny" : True,
                  "tinier" : True,
                  "tiniest" : True,
                  "short" : True,
                  "shorter" : True,
                  "shortest" : True,
                  "main" : True,
                  "actual" : True,
                  "nice" : True,
                  "nicer" : True,
                  "nicest" : True,
                  "real" : True,
                  "same" : True,
                  "able" : True,
                  "certain" : True,
                  "usual" : True,
                  "so-called" : True,
                  "mainly" : True,
                  "mostly" : True,
                  "recent" : True,
                  "anymore" : True,
                  "complete" : True,
                  "lately" : True,
                  "possible" : True,
                  "commonly" : True,
                  "constantly" : True,
                  "continually" : True,
                  "directly" : True,
                  "easily" : True,
                  "nearly" : True,
                  "slightly" : True,
                  "somewhere" : True,
                  "estimated" : True,
                  "latest" : True,
                  "different" : True,
                  "similar" : True,
                  "widely" : True,
                  "bad" : True,
                  "worse" : True,
                  "worst" : True,
                  "great" : True,
                  "specific" : True,
                  "available" : True,
                  "average" : True,
                  "awful" : True,
                  "awesome" : True,
                  "basic" : True,
                  "beautiful" : True,
                  "busy" : True,
                  "current" : True,
                  "entire" : True,
                  "everywhere" : True,
                  "important" : True,
                  "major" : True,
                  "multiple" : True,
                  "normal" : True,
                  "necessary" : True,
                  "obvious" : True,
                  "partly" : True,
                  "special" : True,
                  "last" : True,
                  "early" : True,
                  "earlier" : True,
                  "earliest" : True,
                  "young" : True,
                  "younger" : True,
                  "youngest" : True,
                  "" : True,
                  "oh" : True,
                  "wow" : True,
                  "tut-tut" : True,
                  "tsk-tsk" : True,
                  "ugh" : True,
                  "whew" : True,
                  "phew" : True,
                  "yeah" : True,
                  "yea" : True,
                  "shh" : True,
                  "oops" : True,
                  "ouch" : True,
                  "aha" : True,
                  "yikes" : True,
                  "tbs" : True,
                  "tbsp" : True,
                  "spk" : True,
                  "lb" : True,
                  "qt" : True,
                  "pk" : True,
                  "bu" : True,
                  "oz" : True,
                  "pt" : True,
                  "mod" : True,
                  "doz" : True,
                  "hr" : True,
                  "f.g" : True,
                  "ml" : True,
                  "dl" : True,
                  "cl" : True,
                  "l" : True,
                  "mg" : True,
                  "g" : True,
                  "kg" : True,
                  "quart" : True,
                  "seconds" : True,
                  "minute" : True,
                  "minutes" : True,
                  "hour" : True,
                  "hours" : True,
                  "day" : True,
                  "days" : True,
                  "week" : True,
                  "weeks" : True,
                  "month" : True,
                  "months" : True,
                  "year" : True,
                  "years" : True,
                  "today" : True,
                  "tomorrow" : True,
                  "yesterday" : True,
                  "thing" : True,
                  "things" : True,
                  "way" : True,
                  "ways" : True,
                  "matter" : True,
                  "case" : True,
                  "likelihood" : True,
                  "ones" : True,
                  "piece" : True,
                  "pieces" : True,
                  "stuff" : True,
                  "times" : True,
                  "part" : True,
                  "parts" : True,
                  "percent" : True,
                  "instance" : True,
                  "instances" : True,
                  "aspect" : True,
                  "aspects" : True,
                  "item" : True,
                  "items" : True,
                  "idea" : True,
                  "theme" : True,
                  "person" : True,
                  "instance" : True,
                  "instances" : True,
                  "detail" : True,
                  "details" : True,
                  "factor" : True,
                  "factors" : True,
                  "difference" : True,
                  "differences" : True,
                  "not" : True,
                  "yes" : True,
                  "sure" : True,
                  "top" : True,
                  "bottom" : True,
                  "ok" : True,
                  "okay" : True,
                  "amen" : True,
                  "aka" : True,
                  "etc" : True,
                  "etcetera" : True,
                  "sorry" : True,
                  "please" : True,
                  "ms" : True,
                  "mss" : True,
                  "mrs" : True,
                  "mr" : True,
                  "dr" : True,
                  "prof" : True,
                  "jr" : True,
                  "sr" : True,
                  "cant" : True,
                  "couldnt" : True,
                  "couldve" : True,
                  "dont" : True,
                  "doesnt" : True,
                  "didnt" : True,
                  "havent" : True,
                  "hadnt" : True,
                  "hasnt" : True,
                  "ive" : True,
                  "youve" : True,
                  "youre" : True,
                  "weve" : True,
                  "theyve" : True,
                  "id" : True,
                  "youd" : True,
                  "hed" : True,
                  "shed" : True,
                  "itd" : True,
                  "wed" : True,
                  "theyd" : True,
                  "wouldnt" : True,
                  "wouldve" : True,
                  "neednt" : True,
                  "shallnt" : True,
                  "shant" : True,
                  "shouldnt" : True,
                  "wont" : True,
                  "ill" : True,
                  "youll" : True,
                  "hell" : True,
                  "shell" : True,
                  "itll" : True,
                  "well" : True,
                  "theyll" : True,
                  "theres" : True,
                  "therere" : True,
                  "therell" : True,
                  "heres" : True,
                  "herere" : True,
                  "therell" : True,
                  "thats" : True
                 }

'''
name:
returns:
Parameters:
    
description:

'''

'''
name: take_punctuation
returns: String
Parameters:
    in_str: String
    
description:
    Takes in a string converts it all to lower case and keeps only the alphabet
    characters along with spaces, and new lines. Also all punctuation is 
    replaced with a space.
'''
def take_punctuation(in_str):
    
    #dictionary used to keep the function at O(n)
    only_these =	{
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
        " ": " "
    }
    
    ret_str = ""
    
    for x in in_str:
        temp = x.lower()
        #note didn't use the "in" keyword because "in" is basically a loop 
        #and I wanted to keep this function at O(n)
        try: 
            ret_str = ret_str + only_these[temp]
            
        except KeyError: #if there is an exception 
            if(temp != "'"):
                ret_str = ret_str + " "
            
    return(ret_str)

'''
name: word_cntr
returns: dictionary
Parameters:
    anlyz_str: str
    cnt_dict: dictionary
    fltr_out: dictionary
    
description: filters out unwanted words, and counts the wanted words in a 
            dictionary

'''
def word_cntr(anlyz_str, cnt_dict, fltr_out):
    
    word_list = anlyz_str.split() #puts all the words into a list (runtime O(n))
    
    for y in word_list: #iterates through the word list
       
        #print(y)#DEBUGGING
       
        try: #checks if the current wored is an unwanted word
        
            is_it_here = fltr_out[y]
            #print("No error on 1st try")#DEBUGING
            
        except KeyError: #this block is executed if it isn't an unwanted word
       
            try: #checks if word is already in the dictionary
                cnt_dict[y] = cnt_dict[y] + 1
                
            except KeyError: #adds the word to the dictionary if not there
                new_val = {y: 1}
                cnt_dict.update(new_val)
                #print("went into inner except")#DEBUGING
                
    return(cnt_dict)

'''
name: disp_dict
returns: None
Parameters: 
            param_dict1: dictionary
    
description: displays a dictionary that only has one item in each element.

'''
def disp_dict(param_dict1):

    for iter3 in param_dict1:
        print(iter3 + ": " + str(param_dict1[iter3]) + "\n")
    
    return(None)


def temp_main(fltr_words):
    
    anlz_dict = {"NULL" : 0}
    
    take_in_str = "You know what your problem is? You want to think of yourself as the good guy. Well I know you better than anyone, and I can tell you that you're not. In fact, you'd probably sleep a lot better at night if you just admitted to yourself that you're a selfish damned coward who takes whatever he wants and doesn't give a shit about who he hurts. That's you. bone sword oyes know fact"
    
    take_in_str = take_punctuation(take_in_str)
    
    #print(take_in_str)#DEBUGGING
    
    anlz_dict = word_cntr(take_in_str, anlz_dict, fltr_words)
    
    anlz_dict = {key: val for key, val in sorted(anlz_dict.items(), key = lambda ele: ele[1], reverse = True)} # sorts the dictionary
    
    disp_dict(anlz_dict)
    
temp_main(unwanted_words)