import pyperclip
import re
from typing import Literal
from pathlib import Path
from zipfile import ZipFile

# STEP 1

# TODO get the actual text

def fetch_data():
    text_content=None
    text_content=pyperclip.paste()
    print(text_content)
    if text_content is None:
        raise Exception("Any value was copy")
    return text_content

# Step 2

## TODO Create regex exp to match email and numbers

def match_phone_number(message:str):
    pattern=r'\+?\d?\s?\b[\d]{3}\b[\s/-_\.]?[\d]{3}[\s/-_\.]?[\d]{4}' # area?_?3_?3_?_4
    matcher=re.compile(pattern=pattern)
    result=matcher.findall(message)
    return result
    
def match_emails(message:str):
    pattern=r'[\w_\+\-\.]+[@][\w]{2,}[\.]+[\w]{2,}' # host@domain.something
    matcher=re.compile(pattern=pattern)
    result=matcher.findall(message)
    return result

## Step 3 

## TODO concatenate results

def concatenate_matches(emails,phones):
     # Check for matches
    if isinstance(emails,list) and len(emails)==0:
        print("Any email was found\n")
        emails=[]
    if isinstance(phones,list) and len(phones)==0:
        print("Any phone was founded\n")
        phones=[]
    # Manage empty matches
    if not emails and not phones:
        print("Any contact info was founded. Nothing to report...")
        return ""
    
    # Combine matches
    final_match="\n".join(emails+phones) 
    return final_match

## Step 4

## TODO generate report

def generate_report(content:str):
        if len(content) > 0:
           try:
                path=write_report(content=content)
                read_report(path=path)
                return str(path.absolute())
           except Exception as e:
               print("Something went wrong: ",e)
        return False

def write_report(content:str):
    path=Path.cwd()
    path=path/"contact_info_report.txt"
    try:
        with open(path,"w") as f :
            f.write(content)
            f.close()
            print("Reported succesfully generated¡¡¡\n")
        return path
    except Exception as e:
        raise e
        
        
def read_report(path:Path):
    if path.exists() and path.is_file():
        with open(path,"r") as f:
            print("Reading report...\n")
            print(f.read())
            f.close()
    else:
        print(f"The path : {path} don't contain any file to read")
        

## Step 5

## TODO compress report
def compress_report(path:str):
    path_obj=Path(path)
    if path_obj.exists() and path_obj.is_file():
        path="report_compress.zip"
        with ZipFile(path,"w") as z:
            z.write(path_obj.name)
            z.close()
            print("compressed file succesfully¡¡¡")
                
        return path
    return False
            





## Step 6

## TODO Move report and clean the cwd

class AnyContentWasFound(Exception):
    pass

def extractor_app():
    emails=None
    phones=None
    try:
        text=fetch_data()
        emails=match_emails(text)
        phones=match_phone_number(text)
        content_report=concatenate_matches(emails=emails,phones=phones)
        status=generate_report(content=content_report)
        
        # TODO INTEGRATE GIT 
        # TODO compress_report() branche
        if status is not False:
            compress_report(path=status)
        else:
            print("Ther's an error generating the report")

        # TODO move_report() branche
        
    except Exception as e:
        print("Something happened: ",e)


extractor_app()