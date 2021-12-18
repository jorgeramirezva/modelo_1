import pandas as pd
import streamlit as st
import pickle

modelo_cargado = pickle.load(open('modelo_rf.pkl', 'rb'))

#st.title('Modelo de prediccion de valor de cliente') 
#st.text('Este modelo determina el valor de un cliente a partir de algunas caracteristicas obserbadas')

add_selectbox = st.sidebar.selectbox(' ', ('Pagina principal', 'Modelo Batch', 'Modelo csv'))

match add_selectbox:
    case 'Pagina principal':
            st.image('cliente.png')
            st.title('Modelo de prediccion del valor de cliente')
            st.text('Este modelo determina el valor de un cliente')

    case 'Modelo Batch':
        st.title('Aqui puede realizar la prediccion de cada')
        Age = st.number_input('Ingrese aqui la edad', min_value=18, max_value=99, value=45)
        compras = st.number_input('Ingrese el numero de compras promedio en el mes', min_value=0, max_value=150, value=10)
        gasto = st.number_input('Ingrese el gasto promedio del cliente en el mes', min_value=0, max_value=2000, value=20)
        Recency = st.number_input('Numero de dias dede que el cliente no realiza otra transaccion', min_value=0, max_value=365, value=90)
        Income = st.number_input('Salario anual del cliente', min_value=15000, max_value=200000, value=38000)
        input_dict = {'Age':Age, 'compras':compras, 'gasto':gasto, 'Recency':Recency, 'Income':Income}
        input_df = pd.DataFrame([input_dict])

        if st.button('Prediccion'):
            salida = modelo_cargado.predict(input_df)
            output1 = int(salida)
            st.success(output1)
            match output1:
                case 0:
                    st.success('Este cliente es de: Muy Alto Valor')
                case 1:
                    st.success('Este cliente es de: Bajo Valor')
                case 2:
                    st.success('Este cliente es de: Mediano Valor')
                case 3:
                    st.success('Este cliente es de: Alto Valor')

    case 'Modelo csv':
        st.title('Modelo csv')
        archivo_cargado = st.file_uploader('Ingrese aqui el archivo a predecir',type=['csv','CSV'])
        if archivo_cargado is not None:
            data_a_predecir = pd.read_csv(archivo_cargado, sep=';')
            #data_a_predecir.head()
            #data_a_predecir = pd.read_csv(archivo_cargado)
            data_a_predecir['Prediccion'] = modelo_cargado.predict(data_a_predecir)
            st.write(data_a_predecir)   

