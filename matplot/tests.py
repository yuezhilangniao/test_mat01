from django.test import TestCase

# Create your tests here.
def test():
    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams['font.family'] = ['sans-serif']
    # 在我的 notebook 里，要设置下面两行才能显示中文
    plt.rcParams['font.family'] = ['sans-serif']
    # 如果是在 PyCharm 里，只要下面一行，上面的一行可以删除
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["375 g 营销一部",
              "75 g 营销二部",
              "250 g 营销三部",
              "300 g 营销四部"]

    data = [float(x.split()[0]) for x in recipe]
    ingredients = [x.split()[-1] for x in recipe]

    def func(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"))

    ax.legend(wedges, ingredients,
              # title="部门列表",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("各个部门业绩占比", fontproperties="SimHei")

    plt.show()