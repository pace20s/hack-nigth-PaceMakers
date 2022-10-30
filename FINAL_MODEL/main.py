import openai
# import wget
import pathlib
import pdfplumber
import numpy as np


# def getPaper(paper_url, filename="random_paper.pdf"):
#     """
#     Downloads a paper from it's arxiv page and returns
#     the local path to that file.
#     """
#     downloadedPaper = wget.download(paper_url, filename)    
#     downloadedPaperFilePath = pathlib.Path(downloadedPaper)

#     return downloadedPaperFilePath

downloadedPaperFilePath = "./sample.pdf"

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


paperContent = pdfplumber.open(downloadedPaperFilePath).pages
showPaperSummary(paperContent)

#paperFilePath