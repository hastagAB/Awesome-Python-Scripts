def itirate_of(logfile):
    logging.debug("itirate_of")
    lineCount = 0
    start_flag = 0
    elementarray = []
    array2 = []
    with open(logfile, "r") as ifile:
        for line in ifile:
            lineCount += 1
            if "<log4j:event" in line:
                logging.debug("found <log4j:event")
                array2.append(line)
                logging.debug("line: %s", line)
                start_flag = 1

            elif "</log4j:event>" in line:
                logging.debug("found </log4j:event>")
                start_flag = 0
                array2.append(line)
                logging.debug("line: %s", line)
                elementarray.append(array2)
                array2 = []

            elif start_flag == 1:
                logging.debug("startflag set")
                array2.append(line)
                logging.debug("line: %s", line)

        return elementarray, lineCount


def parse(xmlelement):
    logging.debug("parse")
    root = ET.fromstring(xmlelement)
    message = root[0].text
    logger = root.attrib['logger']
    timestamp = root.attrib['timestamp']
    error_level = root.attrib['level']
    thread = root.attrib['thread']

    return message, logger, timestamp, error_level, thread


def ruleset(rule, message, logger, timestamp, error_level, thread):
    logging.debug("ruleset")
    compiled = message + logger + timestamp + error_level + thread
    if args.regexsearch:
        finder = re.findall(rule, compiled)
        if finder:
            frontend(message, logger, timestamp, error_level, thread)
    if args.asciisearch:
        if rule in compiled:
            frontend(message, logger, timestamp, error_level, thread)
    else:
        if rule in compiled:
            frontend(message, logger, timestamp, error_level, thread)


def frontend(message, logger, timestamp, error_level, thread):
    logging.debug("frontend")
    if args.frontend:
        print(eval(args.frontend))
    else:
        print("{}: {} - {}".format(error_level, logger, timestamp))


def main(logfile, itir_file, ruleset, frontend):
    logging.debug("main")
    errors = 0
    warns = 0
    if args.asciisearch:
        rule = args.asciisearch
    elif args.regexsearch:
        rule = args.regexsearch
    else:
        rule = ""
    elementarray, lineCount = itir_file(logfile)
    string = ""
    for i in range(len(elementarray)):
        xmlelement = "".join(elementarray[i])
        message, logger, timestamp, error_level, thread = parse(xmlelement.replace("log4j:", "").rstrip('\n'))
        ruleset(rule, message, logger, timestamp, error_level, thread)
        if error_level == "ERROR":
            errors += 1
        if error_level == "WARN":
            warns += 1


if __name__ in '__main__':
    import xml.etree.ElementTree as ET
    import logging
    import sys
    import re
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', help='log4j file to parse', type=str, required=True)
    parser.add_argument('-as','--asciisearch', help='ascii search pattern', type=str, required=False, default="")
    parser.add_argument('-rs','--regexsearch', help='regex search pattern', type=str, required=False, default="")
    parser.add_argument('-fe', '--frontend', help='customize output: message, logger, timestamp, error_level, thread', type=str, required=False, default="error_level, logger, timestamp")
    args = parser.parse_args()

    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    main(args.file, itirate_of, ruleset, frontend)
