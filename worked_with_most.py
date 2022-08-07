def draw(pairs, scores):
    
    from matplotlib import pyplot as plt
    
    
    plt.style.use('seaborn-darkgrid')
    plt.rcParams.update({'font.size': 12})
    title = "Broj filmova u kojima su dva glumca radila zajedno"
    plt.title(title, fontsize = 16)    
    plt.barh(pairs, scores)
    plt.tight_layout()
    return plt.show()

if __name__ == '__main__':
    
    import pandas as pd
    df = pd.read_csv('top_100_1.csv')

    f = df.sort_values('weight').tail(29)

    scores = []
    pairs = []
    
    for i, row in f.iterrows():
        scores.append(row['weight']) 
        pairs.append(row['actor_1'] + ' & ' + row['actor_2'])

    
    draw(pairs, scores)
