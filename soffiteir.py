from datetime import date
from datetime import datetime
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from matplotlib import pyplot as plt
import streamlit as st

# SITO PER LE EMOJI UTILIZZATE
# https://emojifinder.com/


####################
##### SET PAGE #####
####################

st.set_page_config(
    layout="centered", page_title="La dashboard chat Soffiteir", page_icon="data:image/jpeg;base64,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"
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 300px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 300px;
        margin-left: -300px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#########################
##### IMPORTO IL DF #####
#########################

@st.experimental_memo
def get_data():
    dati = pd.read_excel('df_soffiteir.xlsx')
    return dati

df = get_data()


##########################
##### CREAZIONE KPIs #####
##########################

@st.experimental_memo
def num_mex_totali():
    """
    numero di messaggi totali inviati nella chat
    """

    tot_mex = df.qta_mex.sum()

    return tot_mex

@st.experimental_memo
def num_giorni_chat():
    """
    numero di giorni da quando esiste la chat. Usa today e sottrae la data del primo messaggio
    """

    min_day = min(df.day)
    min_day = min_day.strftime("%d/%m/%Y")
    min_day = datetime.strptime(min_day, "%d/%m/%Y")

    today = date.today()
    today = today.strftime("%d/%m/%Y")
    today = datetime.strptime(today, "%d/%m/%Y")

    return (today - min_day).days

@st.experimental_memo
def num_giorni_chat_reali():
    """
    numero di giorni da quando esiste la chat. Considera il giorno dell'ultimo messaggio caricato
    """

    min_day = min(df.day)
    min_day = min_day.strftime("%d/%m/%Y")
    min_day = datetime.strptime(min_day, "%d/%m/%Y")

    max_day = max(df.day)
    max_day = max_day.strftime("%d/%m/%Y")
    max_day = datetime.strptime(max_day, "%d/%m/%Y")

    return (max_day - min_day).days

@st.experimental_memo
def dado_ghost_friend():
    """
    numero dei giorni in cui Dado ci ha ghostati. Numero di giorni in cui è stato taggato o menzionato
    almeno 1 volta e non ha mandato neanche un messaggio.
    """

    df_pivot_dado = pd.pivot_table(df, values=['qta_dado_mex', 'dado_tag'], index='day', aggfunc='sum')
    df_pivot_dado = df_pivot_dado[(df_pivot_dado['dado_tag'] > 0) & (df_pivot_dado['qta_dado_mex'] == 0)]
    num_giorni_ghosted = len(df_pivot_dado)

    return num_giorni_ghosted

@st.experimental_memo
def giorno_max_messaggi():
    """
    il giorno con il maggior numero di messaggi
    """

    x = df.groupby(by='day')['qta_mex'].sum()
    giorno = x.idxmax(axis=0)
    giorno = giorno.strftime("%d/%m/%Y")
    num_max = x.max()

    giorno_max = [giorno, num_max]

    return giorno_max

################################
##### CFREAZIONE SIDE BAR ######
################################

option = st.sidebar.selectbox('Seleziona la pagina', ('Home page', 'Insights'))


####################
##### HOMEPAGE #####
####################

st.header(option)
st.markdown('#')

if option == 'Home page':

    # CREAZIONE OGGETTI VISIVI KPIs
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="💬 Messaggi totali", value=num_mex_totali())
    kpi2.metric(label="🗓️ Giorni di vita della chat", value=num_giorni_chat())
    kpi3.metric(label="👻 N° di volte che Dado ci ha ghostati", value=dado_ghost_friend())

    st.markdown('---')

    # CREAZIONE GRAFICO ANDAMENTO MESSAGGI
    st.title("Andamento messaggi inviati")
    st.write(f'Il grafico mostra l\'andamento dei messaggi inviati da quando esiste la chat. Si può notare come, dopo un picco iniziale avvenuto in corrispondenza dell\'inizio della pandemia, il numero sia sensibilmente diminuito, assestandosi successivamente attorno a {int(num_mex_totali()/num_giorni_chat_reali())} messaggi medi giornalieri.')

    andamento = df.groupby(by='day')['qta_mex'].sum()
    fig = px.line(andamento, labels={'value': 'Numero messaggi inviati', 'day': 'Periodo'})
    fig.update_layout(showlegend=False,
                      autosize=False,
                      width=800,
                      height=400)
    fig.update_traces(line_color='#ffd966')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.add_vline(x=datetime.strptime("2020-03-03", "%Y-%m-%d").timestamp() * 1000,
                  line_color="#f1c232",
                  line_dash="dot",
                  annotation_text="Inizio pandemia",
                  annotation_position="top right",
                  annotation_font_size=12,
                  annotation_font_color="#f1c232"
                  )
    fig.add_vline(x=datetime.strptime("2022-02-20", "%Y-%m-%d").timestamp() * 1000,
                  line_color="#f1c232",
                  line_dash="dot",
                  annotation_text="Inizio guerra Ucraina\Compleanno Poly",
                  annotation_position="top left",
                  annotation_font_size=12,
                  annotation_font_color="#f1c232"
                  )
    st.plotly_chart(fig)

    st.markdown('#')

    st.title("Distribuzione messaggi")
    st.write("Seleziona la tipologia di distribuzione da visualizzare. ")

    #row_space, col1, col2 = st.columns((.2, 2, 8))
    tipo_distr = st.selectbox('', ('Oraria', 'Settimanale', 'Mensile'), index=0)

    # CREAZIONE GRAFICO SCELTA DISTRIBUZIONE
    def get_plot_dist(tipo_distr):

        """
        funzione che crea grafico a barre in base alla tipologia di asse x selezionato
        Parametri ammessi: Oraria, Settimanale e Mensile
        hour = distribuzione oraria dei messaggi
        WDay = distribuzione settimanale
        month = distribuzione annuale in base ai mesi
        """

        if tipo_distr == 'Oraria':
            distrib_pers = df.groupby(by='hour')['qta_mex'].sum()
        if tipo_distr == 'Settimanale':
            distrib_pers = df.sort_values(['WDay_num']).groupby(by=['WDay_num', 'WDay_name'])['qta_mex'].sum()
            distrib_pers = distrib_pers.droplevel(level=0)
        if tipo_distr == 'Mensile':
            distrib_pers = df.groupby(by=['month_num', 'month_name'])['qta_mex'].sum()
            distrib_pers = distrib_pers.droplevel(level=0)

        distrib_pers = pd.DataFrame(distrib_pers)
        distrib_pers['%_qta_mex'] = round(distrib_pers.qta_mex / distrib_pers.qta_mex.sum() * 100, 1)

        fig = px.bar(x=distrib_pers.index,
                     y=distrib_pers['%_qta_mex'],
                     text=distrib_pers['%_qta_mex'].apply(lambda x: '{0:1.1f}%'.format(x)),
                     labels={'y': '% messaggi inviati', 'x': tipo_distr})
        fig.update_layout(showlegend=False,
                          autosize=False,
                          width=800,
                          height=400)
        fig.update_traces(marker_color='#ffd966')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        return fig

    st.plotly_chart(get_plot_dist(tipo_distr))

    # CREAZIONE GRAFICO CLASSIFICA MESSAGGI INVIATI PER MITTENTE
    st.title('Classifica inviatori')
    st.write(f'Di seguito viene mostrata la classifica in ordine decrescente dei messaggi inviati da ogni mittente.')

    classifica = df.groupby(by='from')['qta_mex'].sum().sort_values(ascending=True)
    fig = px.bar(classifica,
                 orientation='h',
                 text_auto='.2s',
                 labels={'from': 'Mittente', 'value': 'Numero messaggi inviati'})
    fig.update_layout(showlegend=False,
                      autosize=False,
                      width=500,
                      height=700)
    fig.update_traces(marker_color='#ffd966')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig)

    # CREAZIONE BUBBLE CHART
    st.title('Bubble chart')
    st.write(f'Il grafico mostra la media dei messaggi giornalieri, il numero medio di parole e la dimensione della bolla la lunghezza di ogni messaggio. Sull\'asse delle ascisse è evidenziato il quadrante di chi invia messaggi contenenti molte parole ed è stata indicata come "area degli spiegoni". Mentre sull\'asse delle ordinate è evidenziato il quadrante degli "spammatori" seriali.')

    spiegoni = df.pivot_table(index='from',
                              values=['qta_mex', 'number_words', 'lenght_mex', 'day'],
                              aggfunc={'qta_mex': np.sum, 'number_words': np.mean, 'lenght_mex': np.mean})

    spiegoni['avg_mex_day'] = round(spiegoni['qta_mex'] / num_giorni_chat_reali(), 1)
    spiegoni['number_words'] = round(spiegoni['number_words'], 1)
    spiegoni['lenght_mex'] = round(spiegoni['lenght_mex'], 1)

    fig = px.scatter(spiegoni,
                     x="number_words",
                     y="avg_mex_day",
                     size="lenght_mex",
                     color=spiegoni.index,
                     labels={'number_words': 'Parole per messaggio',
                             'avg_mex_day': 'Messaggi al giorno',
                             'lenght_mex': 'Lunghezza messaggi',
                             'from': 'Mittente'},
                     text=spiegoni.index)
    fig.update_layout(showlegend=False)
    fig.update_traces(textposition='top center')
    fig.update_traces(marker_color='#ffd966')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.add_trace(go.Scatter(
        x=[2],
        y=[15],
        text=["Spammer"],
        mode="text",
    ))
    fig.add_trace(go.Scatter(
        x=[17],
        y=[0.5],
        text=["Spiegoni"],
        mode="text",
    ))
    fig.add_trace(go.Scatter(
        x=[17],
        y=[15],
        text=["Male Puro"],
        mode="text",
    ))
    fig.add_vline(x=16,
                  line_width=1,
                  line_dash="dash",
                  line_color="green")
    fig.add_hline(y=14,
                  line_width=1,
                  line_dash="dash",
                  line_color="green")
    fig.add_shape(type='rect',
                  x0=16,
                  y0=14,
                  x1=18,
                  y1=16, line=None, fillcolor='red', opacity=0.1)
    st.plotly_chart(fig)



