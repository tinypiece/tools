# -*- coding: utf-8 -*-

from pyPdf import PdfFileWriter, PdfFileReader

def main(output_file, input_files):
    print "****** \"" + output_file + "\" への書き込み開始 ******"

    output = PdfFileWriter()
    total_pages = 0

    for f in input_files:
        # expect filename as "*.pdf"
        if f[-4:] != ".pdf":
            print "skipped file: ", f
            continue
        else:
            input = PdfFileReader(file(f, 'rb'))
            num_pages = input.getNumPages()
            total_pages += num_pages
            print f, "->", str(num_pages) + " ページ"
            for i in xrange(0, num_pages):
                output.addPage(input.getPage(i))

    outputStream = file(output_file, 'wb')
    output.write(outputStream)
    print total_pages, "ページ 書き込み"
    outputStream.close()

    print
    print "### チェック ###"

    resultFile = PdfFileReader(file(output_file, 'rb'))
    num_pages = resultFile.getNumPages()
    print output_file, "->", str(num_pages), "ページあります"

    print "****** \"" + output_file + "\" への書き込み完了 ******"


if __name__ == '__main__':
    import argparse
    description = "concatinate input PDF files"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-o", "--output", default="output.pdf")
    parser.add_argument("-i", "--input", nargs='*', required=True)
    parser.add_argument("-v", "--version", action='version',
                        version="%(prog)s 1.0")
    args = vars(parser.parse_args())
    
    main(args['output'], args['input'])