import glob, os, shutil, random
from collections import defaultdict, Counter

random.seed(0)
OUT = "dataset_out"

# group images by source photo
groups = defaultdict(list)
for p in glob.glob("pool/images/*.*"):
    stem = os.path.splitext(os.path.basename(p))[0]
    groups[stem.split(".rf.")[0]].append(p)

def classes_of(img):
    stem = os.path.splitext(os.path.basename(img))[0]
    lbl = f"pool/labels/{stem}.txt"
    return {int(l.split()[0]) for l in open(lbl) if l.split()}

# give each group a "primary" class: the rarest class it contains
freq = Counter()
for imgs in groups.values():
    for c in classes_of(imgs[0]):
        freq[c] += 1
by_primary = defaultdict(list)
for g, imgs in groups.items():
    cs = classes_of(imgs[0])
    primary = min(cs, key=lambda c: freq[c])
    by_primary[primary].append(g)

# 80/20 split within each primary class
train_groups, val_groups = [], []
for primary, gs in by_primary.items():
    random.shuffle(gs)
    n_val = max(1, round(0.2 * len(gs)))
    val_groups += gs[:n_val]
    train_groups += gs[n_val:]

def copy(img, split):
    stem = os.path.splitext(os.path.basename(img))[0]
    os.makedirs(f"{OUT}/images/{split}", exist_ok=True)
    os.makedirs(f"{OUT}/labels/{split}", exist_ok=True)
    shutil.copy(img, f"{OUT}/images/{split}/{os.path.basename(img)}")
    shutil.copy(f"pool/labels/{stem}.txt", f"{OUT}/labels/{split}/{stem}.txt")

for g in train_groups:
    for img in groups[g]:
        copy(img, "train")
for g in val_groups:
    copy(sorted(groups[g])[0], "val")   # one copy per photo

# report
for split in ["train", "val"]:
    n_img = len(glob.glob(f"{OUT}/images/{split}/*.*"))
    per = Counter()
    for lbl in glob.glob(f"{OUT}/labels/{split}/*.txt"):
        for c in {int(l.split()[0]) for l in open(lbl) if l.split()}:
            per[c] += 1
    print(split, "images:", n_img, "| images per class:", dict(per))