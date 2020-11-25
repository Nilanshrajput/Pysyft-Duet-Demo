import streamlit
import streamlit as st


st.title('Data Marketplace For Privacy Preserving AI')


action_list = [
	"MNIST",
	"Cancer Dataset",
	"Stock Data",
]
action_st=0
demo_options = st.checkbox("Show Available Datasets")
if demo_options:
	action_st = st.selectbox(
		"",
		action_list,
		
	)

def access_req():
    url = """
            import syft as sy
            duet = sy.duet("7de28b338b90345508a97d31bee7d0ae")
    """
    return url

if action_st:
    if st.button('Request access'):
        streamlit.text(" Run the following script to connect")
        url = access_req()
        streamlit.text(url)


from bokeh.models.widgets import Div
    

url = "https://colab.research.google.com/drive/1ZEOVpEawUySkJiid1Q5U_9kDnu5Cmw4c?usp=sharing"
if st.button('Open Playground'):
    js = "window.open('https://colab.research.google.com/drive/1ZEOVpEawUySkJiid1Q5U_9kDnu5Cmw4c?usp=sharing')"  # New tab or window
    js = "window.location.href = 'https://colab.research.google.com/drive/1ZEOVpEawUySkJiid1Q5U_9kDnu5Cmw4c?usp=sharing'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)