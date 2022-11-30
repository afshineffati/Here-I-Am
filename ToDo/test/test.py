# data = [
#         {"title":"call mom", "priority":"medium", "date":"2022-11-28"},
#         {"title":"tax bill", "priority":"low", "date":"2022-11-20"},
#         {"title":"buy milk", "priority":"high", "date":"2022-11-27"},
#]

data = []

def load():
    with open('datafile.txt', mode='rt', encoding='utf-8') as infile:
        task = {}
        for line in infile:
            if line.strip() == '':
                data.append(task)
                continue
            (key, val) = line.split(':')
            task[key] = val.strip()
            

def save():
    with open('datafile.txt', mode='wt', encoding='utf-8') as outfile:
        for i in range(len(data)):
            for key, val in data[i].items():
                outfile.write(f'{key}:{val}\n')
            outfile.write('\n')
       

def main():
    load()

if __name__ == '__main__':
    main()