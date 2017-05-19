import hug

@hug.get(output=hug.output_format.text)
@hug.cli()
def rcfile():
    """Returns a vimrc file"""
    with open('samples/sample_vimrc') as f:
        rcfile = ''
        for line in f:
            rcfile += f.readline()
    return rcfile

if __name__ == '__main__':
    add.interface.cli()
