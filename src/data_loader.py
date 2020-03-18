import os
import re
from chardet import detect
from .utils.stopwords import stop_words
from .utils.progress_printer import ProgressPrinter

def parse_email(buf):
    # Then, split the header and the main body
    _=buf.find("\n\n")
    header, main_body=buf[:_],buf[_:] # Then, split the main body

    # get content and sender
    content=re.sub(r"[^a-z]"," ",main_body.lower()).split()
    # content=list(set(content))
    content=list(filter(lambda w:w not in stop_words,content))

    sender=None
    _from=re.findall("From:[^\n]*\n",header)
    for f in _from:
        tmp=re.findall("[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+",f)
        tmp=re.findall("[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[\.a-zA-Z0-9_-]+",f)
        if tmp:
            sender=tmp[0]
            break
    sender_domain=sender[sender.find("@"):] if sender else None
    
    ret={
        "content": content,
        "sender_domain": sender_domain,
    }
    return ret

def read_file(file_name):
    try:
        with open(file_name,"r") as f:
            return f.read()
    except:
        with open(file_name,"rb+") as f:
            buf=f.read()
        with open(file_name,"r",encoding=detect(buf)["encoding"]) as f:
            return f.read()
    raise FileNotFoundError

def data_loader(src_path,utf8_only=False):
    ret=[]
    lines=read_file(os.path.join(src_path,"label","index")).splitlines()
    pp=ProgressPrinter(len(lines))
    for line in lines:
        try:
            label,origin_file_name=line.split(' ')
            if label=="ham":
                label=0
            else:
                assert label=="spam"
                label=1
            file_name=os.path.join(src_path,"label",origin_file_name)
            if utf8_only:
                with open(file_name,"r") as f:
                    buf=f.read()
            else:
                buf=read_file(file_name)
            curr_email=parse_email(buf)
            curr_obj={
                "input":curr_email,
                "label":label,
                "source_file":origin_file_name,
            }
            ret.append(curr_obj)
        except:
            pass
        pp.go()
    return ret
