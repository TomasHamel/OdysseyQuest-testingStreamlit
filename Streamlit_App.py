import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.header('Streamlit : build and share data apps')

st.caption('by Tomas H.')

st.subheader('Cars Dataset')
st.caption("@ https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
cars = pd.read_csv(link)
st.dataframe(cars)

st.subheader('Distribution Charts')


# Mise en oeuvre & implémentation de la selectbox

continent = cars['continent'].unique()
selected_continent = st.multiselect('Select your(s) continent(s)', continent, default=cars['continent'].unique()[0])
mask_continent = cars['continent'].isin(selected_continent)


# Représentation graphique - Distribution des variables par continents

fig1, ax = plt.subplots(figsize = (20, 20))

ax1 = plt.subplot(421)
sns.kdeplot(data=cars[mask_continent], x='mpg', hue='continent', fill=True, alpha=.5, linewidth=0)

ax2 = plt.subplot(422)
sns.kdeplot(data=cars[mask_continent], x='cylinders', hue='continent', fill=True, alpha=.5, linewidth=0)

ax3 = plt.subplot(423)
sns.kdeplot(data=cars[mask_continent], x='cubicinches', hue='continent', fill=True, alpha=.5, linewidth=0)

ax4 = plt.subplot(424)
sns.kdeplot(data=cars[mask_continent], x='hp', hue='continent', fill=True, alpha=.5, linewidth=0)

ax5 = plt.subplot(425)
sns.kdeplot(data=cars[mask_continent], x='weightlbs', hue='continent', fill=True, alpha=.5, linewidth=0)

ax6 = plt.subplot(426)
sns.kdeplot(data=cars[mask_continent], x='time-to-60', hue='continent', fill=True, alpha=.5, linewidth=0)

ax7 = plt.subplot(427)
sns.kdeplot(data=cars[mask_continent], x='year', hue='continent', fill=True, alpha=.5, linewidth=0)

st.pyplot(fig1)


# Caractéristiques détaillées

st.subheader('Detailed Specifications')
st.table(cars[mask_continent].describe())

st.write("On observe que les distributions relatives aux voitures européennes & japonnaises sont globalement similaires, elles partagent de nombreuses caractéristiques communes")
st.write("Au contraire, les distributions relatives aux voitures américaines se démarquent grandement de par leurs variétés & leurs densités")

st.subheader('Cars distribution by continent')

col1, col2 = st.columns([3, 1])

with col1:
	fig2 = px.pie(cars, names='continent', width=400, height=400)
	fig2.update_traces(textposition='inside', textinfo='percent+label', showlegend=False)
	st.plotly_chart(fig2)

with col2:
	st.write(' ')
	st.table(cars['continent'].value_counts())

st.write("On notera par ailleurs une sur-représentation des voitures US")


# Correlation chart & table

st.subheader('Correlation Chart')

fig3, ax = plt.subplots(figsize = (8, 5))
sns.heatmap(cars.corr(), vmin=-1, vmax=1, center=0, linewidths=.5, cmap='vlag_r')
st.pyplot(fig3)

st.subheader('Correlation Table')
st.table(cars.corr())

st.write("A l'exception des variables 'time-to-60' & 'year', les autres variables sont plutôt fortement corrélées entre elles")

# st.subheader('Pairplot')
# Pairplot
# pairplot = sns.pairplot(cars, hue='continent')
# st.pyplot(pairplot)


# Scatterplot distribution

st.subheader('Scatterplot Distribution')

st.write("You can now choose your two variables, let's try !")

setting = cars.columns[:-1]

selected_setting_1 = st.selectbox('Choise your 1st variable', setting, help='You can try...')
selected_setting_2 = st.selectbox('Choise your 2nd variable', setting, help="Nooooo, don't choose !")

fig4 = px.scatter(cars, x=str(selected_setting_1), y=str(selected_setting_2), color='continent', size='hp', width=800, height=500)
st.plotly_chart(fig4)

st.subheader('This is the END !')
st.caption('My only friend, ...')
