left_list = [76569, 38663, 60350, 35330, 88681]
right_list = [66648, 66530, 60777, 13469, 66648]

if __name__ == '__main__':
    left_list.sort()
    right_list.sort()
    total_similarity_score = 0
    similarity_score = {}
    for i in left_list:
        for j in right_list:
            if i == j:
                similarity_score[i] = j if i not in similarity_score else similarity_score[i] + j

    print(sum(similarity_score.values()))
