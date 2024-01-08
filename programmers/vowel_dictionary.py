def solution(word):
    answer = 0
    order = 0
    alphabets = ["A","E","I","O","U"]
    
    def traverse(cur_word):
        nonlocal answer
        nonlocal order
        
        if len(cur_word) > 5:
            return
        if cur_word == word:
            answer = order
            return

        order += 1

        for i in range(5):
            traverse(cur_word + alphabets[i])
            if answer:
                return
    
    traverse('')
    return answer