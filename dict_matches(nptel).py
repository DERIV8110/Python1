def orangecap(d):
       dict2 = {}
       for k,v in d.items():
              for s,t in v.items():
                     if s in dict2:
                            dict2[s]+=t
                     else:
                            dict2[s] = t
       high_score = max(dict2, key=dict2.get)
       return (high_score,dict2[high_score])