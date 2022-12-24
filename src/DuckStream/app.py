# App test
import duckdb, pandas as pd, streamlit as st

def app():
    # App layout
    st.set_page_config(layout="wide")
    
    # Data connection
    conn = duckdb.connect(database='../../data\sport\TennisSlamData.duckdb', read_only=True)

    # App content
    st.header('DuckStream App')
    st.markdown('---\n')

    # Sidebar filters
    st.sidebar.title('App Controls')
    st.sidebar.markdown('---\n')

    events = {'Australian Open': 'ausopen', 'Roland Garros': 'frenchopen', 'Wimbledon': 'wimbledon', 'US Open': 'usopen'}
    tournaments = st.sidebar.multiselect(label='Tournament', options=events.keys())
    years = st.sidebar.multiselect(label='Year', options=[i for i in range(2011, 2022)])
    dataset = st.sidebar.selectbox(label='Dataset', options=['matches', 'points'])
    
    # Dataset
    for yr in years:
        for n, tourny in enumerate(tournaments):
            if n == 0:
                data = conn.execute(f'''SELECT * FROM {events[tourny]}_{yr}_{dataset};''').fetch_df()
            else:
                data = pd.concat([data, conn.execute(f'''SELECT * FROM {events[tourny]}_{yr}_{dataset};''').fetch_df()])

    st.dataframe(data=data)

    # Charts
    # plot_data = pd.concat([data['player']])


if __name__ == '__main__':
    app()