# weather-cli

Simple CLI app to get weathet forecast


# Set up

`python3 -m venv venv`

`source venv/bin/activate`

`python3 -m pip install -r requirements.txt`

# Usage


```
% python3 forecast.py --help
Usage: forecast.py [OPTIONS] CITY

Arguments:
  CITY  [required]

Options:
  --count INTEGER                 [default: 3]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```


# Example
```
% python3 forecast.py Ternopil --count=5
2021-02-10 09:00:00: -5.62°C
2021-02-10 12:00:00: -3.14°C
2021-02-10 15:00:00: -3.78°C
```