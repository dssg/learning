
def print_versions():
    import types
    unversioned = []
    print "Modules with __version__:"
    for val in globals().values():
        if isinstance(val, types.ModuleType):
            try:
                ver = val.__version__
                print "\t%s %s" %((val.__name__ + ":").ljust(15), ver.rjust(10))
            except:
                unversioned.append(val.__name__)

    print "\nModules with no __version__:"
    for mod in unversioned:
        print "\t%s" % mod

print_versions()
