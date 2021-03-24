#!/usr/bin/env python3

from halo import Halo
from PIL import Image, ImageColor
import numpy
import argparse
import requests
import math
import os


def get_repo_tree(repo_owner: str, repo_name: str, branch_name: str):
    res = requests.get(
        f'https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees/{branch_name}?recursive=1',
        headers={
            'Accept': 'application/vnd.github.v3+json',
        }
    )

    return res.json()


def get_repo_files(repo_owner: str, repo_name: str, branch_name: str):
    repo_tree = get_repo_tree(repo_owner, repo_name, branch_name)

    repo_files = {}
    for file in repo_tree.get('tree', []):
        repo_files[file.get('path')] = file.get('sha')

    return repo_files


def get_height_for_width(width: int, total_pixels: int):
    return math.ceil(total_pixels/width) + 1


def get_appropriate_width_height(total_pixels: int):
    for width in range(50, 50000, 100):
        height = get_height_for_width(width, total_pixels)
        ratio = height / width

        if ratio > 0.65 and ratio < 0.85:
            return (width, height)

    return (50, get_height_for_width(50, total_pixels))


parser = argparse.ArgumentParser(
    description='Colorise a Github repo'
)

parser.add_argument(
    'repo',
    help='Which repo should we use'
)

parser.add_argument(
    '--branch',
    '-b',
    help='Which branch to use',
    default='master'
)

parser.add_argument(
    '--width',
    '-w',
    help="How wide to make the image",
    type=int
)

args = parser.parse_args()

repo_parts = args.repo.split('/')

tree = get_repo_files(repo_parts[0], repo_parts[1], args.branch)


hash_length = 36
hex_length = 6

total_pixels = (hash_length/hex_length) * len(tree)

if args.width:
    image_width = args.width
    image_height = get_height_for_width(args.width)
else:
    (image_width, image_height) = get_appropriate_width_height(total_pixels)

data = numpy.zeros((image_height, image_width, 3), dtype=numpy.uint8)

x = 0
y = 0

with Halo(text='Generating image', spinner='moon'):

    for sha in tree.values():
        short_sha = sha[:36]
        chunks = [short_sha[i:i+6] for i in range(0, len(short_sha), 6)]

        for chunk in chunks:
            x += 1
            if x >= image_width:
                x = 0
                y += 1

            data[y, x] = list(ImageColor.getrgb(f"#{chunk}"))

image = Image.fromarray(data)

dir = './images'

if not os.path.exists(dir):
    os.makedirs(dir)

filename = os.path.join(dir, args.repo.replace('/', '-')+'.png')

image.save(filename, "png")

print(f'Saved to {filename}')
