import pandas as pd
import requests


class ParliamentDataRetriever:
    # def __init__(self, url):
    #     self.url = url
    def extract_pdf_url(url):
        data = requests.get(url).json()
        return data["versions"][0]['file']['url']
    
    def get_pmg_bills_data():
        url = "http://api.pmg.org.za/bill/"
        try:
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()
            data_ = data.get('results', [])
            title_list= []
            status_list= [] 
            owner_list = []
            date_list = []
            update_date_list = []
            url_list = []     
            for d in data_:  # Displaying the 5 most recent
                title = d.get('title')
                owner = d.get('introduced_by')
                date = d.get('created_at')
                update = d.get('updated_at')
                url = d.get('url')
                if d.get('status') is None:
                    status = {"description": "No status available"}
                else:
                    status = d.get('status')
                title_list.append(title)
                status_list.append(status['description'])
                owner_list.append(owner)
                date_list.append(date)
                update_date_list.append(update)
                url_list.append(url)
            df = pd.DataFrame({'Title': title_list, 'Status': status_list, 
                            'Introduced by': owner_list, 'Created at': date_list, 
                            'Updated at': update_date_list, 'URL': url_list})
            df_check_dup = df.duplicated(subset=['Title'], keep=False)
            df_check_no_status =(df['Status'] == 'No status available')
            # Make an explicit copy to avoid SettingWithCopyWarning when assigning new columns
            df_cleaned = df[~(df_check_dup & df_check_no_status)].copy()
            for i in range(len(df_cleaned)):
                try:
                    df_cleaned.loc[i, 'Document'] = ParliamentDataRetriever.extract_pdf_url(df_cleaned.loc[i, 'URL'])
                except KeyError:
                    df_cleaned.loc[i, 'Document'] = "No document available"
            return df_cleaned
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

if __name__ == "__main__":
    pass