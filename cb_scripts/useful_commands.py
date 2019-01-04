#!/usr/bin/env python3

"""Useful commands."""


def main():
    """Print useful commands."""
    print("""
    # Update Python in Virtual Envs need to automate this part
    # echo "run lsvirtualenv -b | xargs -I % sh -c 'find ~/.virtualenvs/% -type l -delete; virtualenv ~/.virtualenvs/%'"
    find ~/.virtualenvs ! -path ~/.virtualenvs -maxdepth 1 -type d | xargs -I % sh -c 'find % -type l -delete;virtualenv %'

    # Python
    ## virtualenvs
    echo "and pip3 freeze --local | grep -v ‘^\-e’ | cut -d = -f 1 | xargs pip3 install -U"
    #lsvirtualenv -b | xargs -I % sh -c 'source /Users/wheeljack/.virtualenvs/%/bin/activate;pip3 freeze --local | grep -v ‘^\-e’ | cut -d = -f 1 | xargs pip3 install -U'

    ### Update packages for each virtualenv
    ls -d ~/.virtualenvs/*/ | xargs -I % sh -c 'source %/bin/activate;pip3 freeze --local | grep -v ‘^\-e’ | cut -d = -f 1 | xargs pip3 install -U;deactivate'

    ### create requirements.txt for each virtualenv
    ls -d ~/.virtualenvs/*/ | xargs -I % sh -c 'source %/bin/activate;pip3 freeze --local > %requirements.txt; deactivate'
    """)


if __name__ == "__main__":
    main()
