import numpy as np


# 定义一个函数用于计算物品相似度
def item_similarity(data):
    # 计算每两个物品之间的共同用户数
    cooccur = np.zeros((len(data[0]), len(data[0])))
    for user in data:
        for i in range(len(user)):
            if user[i] == 1:
                cooccur[i, i + 1:] += user[i + 1:]
    cooccur += cooccur.T

    # 计算每两个物品之间的相似度（余弦相似度）
    similarity = np.zeros((len(data[0]), len(data[0])))
    for i in range(len(data[0])):
        for j in range(i, len(data[0])):
            similarity[i, j] = np.dot(data[:, i], data[:, j]) / (
                        np.linalg.norm(data[:, i]) * np.linalg.norm(data[:, j]))
    similarity += similarity.T

    return similarity


# 定义一个函数用于进行基于物品的推荐
def item_based_recommend(data, similarity, user_index, k):
    # 找到该用户未评分的物品
    unrated_items = np.where(data[user_index, :] == 0)[0]
    # 计算每个未评分物品与该用户已评分物品的相似度加权分数
    scores = np.zeros(len(unrated_items))
    for i, item in enumerate(unrated_items):
        relevant_items = np.where(data[:, item] == 1)[0]
        scores[i] = np.sum(similarity[item, relevant_items])
    # 找到前k个相似度最高的物品
    top_items = unrated_items[np.argsort(-scores)[:k]]
    return top_items
