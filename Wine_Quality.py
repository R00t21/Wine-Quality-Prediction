import streamlit as st




st.title('Wine Quality')
st.image('images\wine.jpg')
st.header("un poco de historia sobre el vino")
add_selectbox = st.sidebar.selectbox(
    'Creators contact information:',
    ('Email', 'Mobile phone') 
)
add_write = st.sidebar.write(
    "Made with love by Somar and Royk"
)
st.write(
    "De acuerdo a diversos testimonios arqueológicos la historia del vino data del año 6000 a.c. donde, en la actual Armenia, se encontró una bodega para almacenar esta bebida."
    "Sin embargo, la documentación sobre el cuidado de la vid, cosecha y prensado de las uvas viene desde los griegos en el siglo VII a.c."
)
st.write(
    "El vino, tal como se conoce hoy en día, es una bebida alcohólica procedente de la fermentación del zumo de uva, la cual se produce gracias a la acción de las levaduras presentes en el hollejo de las uvas."
    "El nombre vino procede del latín vinum , que se cree que procede del griego oinos e incluso del sánscrito vêna ."
)
st.write(
    "La historia dicta que los fenicios fueron los creadores del vino, por tanto, los artífices del desarrollo del cultivo y elaboración del vino."
    "Además, introdujeron viñedos y bodegas en sus territorios en el Norte de África, Sicilia, Francia y España, donde popularizaron el vino y su comercio con griegos y romanos."
)
st.title('Sobre el proyecto:')
st.write(
    "Los dos dataset de la caludad del vino (wine quality) fue desarrollado en colaboracion con la compañía portoguesa (Vinho Verde)"
    "Usando las variantes del vino tinto y blanco de la misma compañía"
)
st.write(
    "La calidad del vino se determina según algunos parametros en específico los cuales son:"
    "Acidez fija, Acidez volátil, Ácido cítrico, Azúcar residual, Cloruros, Dióxido de azufre libre, Dióxido de azufre total, Densidad, pH, Sulfatos y el Alcohol"
    "Dependiendo de todos los parámetros mencionados anteriormente se define la calidad del vino ya sea blaco o tinto."
)
st.write(
    "Haciendo el uso de las ciencias del Machine Learning se ha logrado entrenar ambos datasets usando algorítmos de clasificación"
    "Con el modelo de Random Forest Classifier"
)

