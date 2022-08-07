from matplotlib import pyplot as plt
import matplotlib as mpl

plt.figure('Najduzi nezavisni niz')

group_3 = ['Annette Bening', 'Benedict Cumberbatch', 'Benicio Del Toro', 'Brie Larson', 'Bryan Cranston', 'Hailee Steinfeld', 'Jeffrey Wright', 'Josh Brolin', 'Leonardo DiCaprio', 'Michael Shannon', 'Michael Stuhlbarg', 'Natalie Portman', 'Robert Downey Jr']
group_4 = ['Adam Driver', 'Alicia Vikander', 'Allison Janney', 'Amy Adams', 'Andrew Garfield', 'Ben Foster', 'Ben Mendelsohn', 'Bob Odenkirk', 'Bradley Cooper', 'Carrie Coon', 'Cate Blanchett', 'Charlize Theron', 'Chiwetel Ejiofor', 'Chris Pine', 'Christian Bale', 'Claire Foy', 'Daniel Kaluuya', 'David Oyelowo', 'Denzel Washington', 'Emma Stone', 'Evan Rachel Wood', 'Frances McDormand', 'Gary Oldman', 'Gina Rodriguez', 'Hugh Jackman', 'Idris Elba', 'Jake Gyllenhaal', 'Janelle Monáe', 'Javier Bardem', 'Jennifer Lawrence', 'Jesse Plemons', 'Jessica Chastain', 'Joaquin Phoenix', 'Joel Edgerton', 'Jonah Hill', 'Julianne Moore', 'Kate Winslet', 'Keri Russell', 'Kumail Nanjiani', 'Kyle Chandler', 'LaKeith Stanfield', 'Letitia Wright', 'Lucas Hedges', "Lupita Nyong'o", 'Mahershala Ali', 'Margot Robbie', 'Marion Cotillard', 'Mark Ruffalo', 'Mark Rylance', 'Martin Freeman', 'Matt Damon', 'Matthew Rhys', 'Meryl Streep', 'Michael B. Jordan', 'Michael Fassbender', 'Michael Keaton', 'Michelle Williams', 'Naomie Harris', 'Nicole Kidman', 'Octavia Spencer', 'Oscar Isaac', 'Paul Dano', 'Rachel Weisz', 'Ralph Fiennes', 'Reese Witherspoon', 'Riz Ahmed', 'Robin Wright', 'Ryan Gosling', 'Sam Rockwell', 'Samuel L. Jackson', 'Saoirse Ronan', 'Sarah Paulson', 'Sterling K. Brown', 'Steve Carell', 'Taraji P. Henson', 'Tatiana Maslany', 'Tiffany Haddish', 'Tilda Swinton', 'Timothée Chalamet', 'Tom Cruise', 'Tom Hanks', 'Tom Hardy', 'Tom Hiddleston', 'Viola Davis', 'Will Smith', 'Woody Harrelson']

len_3 = len(group_3)
len_4 = len(group_4)

print(len_3, len_4)

groups = [group_3, group_4]
labels = []
for group in groups:
    string = ''
    for i, name in enumerate(group):
        if (i+1)%3 == 0:
            string+='\n'
        string += name + ', ' 
    labels.append(string)

ratios = [len_3, len_4]
print(ratios)

#labels = 'Annette Bening , Benedict Cumberbatch, Benicio Del Toro, \nBrie Larson, Bryan Cranston, Hailee Steinfeld, \nJeffrey Wright, Josh Brolin, Leonardo DiCaprio,\n Michael Shannon, Michael Stuhlbarg, Natalie Portman, \nRobert Downey Jr', group_4 = ['Adam Driver', 'Alicia Vikander', 'Allison Janney', 'Amy Adams', 'Andrew Garfield', 'Ben Foster', 'Ben Mendelsohn', 'Bob Odenkirk', 'Bradley Cooper', 'Carrie Coon', 'Cate Blanchett', 'Charlize Theron', 'Chiwetel Ejiofor', 'Chris Pine', 'Christian Bale', 'Claire Foy', 'Daniel Kaluuya', 'David Oyelowo', 'Denzel Washington', 'Emma Stone', 'Evan Rachel Wood', 'Frances McDormand', 'Gary Oldman', 'Gina Rodriguez', 'Hugh Jackman', 'Idris Elba', 'Jake Gyllenhaal', 'Janelle Monáe', 'Javier Bardem', 'Jennifer Lawrence', 'Jesse Plemons', 'Jessica Chastain', 'Joaquin Phoenix', 'Joel Edgerton', 'Jonah Hill', 'Julianne Moore', 'Kate Winslet', 'Keri Russell', 'Kumail Nanjiani', 'Kyle Chandler', 'LaKeith Stanfield', 'Letitia Wright', 'Lucas Hedges', "Lupita Nyong'o", 'Mahershala Ali', 'Margot Robbie', 'Marion Cotillard', 'Mark Ruffalo', 'Mark Rylance', 'Martin Freeman', 'Matt Damon', 'Matthew Rhys', 'Meryl Streep', 'Michael B. Jordan', 'Michael Fassbender', 'Michael Keaton', 'Michelle Williams', 'Naomie Harris', 'Nicole Kidman', 'Octavia Spencer', Oscar Isaac, Paul Dano, Rachel Weisz, Ralph Fiennes, Reese Witherspoon, Riz Ahmed, Robin Wright, Ryan Gosling, Sam Rockwell, Samuel L. Jackson, Saoirse Ronan, Sarah Paulson, Sterling K. Brown, Steve Carell, Taraji P. Henson, Tatiana Maslany, Tiffany Haddish, Tilda Swinton, Timothée Chalamet, Tom Cruise, Tom Hanks, Tom Hardy, Tom Hiddleston, Viola Davis, Will Smith, Woody Harrelson'



explode = (0, 0.1)
colors = ['#0066cc', '#ff9933']

plt.rcParams.update({'font.size': 12})

plt.title('Najduzi nezavisni niz glumaca', size = 18)

plt.pie(ratios, colors = colors, labels = labels, shadow = True, startangle=150, explode=explode)
plt.legend(['3 glumca','4 glumca'], loc="upper right",)



plt.show()

