
# nbpresent
> remix your Jupyter Notebooks as interactive slideshows

## Usage
After [installing](#install) (and potentially enabling) as appropriate for your environment, after launching the Jupyter Notebook, all Notebooks will show two new buttons that show/hide the _slide sorter_ and the _presenter view_. Launching the sorter will trigger an interactive tour, which can be relaunched by clicking the _question mark_ in the top right corner of the sorter.

When you are happy with your presentation, you can download the standalone HTML file from the _File -> Download as -> Presentation (.html)_ menu item.

## Install

> Note: installing directly off this repo won't work, as we don't ship the built JavaScript and CSS assets. See more about [developing](#develop) below.

### `pip`
```shell
pip install nbpresent
python -m nbpresent.install
```

Then either run 
```python
%reload_ext nbpresent
```

_every time you start the notebook_ or _enable_ the extension for every notebook launch:
```shell
python -m nbpresent.install --enable --user
```

> `nbpresent.install` accepts all of the same arguments as `jupyter nbextension install`.

### `conda`
```shell
conda install -c anaconda-nb-extensions/label/dev nbpresent
```

This will enable `nbpresent` by default.

## Export
Stock `nbconvert` doesn't store quite enough information, so you'll need to do something like this:
```shell
nbpresent -i notebooks/README.ipynb -o README.html
```
The resulting file can be hosted and viewed (but not edited!) on any site.

If you have installed [nbbrowserpdf](https://github.com/Anaconda-Server/nbbrowserpdf), you can also export to pdf:
```shell
nbpresent -i notebooks/README.ipynb -f pdf -o README.pdf
```

You can also pass in and get back streams:
```shell
cmd_that_generates_ipynb | nbpresent -f pdf > README.pdf
```

Here's the whole doc:


```python
!nbpresent --help
```

    usage: nbpresent [-h] [-i IPYNB] [-o OUTFILE] [-f {html,pdf}]
    
    Generate a static nbpresent presentation from a Jupyter Notebook
    
    optional arguments:
      -h, --help            show this help message and exit
      -i IPYNB, --ipynb IPYNB
                            Input file (otherwise read from stdin)
      -o OUTFILE, --outfile OUTFILE
                            Output file (otherwise write to stdout)
      -f {html,pdf}, --out-format {html,pdf}
                            Output format


## Develop
This assumes you have cloned this repository locally:
```
git clone https://github.com/Anaconda-Server/nbpresent.git
cd nbpresent
```

### Repo Architecture

The `nbpresent` nbextension is built from `./src` into `./nbpresent/static/nbresent` with:
- `less` for style
- `es6` (via `babel`) for javascript
- `browserify` for packaging

The `nbpresent` python module (server component) is stored in the `/nbpresent` folder

### Getting Started
You'll need conda installed, either from [Anaconda](https://www.continuum.io/downloads) or [miniconda](http://conda.pydata.org/miniconda.html). You can import a Python 3.5 development environment named `nbpresent` from `./environment.yml`.

```shell
conda update env
source activate nbpresent
```

We _still_ use `npm` for a lot of dependencies, so then run:
```shell
npm install
npm run build:all
```

### Ensure development asset loading
To ensure that you always get the right assets, install the nbextension with the `symlink`, `force` and `enable` options:
```shell
python -m nbpresent.install --overwrite --symlink --enable --user
```
You may also want to pass in `--prefix` instead of user.

### Chore Automation
| Task | Command |
|------|---------|
| Build all of the front end assets with sourcemaps for development | `npm run build` |
| Rebuild on every save | `npm run watch` |
| Rebuild all of the front end assets, and optimize it | `npm run dist` |
| Run the CasperJS and `nose` tests  | `npm run test` |
| Check code style |  `npm run lint` |
| Build the conda package | `npm run pkg:conda` |
| Build and upload the pypi package | `npm run pkg:pypi` |
| Build the ESDoc and Sphinx documentation | `npm run docs` |
