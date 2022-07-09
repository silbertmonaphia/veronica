def pickone(list_):
    import random
    return random.choice(list_)


def generate_meal():
    # 要求：30天不重样，早餐内不重样(30款)，午晚餐内不重样(60款)
    carbo = ['米饭', '面条', '红薯', '紫薯', '豆腐']
    protein = ['虾', '鱼', '鸡', '猪', '牛']
    vagitables = {
        'leaf': ['西生菜', '油麦菜', '菠菜', '菜心',
                 '包菜', '白菜', '西洋菜', '茼蒿',
                 '空心菜', '落葵', '芥菜', '芥兰',
                 '番薯苗', '韭菜', '红苋'
                 ],
        'other': ['西兰花', '花椰菜', '西芹',
                  '胡萝卜', '西红柿', '茄子',
                  '苦瓜', '南瓜',
                  '四季豆', '荷兰豆', '白萝卜',
                  '紫甘蓝', '莴笋', '芦笋(Asparagus)', '竹笋',
                  '丝瓜(Loofah)','节瓜','蒲瓜','青瓜/黄瓜','冬瓜','西葫芦'
                 ],
        'mushroom': ['香菇', '平菇', '金针菇',
                     '木耳', '银耳', '虫草花',
                     '杏鲍菇','猴头菇'
                    ]
    }

    carbo_cook = ['蒸', '煮', '炒', '煎', '炸', '烤']
    protein_cook = ['蒸', '煮', '炒', '煎', '炸', '烤']
    vage_cook = ['蒸', '煮', '炒', '煎', '炸', '烤']

    lst = []
    lst.append(pickone(carbo_cook) + pickone(carbo))
    lst.append(pickone(protein_cook) + pickone(protein))
    lst.append(pickone(vage_cook) + pickone(vagitables['leaf']))
    lst.append(pickone(vage_cook) + pickone(vagitables['other']))
    lst.append(pickone(vage_cook) + pickone(vagitables['mushroom']))
    meal = '-'.join(lst)
    print(meal)

    return meal


if __name__ == '__main__':
    meal_lst = []
    meal = ''
    for i in range(14):
        meal = generate_meal()
        while meal in meal_lst:
            meal = generate_meal()
        meal_lst.append(meal)
