import PyPDF2

topics = []
with open('Text.pdf', 'rb') as f :
    topics = []
    pdf = PyPDF2.PdfFileReader(f)
    for page in range(pdf.numPages):
        pageObj = pdf.getPage(page)
        data = ""
        for i in pageObj.extract_text(0):
            if i != '\n':
                data += i
            else:
                break
        if data not in topics:
            topics.append(data)
for i in range(1, len(topics)):
    print(f"{i}. {topics[i]}")


# #%%
# import PyPDF2
# topics = []
# with open('Text.pdf', 'rb') as f :
#     pdf = PyPDF2.PdfFileReader(f)
#     pageObj = pdf.getPage(0)
#     data = pageObj.extract_text(0)
#     dots = ""
#     for i in data:
#         if i!= '\n':
#             dots += i
#         else:
#             break
    
# print(dots)

## %%
