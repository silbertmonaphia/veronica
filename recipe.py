import random
from typing import List, Dict

def pickone(items: List[str]) -> str:
    return random.choice(items)

def generate_meal(seen_meals: set) -> str:
    # Move these to module level constants to avoid recreation
    CARBO = ['米饭', '面条', '红薯', '紫薯', '豆腐']
    PROTEIN = ['虾', '鱼', '鸡', '猪', '牛']
    VEGETABLES = {
        'leaf': ['西生菜', '油麦菜', '菠菜', '菜心',
                '包菜', '白菜', '西洋菜', '茼蒿',
                '空心菜', '落葵', '芥菜', '芥兰',
                '番薯苗', '韭菜', '红苋'],
        'other': ['西兰花', '花椰菜', '西芹',
                '胡萝卜', '西红柿', '茄子',
                '苦瓜', '南瓜', '四季豆', '荷兰豆', 
                '白萝卜', '紫甘蓝', '莴笋', '芦笋(Asparagus)', 
                '竹笋', '丝瓜(Loofah)', '节瓜', '蒲瓜',
                '青瓜/黄瓜', '冬瓜', '西葫芦'],
        'mushroom': ['香菇', '平菇', '金针菇',
                    '木耳', '银耳', '虫草花',
                    '杏鲍菇', '猴头菇']
    }
    COOKING_METHODS = ['蒸', '煮', '炒', '煎', '炸', '烤']

    # Generate meal until we find a unique one
    while True:
        meal = '-'.join([
            pickone(COOKING_METHODS) + pickone(CARBO),
            pickone(COOKING_METHODS) + pickone(PROTEIN),
            pickone(COOKING_METHODS) + pickone(VEGETABLES['leaf']),
            pickone(COOKING_METHODS) + pickone(VEGETABLES['other']),
            pickone(COOKING_METHODS) + pickone(VEGETABLES['mushroom'])
        ])
        if meal not in seen_meals:
            return meal

def main():
    seen_meals = set()
    for _ in range(14):
        meal = generate_meal(seen_meals)
        seen_meals.add(meal)
        print(meal)

if __name__ == '__main__':
    main()
