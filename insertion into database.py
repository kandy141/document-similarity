from time import clock
import sys,os
import re
import cx_Oracle
from stemming.porter2 import stem
path=input('ENTER THE PATH:')
a=clock()
con=cx_Oracle.connect('scott/tiger@127.0.0.1/XE')
cus=con.cursor()
#path='C:/Python32/files/'
for filename in os.listdir(path):
    fil=open(path+filename,"r")
    content_list_temp=re.findall(r"[\w-]+",fil.read().lower())  
    content_list=[]
    for word in content_list_temp:
        content_list.append(stem(word))
    stopwords=['ll','nt','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','a\x92s','able','about','above','according','accordingly','across','actually','after','afterwards','again','against','ain\x92t','all','allow','allows','almost','alone','along','already','also','although','always','am','among','amongst','an','and','another','any','anybody','anyhow','anyone','anything','anyway','anyways','anywhere','apart','appear','appreciate','appropriate','are','aren\x92t','around','as','aside','ask','asking','associated','at','available','away','awfully','b','be','became','because','become','becomes','becoming','been','before','beforehand','behind','being','believe','below','beside','besides','best','better','between','beyond','both','brief','but','by','c','c\x92mon','c\x92s','came','can','can\x92t','cannot','cant','cause','causes','certain','certainly','changes','clearly','co','com','come','comes','concerning','consequently','consider','considering','contain','containing','contains','corresponding','could','couldn\x92t','course','currently','d','definitely','described','despite','did','didn\x92t','different','do','does','doesn\x92t','doing','don\x92t','done','down','downwards','during','e','each','edu','eg','eight','either','else','elsewhere','enough','entirely','especially','et','etc','even','ever','every','everybody','everyone','everything','everywhere','ex','exactly','example','except','f','far','few','fifth','first','five','followed','following','follows','for','former','formerly','forth','four','from','further','furthermore','g','get','gets','getting','given','gives','go','goes','going','gone','got','gotten','greetings','h','had','hadn\x92t','happens','hardly','has','hasn\x92t','have','haven\x92t','having','he','he\x92s','hello','help','hence','her','here','here\x92s','hereafter','hereby','herein','hereupon','hers','herself','hi','him','himself','his','hither','hopefully','how','howbeit','however','i','i\x92d','i\x92ll','i\x92m','i\x92ve','ie','if','ignored','immediate','in','inasmuch','inc','indeed','indicate','indicated','indicates','inner','insofar','instead','into','inward','is','isn\x92t','it','it\x92d','it\x92ll','it\x92s','its','itself','j','just','k','keep','keeps','kept','know','knows','known','l','last','lately','later','latter','latterly','least','less','lest','let\x92,','let\x92s','like','liked','likely','little','look','looking','looks','ltd','m','mainly','many','may','maybe','me','mean','meanwhile','merely','might','more','moreover','most','mostly','much','must','my','myself','n','name','namely','nd','near','nearly','necessary','need','needs','neither','never','nevertheless','new','next','nine','no','nobody','non','none','noone','nor','normally','not','nothing','novel','now','nowhere','o','obviously','of','off','often','oh','ok','okay','old','on','once','one','ones','only','onto','or','other','others','otherwise','ought','our','ours','ourselves','out','outside','over','overall','own','p','particular','particularly','per','perhaps','placed','please','plus','possible','presumably','probably','provides','q','que','quite','qv','r','rather','rd','re','really','reasonably','regarding','regardless','regards','relatively','respectively','right','s','said','same','saw','say','saying','says','second','secondly','see','seeing','seem','seemed','seeming','seems','seen','self','selves','sensible','sent','serious','seriously','seven','several','shall','she','should','shouldn\x92t','since','six','so','some','somebody','somehow','someone','something','sometime','sometimes','somewhat','somewhere','soon','sorry','specified','specify','specifying','still','sub','such','sup','sure','t','t\x92s','take','taken','tell','tends','th','than','thank','thanks','thanx','that','that\x92s','thats','the','their','theirs','them','themselves','then','thence','there','there\x92s','thereafter','thereby','therefore','therein','theres','thereupon','these','they','they\x92d','they\x92ll','they\x92re','they\x92ve','think','third','this','thorough','thoroughly','those','though','three','through','throughout','thru','thus','to','together','too','took','toward','towards','tried','tries','truly','try','trying','twice','two','u','un','under','unfortunately','unless','unlikely','until','unto','up','upon','us','use','used','useful','uses','using','usually','v','value','various','very','via','viz','vs','w','want','wants','was','wasn\x92t','way','we','we\x92d','we\x92ll','we\x92re','we\x92ve','welcome','well','went','were','weren\x92t','what','what\x92s','whatever','when','whence','whenever','where','where\x92s','whereafter','whereas','whereby','wherein','whereupon','wherever','whether','which','while','whither','who','who\x92s','whoever','whole','whom','whose','why','will','willing','wish','with','within','without','won\x92t','wonder','would','would','wouldn\x92t','x','y','yes','yet','you','you\x92d','you\x92ll','you\x92re','you\x92ve','your','yours','yourself','yourselves','z','zero']
    content_filtered=[]
    content_set=set(content_list)
    for t in content_set:
        if t not in stopwords:
            content_filtered.append(t)
    #print(content_filtered)
    #print(content_filtered)
    for element in content_filtered:
        count=content_list.count(element)
        #print(element)
        cus.execute('insert into search(word,document,tf) values(\''+element+'\' , \''+path+filename+'\' , '+str(count)+')')
    fil.close()
cus.execute('commit')    
b=clock()
print('\n',b-a)


