import openai
# import wget
# import pathlib
import pdfplumber
import numpy as np

PaperFilePath = "./sample2.pdf"

def showPaperSummary(paperContent):
    tldr_tag = "\n tl;dr:"
    openai.organization = 'org-CCY2sGmfLZVuGLoQQ3I1ScxI'
    openai.api_key = "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"
    engine_list = openai.Engine.list() 
    
    for page in paperContent:    
        text = page.extract_text() + tldr_tag
        response = openai.Completion.create(engine="davinci",prompt=text,temperature=0.3,
            max_tokens=140,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        print(response["choices"][0]["text"])


paperContent = pdfplumber.open(PaperFilePath).pages
showPaperSummary(paperContent)

#paperFilePath