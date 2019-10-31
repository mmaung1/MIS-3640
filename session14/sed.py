def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f_w = open(dest,'w')
    with open(source, 'r') as f_r: #r is for read 
        for line in f_r:
            new_line = line.replace(pattern, replace)
            f_w.write(new_line)
    f_w.close()


pattern = 'man '
replace = 'woman '
source = 'session14/output.txt'
dest = 'session14/output2.txt'
sed(pattern,replace,source,dest)