import streamlit as st
from anneal import *

# メイン画面の作り込み
"# エネルギー使用のスケジュール管理"
"## dimod大丈夫？"

st.sidebar.number_input("ステップ", value=3, step=1)
