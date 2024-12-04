left_list = [76569, 38663, 60350, 35330, 88681]
right_list = [66648, 66530, 60777, 13469, 66648]

if __name__ == '__main__':
    left_list.sort()
    right_list.sort()
    total_distance = 0
    similarity_score = 0
    similarities = {}
    for i in range(0, len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
        similarities[left_list[i]] = right_list if left_list[i] not in similarities else similarities[left_list[i]] + right_list
        
    print(total_distance)
