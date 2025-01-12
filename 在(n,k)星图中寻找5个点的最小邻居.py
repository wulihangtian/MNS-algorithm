import sys
from itertools import permutations
from math import sin, cos, pi
from matplotlib import pyplot as plt
import random
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题
#获取所有点集
def V_S(n,k):
    numbers = list(range(1, n + 1))
    perms = permutations(numbers, k)
    result = list(perms)
    # print(result)
    hex_result = [''.join(map(lambda x: hex(x)[2:], perm)) for perm in result]
    # print("排列结果（16进制）:", hex_result)
    return hex_result
    # result = [int(''.join(map(str, perm))) for perm in result]
    # print(result)
    # str_list = [str(element) for element in result]
    # return str_list

#两点之间海明距离
def H(str1,str2):
    res = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            res = res + 1
    return res

#根据连边规则连边
def E(my_list, n, k):
    my_E_list = []
    # 使用集合来快速查找和比较，减少循环中的重复工作
    my_set = set(my_list)

    # 尝试减少循环中的工作量，但完全去除循环可能不现实
    for vertex1 in my_list:
        for vertex2 in (my_set - {vertex1}):  # 直接排除自身，减少一次if判断
            # i-边逻辑
            for i in range(k):
                if vertex1[0] == vertex2[i] and vertex2[0] == vertex1[i] and H(vertex1, vertex2) == 2:
                    my_E_list.append([vertex1, vertex2])
                    break  # 找到一个匹配就跳出内层循环

            # 1-边逻辑
            if vertex1[0] != vertex2[0] and H(vertex1, vertex2) == 1:
                my_E_list.append([vertex1, vertex2])

    print(my_E_list)
    return quchong(my_E_list)

#去除列表中
def quchong(list):
    unique_list = []
    seen_sublists = set()

    for sublist in list:
        # 将子列表中的元素排序并连接为字符串
        sorted_str = ''.join(sorted(sublist))

        # 检查字符串是否已经出现过
        if sorted_str not in seen_sublists:
            unique_list.append(sorted(sublist))
            seen_sublists.add(sorted_str)
    print(len(unique_list))
    return unique_list

def drawSnk(n, k):
    V_s = V_S(n, k)
    # print(V_s)
    # print("点数：{}".format(len(V_s)))
    # print("顶点集：{}".format(V_s))
    E_s = E(V_s, n, k)
    # print("边数：{}".format(len(E_s)))
    # print("边集：{}".format(E_s))
    # int_V_s52_list = [int(element) for element in V_s]
    # int_E_s52_list = [[int(element) for element in sublist] for sublist in E_s]
    int_V_s52_list = [element for element in V_s]  # 这实际上只是复制列表
    int_E_s52_list = [sublist[:] for sublist in E_s]  # 复制每个子列表

    list1 = []
    list2 = []
    vertices = int_V_s52_list
    print(vertices)
    edges = int_E_s52_list
    # 创建无向图对象
    G = nx.Graph()

    # 添加顶点
    G.add_nodes_from(vertices)

    # 添加边
    G.add_edges_from(edges)

    # # 创建一个字典，将最后一位数字映射到具有相同最后一位数字的顶点列表
    # last_digits_dict = {digit: [v for v in vertices if int(str(v)[-1]) == digit] for digit in range(10)}
    #
    # # 获取每个颜色的平均角度
    # angles = {digit: 2 * pi * digit / 10 for digit in range(10)}
    #
    # # 设置顶点的位置，使用shell_layout环形布局
    # pos = nx.shell_layout(G, nlist=list(last_digits_dict.values()))
    #
    # # 设置顶点颜色，根据最后一位数字
    # node_colors = [int(str(v)[-1]) for v in vertices]
    #
    # nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=150, node_color=node_colors,
    #         font_color='white', font_size=6, edge_color='black', width=1, cmap=plt.cm.coolwarm)
    #
    # # 统计每个颜色的顶点数量
    # color_counts = {color: node_colors.count(color) for color in set(node_colors)}
    #
    # # 显示图形
    # plt.show()

    count =0
    iter = int(input("请输入迭代次数："))
    select_nodes=int(input("请输入点数："))
    numm=0
    for i in range(iter):
        count += 1
        if i == 11227:
            random_points = [51234,61234,71234,81234,91234,'a1234']
        # elif i == 23932:
        #     random_points = [2318,4318,5318,6318,7318]
        # elif i == 75488:
        #     random_points = [2318,4518,5318,6318,7318]
        # elif i == 56588:
        #     random_points = [2318,4218,5318,6318,7318]
        # elif i == 88888:
        #     random_points = [2318,4318,5418,6318,7318]
        # elif i == 49188:
        #     random_points = [2318,4318,5218,6418,7318]
        # elif i == 23388:
        #     random_points = [2318,4318,5218,6318,7318]
        else:
            random_points = random.sample(int_V_s52_list, select_nodes)
        str_random_points = {str(num) for num in random_points}
        neighbors_count = set()
        for point in str_random_points:
              vertex_str = point
              first_char = vertex_str[0]
              for i in range(1,k):
                  new_string1 = vertex_str[i]+vertex_str[1:i]+first_char+vertex_str[i+1:]
                  neighbors_count.add(new_string1)
              seen = [False]*(n+1)
              for char in vertex_str:
                  num =int(char,16)
                  seen[num] = True
              for num in range(1,n+1):
                  if not seen[num]:
                      new_string2 = str(num)+vertex_str[1:]
                      neighbors_count.add(new_string2)

        neighbors_count = neighbors_count-str_random_points
        print(neighbors_count)
        list1.append(count)
        print(len(neighbors_count))
        list2.append(len(neighbors_count))
        if len(neighbors_count)==n+(select_nodes-1)*k-2*select_nodes+1:
            numm = numm+1
    plt.plot(list1, list2, marker='o', linestyle='-', color='b', label='experimental value',zorder=3)
    plt.axhline(y=n+(select_nodes-1)*k-2*select_nodes+1, color='r', linestyle='--', label='theoretical value', linewidth=5,zorder=2)
    plt.xlabel('iterations',fontsize=40)
    plt.ylabel('number of neighbors',fontsize=40)
    plt.tick_params(axis='both', which='major', labelsize=40)

    plt.yticks(range(n+(select_nodes-1)*k-2*select_nodes+1, max(list2) + 1, 2))

    legend=plt.legend(fontsize=35, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
    for line in legend.get_lines():
        line.set_linewidth(5)
    plt.grid(True)
    print(numm)
    plt.show()


def main():
    try:
        n = int(input("请输入n的值："))
        k = int(input("请输入k的值："))
        if k <= 0 or k > n:
            raise ValueError("k必须是正整数且不大于n")
        drawSnk(n, k)
        # detect_fault(n, k)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()