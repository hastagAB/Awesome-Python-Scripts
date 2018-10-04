import sys
try:
    import aiml
except ImportError:
    print('[!] Failed to import the module')
    try:
        select = raw_input('[*] Attempt to auto-install aiml? [Y/n')
    except KeyboardInterrupt:
        print('\n[!] User Cancel')
        sys.exit(5)
    if select.strip().lower()[0] == 'y':
        print('[*] Trying to Install aiml... ')
        sys.stdout.flush()
        try:
            import pip
            pip.main(['install', '-q', 'aiml'])
            import aiml
            print('Finished')
        except Exception:
            print('Something happens PLease check your internet connection')
            sys.exit(5)

    elif select.strip().lower()[0] == 'n':
        print('[*] User cancel Auto-install')
        sys.exit(5)
        

kern = aiml.Kernel()
kern.learn('load.xml')
kern.respond('load aiml b')

while True:
    print(kern.respond(raw_input('Type your Message >>')))
