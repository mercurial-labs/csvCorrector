def correctLine(line, delimiter):
    line.strip()
    if len(line) == 0:
        return ""
    line = f"\"{line}\"\n"
    line = line.replace(delimiter, "\",\"")
    return line


def correctFile(input, output, delimiter):
    try:
        outfile = open(output, 'w')
    except Exception:
        print('Error while opening file')
        return {'error': 'Error while opening file for writing.'}

    try:
        with open(input, 'r') as inpFile:
            for line in inpFile:
                corrected = correctLine(line, delimiter)
                outfile.write(corrected)
        outfile.close()
    except Exception as e:
        print('Error while correcting', e)
        return {'error': 'Error while correcting file.'}
    return {}

# correctFile("/Users/schaud3/Documents/Docs/OneDrive - Walmart Inc/Official/Features/GNFR migration/inpTest.csv","/Users/schaud3/Documents/Docs/OneDrive - Walmart Inc/Official/Features/GNFR migration/output.csv","|")