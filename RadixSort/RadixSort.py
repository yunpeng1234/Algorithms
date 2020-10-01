def radix_sort(xs) :

    def counting_sort_radix(xs, base) :

        counts = {}
        for idx in range(10) :
            counts[idx] = [0,[]]

        for idx in range(len(xs)) :
            base_val = int(xs[idx] / base) % 10
            counts[base_val][0] += 1
            counts[base_val][1].append(xs[idx])

        for count in range(1, 10) :
            counts[count][0] += counts[count - 1][0]

        xs = [None for x in xs]

        for count in range(10) :
            if counts[count][0] != 0 :
                for i in range(counts[count][0]) :
                    if xs[i] == None :
                        xs[i] = counts[count][1].pop(0)
        return xs

    max_val = max(xs)
    num_bases = 1
    while max_val > 1 :
        num_bases += 1
        max_val /= 10

    for bases in range(num_bases) :
        base = 10 ** bases
        xs = counting_sort_radix(xs, base)

    return xs
