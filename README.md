# repo-col

A small utility to generate an image based on the SHA vaules of a github tree.

## Usage

### Docker Usage

```bash
docker run -v $(pwd):/app/images philwc/repo-col [REPO NAME]

docker run -v $(pwd):/app/images philwc/repo-col philwc/repo-col
```

### Manual Usage

```bash
pip3 install -r requirements.txt

./main.py [REPO NAME]
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
