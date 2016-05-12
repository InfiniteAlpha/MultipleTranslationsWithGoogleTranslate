##USING A POST REQUEST TO REQUEST DATA THROUGH A GOOGLE SEARCH


import urllib
import mechanize

def translate(home_language,target_language,text):
    text = text.replace(" ","%20")
    get_url = "http://translate.google.com/translate_a/t?client=t&sl="+home_language+"&tl="+target_language+"&hl="+home_language+"&sc=2&ie=UTF-8&rom=l&prev=btn&ssel=5&tsel=5&q="+text
    #get_url = "http://translate.google.com/?hl="+home_language+"#"+home_language+"/"+target_language+"/"+text
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent','Chrome')]
    translate_text = browser.open(get_url).read().decode('utf-8',errors='ignore') ##ISO-8859-1
    translate_text = translate_text.split("]]")
    return translate_text[0].replace("[[[","").replace('"','').split(",")[0]

##def spinner(text):
    ##return translate("zh-CN","en",translate("en","zh-CN",text).encode('utf-8'))
##print spinner("Hello World")

def spinner(home_language,target_language,text):
    return post_request( target_language, home_language,  post_request(home_language,target_language,text))


def post_request(home_language,target_language,text):
    post_url = "http://translate.google.com/translate_a/t"
    parameters = {
        'client':'t',
        'text':text,
        'sl':home_language,
        'tl':target_language,
        'hl':home_language,
        'ie':'UTF-8',
        'oe':'UTF-8',
        'pc':'2',
        'oc':'1',
        'otf':'1',
        'rom':'1',
        'ssel':'0',
        'tsel':'0',
        }

##    test = ""
##    for t in text:
##        try:
##            test += t.encode('utf-8')
##        except:
##            a = 0
##            text = test

    try:
        data = urllib.urlencode(parameters)
        ##print data
        ##urlencode appends text and parameters onto the end of the url (replaces " " with "+")
    except:
        print "error encoding params"

    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent','Chrome')]
    ##translate_text = browser.open(post_url,data).read().decode('utf-8')
    response = browser.open(post_url,data).read()#.decode('utf-8')
    ##print translate_text

    


    #return translate_text
    ##after changing from print to return, we are now able to convert the parameter values to variables

    #response = post_request("en","zh-CN",'Disclaimer: We are not responsible for any use of the code presented in this video by a third party. The code presented in this video is free of charge and provided for educational purposes only.')
    translate_array = response.replace("[[[","").replace('["',"$$$").replace('"]',"$$$").split("$$$")

    trans_string = ""

    for block in translate_array:
        trans_string += block.split('","')[0]
    return  trans_string.split("]")[0].replace(",","")[1:]

    #print trans_string.split("]")[0].replace(",","")[1:]

##print translate_array


#print spinner("en","zh-CN","Disclaimer: Research LLC is not responsible for any use of the code presented in this video by a third party. The code presented in this tuturial is free of charge and for educational purposes only.")

##print post_request("zh-CN","en",post_request("en","zh-CN",'Welcome to the best post request tutorial on youtube'))






homeArray = ["en"]
targetArray = ["af","ak","sq","am","ar"]#,"hy","az","eu","be","bem","bn","bh","xx-bork","bs","br","bg","km","ca","chr","ny","zh-CN","zh-TW","co","hr","cs","da","nl","xx-elmer","en","eo","et","ee","fo","tl","fi","fr","fy","gaa","gl","ka","de","el","gn","gu","xx-hacker","ht","ha","haw","iw","hi","hu","is","ig","id","ia","ga","it","ja","jw","kn","kk","rw","rn","xx-klingon","kg","ko","kri","ku","ckb","ky","lo","la","lv","ln","lt","loz","lg","ach","mk","mg","ms","ml","mt","mi","mr","mfe","mo","mn","sr-ME","ne","pcm","nso","no","nn","oc","or","om","ps","fa","xx-pirate","pl","pt-BR","pt-PT","pa","qu","ro","rm","nyn","ru","gd","sr","sh","st","tn","crs","sn","sd","si","sk","sl","so","es","es-419","su","sw","sv","tg","ta","tt","te","th","ti","to","lua","tum","tr","tk","tw","ug","uk","ur","uz","vi","cy","wo","xh","yi","yo","zu"]
targetLangArray = ["Afrikaans","Akan","Albanian","Amharic","Arabic"]#,"Armenian","Azerbaijani","Basque","Belarusian","Bemba","Bengali","Bihari","Bork, bork, bork!","Bosnian","Breton","Bulgarian","Cambodian","Catalan","Cherokee","Chichewa","Chinese (Simplified)","Chinese (Traditional)","Corsican","Croatian","Czech","Danish","Dutch","Elmer Fudd","English","Esperanto","Estonian","Ewe","Faroese","Filipino","Finnish","Estonian","Ewe","Faroese","Filipino","Finnish","French","Frisian","Ga","Galician","Georgian","German","Greek","Guarani","Gujarati","Hacker","Haitian Creole","Hausa","Hawaiian","Hebrew","Hindi","Hungarian","Icelandic","Igbo","Indonesian","Interlingua","Irish","Italian","Japanese","Javanese","Kannada","Kazakh","Kinyarwanda","Kirundi","Klingon","Kongo","Korean","Krio (Sierra Leone)","Kurdish","Kurdish (Soranî)","Kyrgyz","Laothian","Latin","Latvian","Lingala","Lithuanian","Lozi","Luganda","Luo","Macedonian","Malagasy","Malay","Malayalam","Maltese","Maori","Marathi","Mauritian Creole","Moldavian","Mongolian","Montenegrin","Nepali","Nigerian Pidgin","Northern Sotho","Norwegian","Norwegian (Nynorsk)","Occitan","Oriya","Oromo","Pashto","Persian","Pirate","Polish","Portuguese (Brazil)","Portuguese (Portugal)","Punjabi","Quechua","Romanian","Romansh","Runyakitara","Russian","Scots Gaelic","Serbian","Serbo-Croatian","Sesotho","Setswana","Seychellois Creole","Shona","Sindhi","Sinhalese","Slovak","Slovenian","Somali","Spanish","Spanish (Latin American)","Sundanese","Swahili","Swedish","Tajik","Tamil","Tatar","Telugu","Thai","Tigrinya","Tonga","Tshiluba","Tumbuka","Turkish","Turkmen","Twi","Uighur","Ukrainian","Urdu","Uzbek","Vietnamese","Welsh","Wolof","Xhosa","Yiddish","Yoruba","Zulu"]
text = str("Brown, who had transferred to Missouri from Auburn, led the Southeastern Conference with 19.9 points per game last season. Missouri went 7-8 after the start of February and missed the NCAA tournament for the first time in six years.")
count = 0

for v in homeArray:
    for y in targetArray:
        print post_request(v,y,text)
        print("")
        print spinner(v,y,text)
        #print v
        #print y
        print targetLangArray[count]
        print("")
        print("")
        count +=1

#print translate("en","zh-CN","Hello").encode('utf-8')
#print translate("zh-CN","en",translate("en","zh-CN","hello").encode('utf-8'))


##Need post request because we're sending a large file
##In translate.google.com: the website comes before the "?" and paramaters follow the "?"

##Apache (or whatever web server Google uses) limits the size of the request we can make - using this code, we can translate an entire book if we want to whereas you would normally be limited within Google Translate
##TUTORIAL #20-B by Chris Reeves


