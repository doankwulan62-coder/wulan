import streamlit as st

st.title("🎈 aplikasi ankim kalcer")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.markdown("*wulan"" is **really** **kalcer***.")
st.markdown('''
    :red[wulan] :orange[tek lan] :green[lan] :blue[wul] :violet[etek]
    :gray[laan] :rainbow[sen] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
