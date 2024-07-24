import re

def cleanResume(txt):
    cleanTxt = re.sub('http\S+\s',' ', txt)
    cleanTxt = re.sub('@\S+',' ', cleanTxt)
    cleanTxt = re.sub('#\S+',' ', cleanTxt)
    cleanTxt = re.sub('RT|cc',' ', cleanTxt)
    cleanTxt = re.sub('[%s]'%re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_{|}~"""),' ', cleanTxt)
    cleanTxt = re.sub(r'[^\x00-\x7f]',' ', cleanTxt)
    cleanTxt = re.sub('\s+',' ', cleanTxt)

    return cleanTxt