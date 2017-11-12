import collections
import json
import os
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='85ab5a80-802d-42cf-9b8c-fd06d897fa75',
    password='wG32Agu27wRs', 
    #x-watson-learning-opt-out=True  
    )

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def analyze_my_tone(string):
    tone = tone_analyzer.tone(string,tones=['social','language'],sentences=False,content_type='text/plain')
    #print (tone.items())
    #print ("\n\n")
    dict1 = tone.values()[0].values()[0]
    dict2 = convert(dict1)
    for i in dict2:
        w1 = i['score']*100
        i['w1'] = w1
        w2 = 100-i['w1']
        
        i['w2'] = w2
  
    return (dict2)



    
if __name__ == "__main__":
    user_text = raw_input("ENTER:")
    analyze_my_tone(user_text)


#What am I missing? I need this to be a dictionary so I can access one of the keys. 


'''
{u'document_tone':{u'tones': [
        {u'tone_name': u'Sadness', u'score': 0.718779, u'tone_id': u'sadness'}]
    }
}

curl -X POST --user "85ab5a80-802d-42cf-9b8c-fd06d897fa75":"wG32Agu27wRs" \
--header "Content-Type: application/json" \
--data-binary @/home/sanjit/projects/lnmhacks/tone.json \
"https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21"
'''