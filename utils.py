def confirm(msg, enterConfirms=True):
    response = raw_input(msg + " ")
    return (enterConfirms and not response) or response.lower() == "y"


def printAndExit(msg, exitCode):
    print(msg)
    sys.exit(exitCode)


def success(msg):
    printAndExit(msg, exitCode=0)


def die(msg, exitCode=0):
    print(msg)
    sys.exit(exitCode)

