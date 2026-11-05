import os, shutil, glob, yaml
from collections import Counter

# ---- EDIT THESE TWO LINES ----
SRC = r"D:\Repos\IAT 360\downloads\weeds-plants1.v3i.yolov8"
PREFIX = "weeds"
# ------------------------------

# your master class ids
NEW = {"fireweed": 0, "himalayan balsam": 1, "japanese knotweed": 2, "purple loosestrife": 3}

def norm(n):
    return n.lower().replace("-", " ").replace("_", " ").strip()

names = yaml.safe_load(open(f"{SRC}/data.yaml"))["names"]
if isinstance(names, dict):
    names = [names[i] for i in sorted(names)]
idmap = {i: NEW[norm(n)] for i, n in enumerate(names) if norm(n) in NEW}
print("Mapping:", {names[i]: v for i, v in idmap.items()})

os.makedirs("pool/images", exist_ok=True)
os.makedirs("pool/labels", exist_ok=True)

counts, kept, skipped = Counter(), 0, 0
for split in ["train", "valid", "test"]:
    for lbl in glob.glob(f"{SRC}/{split}/labels/*.txt"):
        lines = []
        for l in open(lbl):
            p = l.split()
            if p and int(p[0]) in idmap:
                lines.append(" ".join([str(idmap[int(p[0])])] + p[1:]))
        if not lines:
            skipped += 1
            continue
        stem = os.path.splitext(os.path.basename(lbl))[0]
        img = next(iter(glob.glob(f"{SRC}/{split}/images/{stem}.*")), None)
        if not img:
            continue
        ext = os.path.splitext(img)[1]
        shutil.copy(img, f"pool/images/{PREFIX}_{stem}{ext}")
        open(f"pool/labels/{PREFIX}_{stem}.txt", "w").write("\n".join(lines))
        for ln in lines:
            counts[int(ln.split()[0])] += 1
        kept += 1

print(f"Kept {kept} images, skipped {skipped} (only had dropped classes)")
print("Boxes per class id:", dict(counts))