def get_max_score(p):
    highest = max(p[0]['score'],p[1]['score'])
    if p[0]['score'] == highest:
        return p[0]['label']
    else:
        return p[1]['label']
    
    
