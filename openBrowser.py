import webbrowser


def openBrowser(address):
    """
    Opens web browser at an address.

    :param str address: address of the web page to open
    
    """
    if type(address) != str:
        raise TypeError("String argument expected.")
    webbrowser.open_new(address)
