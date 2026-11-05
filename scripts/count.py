import glob, os
from collections import Counter

imgs = glob.glob("pool/images/*.*")
groups = {os.path.basename(p).split(".rf.")[0] for p in imgs}
print("Total images:", len(imgs))
print("Unique source photos (before .rf.):", len(groups))

per_class = Counter()
for lbl in glob.glob("pool/labels/*.txt"):
    for l in open(lbl):
        if l.split():
            per_class[int(l.split()[0])] += 1
print("Boxes per class:", dict(per_class))

img_class = Counter()
for lbl in glob.glob("pool/labels/*.txt"):
    for c in {int(l.split()[0]) for l in open(lbl) if l.split()}:
        img_class[c] += 1
print("Images containing each class:", dict(img_class))