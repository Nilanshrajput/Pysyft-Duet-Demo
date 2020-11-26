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
            duet = sy.duet("76e601789f7161aa8e2c5fe2be9287d7")
    """
    return url

if action_st:
    if st.button('Request access'):
        streamlit.text(" Run the following script to connect")
        url = access_req()
        streamlit.text(url)


from bokeh.models.widgets import Div
    

url = "https://colab.research.google.com/github/Nilanshrajput/Pysyft-Duet-Demo/blob/master/mnist/MNIST_Syft_Data_Scientist.ipynb"
if st.button('Open Playground'):
    js = f"window.open({url})"  # New tab or window
    js = f"window.location.href = {url}"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)