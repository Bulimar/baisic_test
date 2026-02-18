import array

def compress_numbers(mass):

    result = array.array('i', [mass[0]])
    
    for i in range(1, len(mass)):
        if mass[i] != mass[i-1]:
            result.append(mass[i])
    
    return result

if __name__ ==  '__main__':
    arr = array.array('i', [42])
    
    print(compress_numbers(arr))
    print(compress_numbers(arr))

    print(compress_numbers(arr))

    print(compress_numbers(arr))

    print(compress_numbers(arr))

    print(compress_numbers(arr))

    
