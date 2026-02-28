import streamlit as st
import pandas as pd
from urllib.parse import quote_plus


def main():
    # Ensure session state exists (if you add login later it can populate this)
    if 'user' not in st.session_state:
        st.session_state['user'] = None

    st.title("Parliament Monitoring Dashboard")

    tab_prev, tab_cur = st.tabs(["Previous Snapshot", "Current Data"])

    with tab_prev:
        st.subheader("Previous snapshot")
        try:
            with open('old_data.json', 'r') as f:
                old_data = pd.read_json(f, orient='records', lines=True)
            old_data = old_data[['Title', 'Status', 'Introduced by', 'Created at', 'Updated at', 'Document']]
            def make_url(val: str) -> str:
                s = str(val)
                if not s:
                    return ""
                if s.startswith('http://') or s.startswith('https://'):
                    return s
                return f"https://www.google.com/search?q={quote_plus(s)}"

            # Create clickable link column
            # old_data["clickable_link"] = old_data["Document"].apply(make_url)

            st.write(f"Loaded {len(old_data)} records")

            st.dataframe(
                old_data,
                column_config={
                    "Document": st.column_config.LinkColumn(
                        "Document Link",
                        display_text="Open"
                    )
                },
                use_container_width=True,
            )

        except FileNotFoundError:
            st.warning("No previous snapshot found (old_data.json missing).")
        except Exception as e:
            st.error(f"Failed to load previous snapshot: {e}")

    with tab_cur:
        st.subheader("Current Data")
        st.write("Current run / dashboard content goes here.")


if __name__ == "__main__":
    main()
