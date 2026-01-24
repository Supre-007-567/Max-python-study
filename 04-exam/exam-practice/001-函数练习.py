#
# # 创建用户资料卡
# def create_profile(name, age, city='北京', hobby='阅读', **args):
#     # my_gender = args['gender'] if 'gender' in args else ''
#     return f"你好，我是{name}，今年{age}岁了，来自{city}，兴趣爱好是{hobby}，'性别'{args['gender'] if 'gender' in args else ''}"
#
#
# print(create_profile('胡歌', 20, '郑州', 'football', gender='男'))


# def analyze_numbers(my_list: list[int]) -> tuple[int, int | None, int | None]:
#     if len(my_list) == 0:
#         return 0, None, None
#
#     fn_even_count = 0
#     for num in my_list:
#         if num % 2 == 0:
#             fn_even_count += 1
#     fn_list_max = max(my_list)
#     fn_list_min = min(my_list)
#     re_tuple = (fn_even_count, fn_list_max, fn_list_min)
#     return re_tuple
#
#
# if __name__ == '__main__':
#     my_list = [1, 2, 3, 4, 5]
#     even_count, list_max, list_min = analyze_numbers(my_list)
#     print(f"偶数个数：{even_count}，最大值：{list_max}，最小值：{list_min}")


# my_str = '彭于晏'
# print(len(my_str))

def input_scores() -> dict[str, int]:
    score_dict: dict[str, int] = {}
    while True:
        stu_name = input("请输入学生姓名\n")
        if len(stu_name) == 0:
            print("结束成绩录入")
            break
        score = int(input("请输入学生成绩\n"))
        score_dict[stu_name] = score
    return score_dict


def calculate_stats(score_dict: dict[str, int]):
    # 空字典校验，避免报错
    if not score_dict:
        print("⚠️ 暂无成绩数据，无法统计！")
        return
    # 获取所有成绩值，简洁高效
    scores = list(score_dict.values())
    score_max = max(scores)
    score_min = min(scores)
    average = sum(scores) / len(scores)
    return {'average': average, 'max': score_max, 'min': score_min}


def query_score(score_dict: dict[str, int], name: str = ''):
    # 空数据校验
    if not score_dict:
        print("⚠️ 暂无成绩数据，无法查询！")
        return
    if not name:
        print('查询所有成绩成功：')
        return score_dict
    for item in score_dict:
        if item == name:
            print(f"查询{item}成绩成功：")
            return {item, score_dict[item]}


def main():
    score_dict = input_scores()
    count_dict = calculate_stats(score_dict)
    print(count_dict)
    query_result = query_score(score_dict, '')
    print(query_result)


if __name__ == '__main__':
    main()
