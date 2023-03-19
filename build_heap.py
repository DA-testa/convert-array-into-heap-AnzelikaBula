def heapify(data, j, i, swaps):
    
    
    smallest = i 
    right = 2 * i + 2     
    left = 2 * i + 1   
     
       

    if left < j and data[i] > data[left]:
        smallest = left

    if right < j and data[smallest] > data[right]:
        smallest = right

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        heapify(data, j, smallest, swaps)


def build_heap(data, j):
    swaps = []

    for i in range(j // 2, -1, -1):
        heapify(data, j, i, swaps)

    return swaps


def main():
    try:
        text = input("Enter I or F:  ")
        
        if text.startswith('I'):
            n = int(input("digit: "))
            data = list(map(int, input().split()))
        elif text.startswith('F'):
            filename = "tests/" + input("Fails: ")
            with open(filename, "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))

        assert len(data) == n

        swaps = build_heap(data, n)

        print(len(swaps))
        
        for a, b in swaps:
            print(a, b)
            
    except Exception as e:
        
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main()