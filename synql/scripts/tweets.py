import re, itertools as it
import freebase_utils as fbu
from everySNAKE.utils import memo as mem
#scan through a big list of tweets for frequently occuring
#terms.
def tokenize(alltweets):
    '''
    tokenize tweets the easy way - just lowercase everything and split at whitespace.
    '''
    alltexts = set([e.text for e in alltweets])
    allterms = [word.lower() for full in alltexts for word in re.compile('\s+').split(full)]
    return allterms

def count(allterms):
    '''
    count tokenized terms.
    '''
    return dict([(k,len(list((g)))) for k,g in it.groupby(sorted(allterms))])

def run(alltweets, freebase_type = 'band', **kwargs):
    '''
    yield a list of statistically significant tweets.
    cross check it against a set of aliases generated by freebase.
    
    called with a freebase type, it will call the fetch_type routine
    provided by freebase.py in order to grab a list of aliases to match
    against discovered terms.
    '''

    counts = count(tokenize(alltweets))
    long_keys = set([k for k in counts.keys() if len(k)>=5])
    freebase_aliases = fbu.fetch_type(freebase_type, **mem.sr(kwargs))
    matched = [ a.lower() for a  in freebase_aliases if (a.lower() in long_keys)]
    
    raise Exception()