######################
###### INSIGHTS ######
######################

st.markdown('#')

if option == 'Insights':

    mittenti = list(df['from'].sort_values(ascending=True).unique())
    mittenti_select = st.sidebar.selectbox('Seleziona il mittente dei messaggi', mittenti, index=9)

    min_day = min(df.day)
    min_day = min_day.strftime("%d/%m/%Y")
    min_day = datetime.strptime(min_day, "%d/%m/%Y")

    max_day = max(df.day)
    max_day = max_day.strftime("%d/%m/%Y")
    max_day = datetime.strptime(max_day, "%d/%m/%Y")

    df['day'] = pd.to_datetime(df['day'])

    date_slider = st.sidebar.slider('Seleziona il periodo', value=(min_day,max_day))


    def num_mex_inviati(mittente):
        """
        mostra il numero di messaggi inviati dal mittente selezionato
        """

        tot_mex_inviati = df[(df['from'] == mittente) & (df['day'] >= date_slider[0]) & (df['day'] <= date_slider[1])].qta_mex.sum()

        return tot_mex_inviati

    col1, col2 = st.columns(2)
    col1.metric(label="💬 Messaggi totali", value=num_mex_inviati(mittenti_select))
    col2.metric(label="Hai selezionato:", value=mittenti_select)
    st.markdown('#')

    # GRAFICO ANDAMENTO MENSILE MESSAGGI

    st.title('Andamento mensile')


    def get_plot_andamento_mittente(mittenti_select):

        andamento_mittente = df[(df['from'] == mittenti_select) & (df['day'] >= date_slider[0]) & (df['day'] <= date_slider[1])].groupby(pd.Grouper(key='day', freq='M'))['qta_mex'].sum()
        fig = px.bar(andamento_mittente,
                     text_auto='.2s',
                     labels={'value': 'Numero messaggi inviati', 'day': 'Periodo'})
        fig.update_layout(showlegend=False,
                          autosize=False,
                          width=800,
                          height=400)
        fig.update_traces(marker_color='#ffd966')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        return fig

    st.plotly_chart(get_plot_andamento_mittente(mittenti_select))


    # GRAFICO DISTRIBUZIONE ORARIA MESSAGGI

    st.title('Distribuzione oraria')


    def get_plot_orario(mittenti_select):

        distrib_oraria = df[(df['from'] == mittenti_select) & (df['day'] >= date_slider[0]) & (df['day'] <= date_slider[1])].groupby(by='hour')['qta_mex'].sum()

        fig = px.bar(distrib_oraria,
                     text_auto='.2s',
                     labels={'value': 'Numero messaggi inviati', 'hour': 'Orario'},
                     height=400)
        fig.update_layout(showlegend=False,
                          autosize=False,
                          width=800,
                          height=400)
        fig.update_traces(marker_color='#ffd966')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        return fig

    st.plotly_chart(get_plot_orario(mittenti_select))


    # GRAFICO DISTRIBUZIONE ORARIA MESSAGGI

    st.title('Distribuzione settimanale')


    def get_plot_giorno(mittenti_select):

        distrib_giorno = df[(df['from'] == mittenti_select) & (df['day'] >= date_slider[0]) & (df['day'] <= date_slider[1])].groupby(by='WDay_name')['qta_mex'].sum()

        fig = px.bar(distrib_giorno,
                     text_auto='.2s',
                     labels={'value': 'Numero messaggi inviati', 'WDay': 'Giorno settimana'},
                     category_orders={
                         'WDay': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']},
                     height=400)
        fig.update_layout(showlegend=False,
                          autosize=False,
                          width=800,
                          height=400)
        fig.update_traces(marker_color='#ffd966')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        return fig

    st.plotly_chart(get_plot_giorno(mittenti_select))

    st.title('Tipologia di messaggi inviati')

    def get_plot_tipo_mex(mittenti_select):

        tipo_mex = df[(df['from'] == mittenti_select) & (df['day'] >= date_slider[0]) & (df['day'] <= date_slider[1])].groupby(by='media_type')['qta_mex'].sum()

        fig = px.bar(tipo_mex,
                     orientation='h',
                     labels={'media_type': 'Tipologia messaggio', 'value': 'Numero messaggi inviati'})
        fig.update_layout(showlegend=False,
                          autosize=False,
                          width=800,
                          height=400)
        fig.update_traces(marker_color='#ffd966')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        return fig

    st.plotly_chart(get_plot_tipo_mex(mittenti_select))

    st.markdown('#')