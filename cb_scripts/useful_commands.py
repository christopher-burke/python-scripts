#!/usr/bin/env python3

"""Useful commands."""


def main():
    """Print useful commands."""

    # Python
    # Commands for virtualenvs:
    # Update Python in Virtual Envs need to automate this part.
    print(r"""find ~/.virtualenvs ! -path ~/.virtualenvs -maxdepth 1 -type d | xargs -I % sh -c 'find % -type l -delete;virtualenv %'""")

    # Update packages for each virtualenv.
    print(r"""ls -d ~/.virtualenvs/*/ | xargs -I % sh -c 'source %/bin/activate;pip3 freeze --local | grep -v ‘^\-e’ | cut -d = -f 1 | xargs pip3 install -U;deactivate'""")

    # create requirements.txt for each virtualenv.
    print(r"""ls -d ~/.virtualenvs/*/ | xargs -I % sh -c 'source %/bin/activate;pip3 freeze --local > %requirements.txt; deactivate'""")

    # Ubuntu
    # Blank screen on Ubunutu.
    print(r"sudo sh -c 'vbetool dpms off;read ans; vbetool dpms on'")


if __name__ == "__main__":
    main()
