import io
from pathlib import Path

import pandas as pd
import requests
import streamlit as st
import toml


def get_project_root() -> str:
    return str(Path(__file__).parent.parent.parent)


@st.cache()
def load_dataset(file) -> pd.DataFrame:
    try:
        return pd.read_csv(file)
    except:
        st.error(
            "This file can't be converted into a dataframe. Please import a csv file with ',' as a separator."
        )
        st.stop()


@st.cache()
def load_config(config_streamlit_filename: str, config_readme_filename: str):
    config_streamlit = toml.load(Path(get_project_root()) / f"config/{config_streamlit_filename}")
    config_readme = toml.load(Path(get_project_root()) / f"config/{config_readme_filename}")
    return config_streamlit, config_readme


@st.cache()
def download_toy_dataset(url: str) -> pd.DataFrame:
    download = requests.get(url).content
    df = pd.read_csv(io.StringIO(download.decode("utf-8")))
    return df