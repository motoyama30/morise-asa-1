"""Make progress chart of onolab members."""
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class User:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.progress = [0] * 10


def get_progress() -> List[User]:
    cur = Path(".")
    users = list(
        filter(lambda x: x.is_dir() and x.name not in IGNORE, sorted(cur.iterdir()))
    )

    progress = []
    # user ごとの progress を取得する
    for user in users:
        u = User(user.name, user)
        for chap, max_cnt in zip(range(n_chapters), n_codes):
            # user/chapterXX の path (章だけ 1-indexed なので num+1)
            chapter_path = Path(user / f"chapter{chap+1:02d}")

            # user/chapterXX に含まれる .py ファイルをカウント
            py_files = list(chapter_path.glob("[0-9][0-9].py"))
            print(f"{chapter_path}", py_files)

            # 問題数は max_cnt が上限で、それ以上のファイル数が含まれる場合は max_cnt にする
            solved_cnt = min(len(py_files), max_cnt)
            u.progress[chap] = solved_cnt
        progress.append(u)

    return progress


def plot_progress(users: np.array, scores: np.array):
    # 描画されるグラフのサイズを指定
    plt.figure(figsize=(8, 6))

    # 各章ごとに棒グラフを積み上げていく
    for chap in range(n_chapters):
        label = f"Chapter {chap+1}"
        bottom = np.sum(scores[:, :chap], axis=1)
        plt.bar(
            users,
            scores[:, chap],
            bottom=bottom,
            align="center",
            tick_label=users,
            label=label,
        )

    # グラフの設定
    plt.xticks(rotation=30, fontsize=10)
    plt.ylim(0, sum(n_codes))

    # 凡例をグラフの外側に表示する
    plt.legend(bbox_to_anchor=(1.28, 1.0))
    plt.subplots_adjust(right=0.8)

    plt.savefig("progress.png")


def main():
    data = get_progress()
    users = np.array([user.name for user in data])
    scores = np.array([user.progress for user in data])

    if scores.size:
        plot_progress(users, scores)


if __name__ == "__main__":
    # 章数と各章の問題数
    n_chapters, n_codes = 7, [6, 19, 9, 15, 10, 11, 18]

    # progress bar に表示しないディレクトリ名
    IGNORE = [".git", ".github", ".automation"]

    sns.set()
    sns.set_palette("hls", n_chapters)

    main()
