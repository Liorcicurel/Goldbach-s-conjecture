
def parse_primes(filename):
    infile = open(filename, "r")
    set_1 = set()
    for line in infile:
        line_number = line.split()
        for num in line_number:
            set_1.add(int(num))
    infile.close()
    return set_1

def check_goldbach_for_num(n, primes_set):
    for m in primes_set:
        if n-int(m) in primes_set:
            return True
    return False

def check_goldbach_for_range(limit, primes_set):
    if limit == 3:
        return True
    else:
        for a in range(4,limit,2):
            check_goldbach_for_num(a,primes_set)
            if check_goldbach_for_num(a,primes_set) is False:
                return False
    return True


def check_goldbach_for_num_stats(n, primes_set):
    cnt=0
    for item in primes_set:
        if n-int(item) in primes_set:
            cnt+=1
            if n-int(item) == int(item):
                cnt+=1
    return int(cnt/2)


def check_goldbach_stats(limit, primes_set):
    dict_prime = {}
    for pair in range(4,limit,2):
        dict_num_pair = check_goldbach_for_num_stats(pair,primes_set)
        if dict_num_pair in dict_prime.keys():
            dict_prime[dict_num_pair] +=1
        else:
            dict_prime[dict_num_pair]= 1
    return dict_prime