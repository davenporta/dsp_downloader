import requests
from tqdm import tqdm
from PyPDF2 import PdfFileMerger, PdfFileReader
from stream_response import ResponseStream

# initialize merge object
mergedTextbook = PdfFileMerger()

print("Initiating download from www.dspguide.com")

for chapter in tqdm(range(1,35)):
    # get chapter pdf from website
    url = 'http://www.dspguide.com/CH%s.PDF' % chapter
    r = requests.get(url, allow_redirects=True, stream=True)

    # wrap request in File like stram with seek() method
    stream = ResponseStream(r.iter_content(64))

    # append to main pdf
    mergedTextbook.append(PdfFileReader(stream, strict=False))

# write pdf to file
mergedTextbook.write("Digital Signal Processing - Smith.pdf")
print("Complete")