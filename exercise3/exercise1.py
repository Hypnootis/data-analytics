import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
plt.clf()
sns.violinplot(data=penguins, y="body_mass_g", x="species", hue="sex")
plt.figure()