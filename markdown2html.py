#!/usr/bin/python3
<<<<<<< HEAD

"""
Markdown script using python.
"""
import sys
import os.path
=======
'''
A script that codes markdown to HTML
'''
import sys
import os
>>>>>>> 2c21f6ad539df954bd6e77782cd3d30f34d85706
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

<<<<<<< HEAD
    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1]) as read:
        with open(sys.argv[2], 'w') as html:
            unordered_start, ordered_start, paragraph = False, False, False
            # bold syntax
            for line in read:
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)

                # md5
                md5 = re.findall(r'\[\[.+?\]\]', line)
                md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
                if md5:
                    line = line.replace(md5[0], hashlib.md5(
                        md5_inside[0].encode()).hexdigest())

                # remove the letter C
                remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
                remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
                if remove_letter_c:
                    remove_c_more = ''.join(
                        c for c in remove_c_more[0] if c not in 'Cc')
                    line = line.replace(remove_letter_c[0], remove_c_more)

                length = len(line)
                headings = line.lstrip('#')
                heading_num = length - len(headings)
                unordered = line.lstrip('-')
                unordered_num = length - len(unordered)
                ordered = line.lstrip('*')
                ordered_num = length - len(ordered)
                # headings, lists
                if 1 <= heading_num <= 6:
                    line = '<h{}>'.format(
                        heading_num) + headings.strip() + '</h{}>\n'.format(
                        heading_num)

                if unordered_num:
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True
                    line = '<li>' + unordered.strip() + '</li>\n'
                if unordered_start and not unordered_num:
                    html.write('</ul>\n')
                    unordered_start = False

                if ordered_num:
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True
                    line = '<li>' + ordered.strip() + '</li>\n'
                if ordered_start and not ordered_num:
                    html.write('</ol>\n')
                    ordered_start = False

                if not (heading_num or unordered_start or ordered_start):
                    if not paragraph and length > 1:
                        html.write('<p>\n')
                        paragraph = True
                    elif length > 1:
                        html.write('<br/>\n')
                    elif paragraph:
                        html.write('</p>\n')
                        paragraph = False

                if length > 1:
                    html.write(line)

            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')
    exit (0)
=======
if __name__ == '__main__':

        # Test that the number of arguments passed is 2
            if len(sys.argv[1:]) != 2:
                        print('Usage: ./markdown2html.py README.md README.html',
                                              file=sys.stderr)
                        sys.exit(1)

                                    # Store the arguments into variables
                                    input_file = sys.argv[1]
                                            output_file = sys.argv[2]

                                                # Checks that the markdown file exists and is a file
                                                    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
                                                                print(f'Missing {input_file}', file=sys.stderr)
                                                                        sys.exit(1)

                                                                            with open(input_file, encoding='utf-8') as file_1:
                                                                                        html_content = []
                                                                                                md_content = [line[:-1] for line in file_1.readlines()]
                                                                                                        for line in md_content:
                                                                                                                        heading = re.split(r'#{1,6} ', line)
                                                                                                                                    if len(heading) > 1:
                                                                                                                                                        # Compute the number of the # present to
                                                                                                                                                                        # determine heading level
                                                                                                                                                                                        h_level = len(line[:line.find(heading[1])-1])
                                                                                                                                                                                                        # Append the html equivalent of the heading
                                                                                                                                                                                                                        html_content.append(
                                                                                                                                                                                                                                                    f'<h{h_level}>{heading[1]}</h{h_level}>\n'
                                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                        html_content.append(line)

                                                                                                                                                                                                                                                            with open(output_file, 'w', encoding='utf-8') as file_2:
                                                                                                                                                                                                                                                                        file_2.writelines(html_content)
>>>>>>> 2c21f6ad539df954bd6e77782cd3d30f34d85706
