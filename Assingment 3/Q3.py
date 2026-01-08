from random import sample

def copy_checker(com):
    print("in use ........")
    def top_occurance(dictionay,max_val=999999999):
        max_dict=0
        most_occured_words=[]
        for key,value in dictionay.items():
            if max_dict<=value and value<max_val:
                max_dict=value
        for key,value in dictionay.items():
            if max_dict==value:
                most_occured_words.append(key)
        return max_dict , most_occured_words

    with open(com,"r") as f :
        data=f.readlines()
        all_work=""
        for small_data in data:
            all_work+=small_data.strip()
            all_work+=" "
    info_content={}
    words=[all_work]
    spliters=[" ","-",".","/",",","'",";",":","_"]
    for split_value in spliters:
        new_word=[]
        for word in words: 
            new_word.extend(word.split(split_value))
        words=new_word

    total_words=0                                                #we will get the count of all the words

    for word in words:
        if word=="":
            continue
        info_content[word.lower()]=info_content.get(word.lower(),0)+1
        total_words+=1
    
    unique_words_list=list(info_content.keys())
    unique_words_len=len(unique_words_list)    # unique words only

    f1_factor=unique_words_len/total_words
    top_5_occurance=0
    top_5_occurance_dict=[]
    words=0
    max_occured=99999999
    loop=0
    while loop<6:  #words<5 and 
        loop+=1
        occurance=top_occurance(info_content,max_occured)
        max_occured=occurance[0]
        if words+len(occurance[1])>5:
            top_5_occurance+=occurance[0]*(5-words)
            top_5_occurance_dict.append(occurance[1][:5-words])
            words=5
            break

        else:   
            words+=len(occurance[1])
            top_5_occurance+=occurance[0]*len(occurance[1])
            top_5_occurance_dict.append(occurance[1])
    f2_factor=top_5_occurance/total_words

    sentences=all_work.split(".")
    num_sentences=len(sentences)
    factor_3_portion1=0
    for sentence in sentences:
        sentence_words=[sentence]
        spliters=[" ","-",".","/",",","'",";",":"]
        for split_value in spliters:
            new_sentence_word=[]
            for sentence_word in sentence_words: 
                new_sentence_word.extend(word.split(split_value))
            sentence_words=new_sentence_word
        if len(sentence_words)>35 or len(sentence_words)<5:
            factor_3_portion1+=1

    f3_factor=factor_3_portion1/num_sentences
    patterns = [",.", ",:", ",;", ".:", ".;", ";:", ";.","..",".,",",,"]
    pattern_cout_dict={pattern:0 for pattern in patterns}
    for pattern in patterns:
        pattern_cout_dict[pattern]+=all_work.count(pattern)
    f4_factor=sum(pattern_cout_dict.values())/total_words

    f5_factor=None
    if total_words >750:
        f5_factor=1
    else:
        f5_factor=0
    net_score=4 + f1_factor*6 + f2_factor*6 -f3_factor - f4_factor - f5_factor
    line_3_matter=""
    for small_list in top_5_occurance_dict:
        for element in small_list:
            line_3_matter+=f"{element} : {info_content[element]}   "
    random_numbers=sample(range(unique_words_len),5)
    line_4_matter=""
    for random_num in random_numbers:
        line_4_matter+=unique_words_list[random_num]
        line_4_matter+="  "

    return net_score,line_3_matter,line_4_matter

num_copies=int(input("enter the number of copies : "))
# f=open("output.txt","w")
# f.close()
for i in range (1,num_copies+1):
    copy_name=f"FILE{i}.txt"
    # copy_name="FILE1.txt"
    output=copy_checker(copy_name)
    with open("output.txt","a") as f :
        f.write(copy_name)
        f.write("\n")
        f.write(f"score : {output[0]}")
        f.write("\n")
        f.write(output[1])
        f.write("\n")
        f.write(output[2])
        f.write("\n")

