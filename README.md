# repo-col

A small utility to generate an image based on the SHA vaules of a github tree.

## Usage

### Docker Usage

```bash
docker run -v $(pwd):/app/images philwc/repo-col [OWNER/REPO NAME]

docker run -v $(pwd):/app/images philwc/repo-col philwc/repo-col
```

### Manual Usage

```bash
pip3 install -r requirements.txt

./main.py [OWNER/REPO NAME]
```

## Help

### Docker Help

```bash
docker run -v $(pwd):/app/images philwc/repo-col -h
```

### Manual Help

```bash
pip3 install -r requirements.txt

./main.py -h
```

## Examples

### torvalds/linux

![torvalds/linux](images/torvalds-linux.png?raw=true "torvalds/linux")

### python/cpython

![python/cpython](images/python-cpython.png?raw=true "python/cpython")

### microsoft/vscode

![microsoft/vscode](images/microsoft-vscode.png?raw=true "microsoft/vscode")

### philwc/repo-col

![philwc/repo-col](images/philwc-repo-col.png?raw=true "philwc/repo-col")
