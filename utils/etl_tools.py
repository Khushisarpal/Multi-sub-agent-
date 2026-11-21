import os 
import requests
import pandas as pd
class ETLTools:
    def init__(self):
        pass
    def extract_load(self, url:str, output_folder:str, format:str):
        """
        This tool extracts the data from the API (url) and loads it into the desired location (destination).
        Args:
            url (str): The API endpoint to extract data from.
            output_folder (str): The folder path where the extracted data will be saved.
        Returns:
         str: A message indicating the success or failure of the operation.
        """

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        output_folder = os.path.join(project_root, 'output_folder')

        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()
            file_name = os.path.join(output_folder, f"extracted_data.{format}")
            os.makedirs(output_folder, exist_ok=True)

            df =pd.json_normalize(data['results'])
            if format == "csv":
                df.to_csv(file_name, index=False)
            elif format == "json":
                df.to_json(file_name, orient='records', lines=True)
            elif format == "parquet":
                df.to_parquet(file_name, index=False)
            else:
                return f"Unsupported format: {format}. Please use 'csv' or 'json'."
            return f"Data extracted from {url} and saved to {file_name} in {format} format."
        except requests.execptions.RequestException as e:
            return f"Error extracting data from {url}: {e}"
        except Exception as e:
            return f"Error saving data to {file_name}: {e}"



    def transform_load_context(self, file_path:str):
        """
        This tool transforms the data from the input file and saves it into the desired location (destination).
        Args:
            file_path (str): The path to the input file to transform.
            output_folder (str): The folder path where the transformed data will be saved.
            output_format (str): The format in which to save the transformed data(e.g., 'csv', 'json', 'parquet'))
        Returns:
         str: A message indicating the success or failure of the operation.
        """
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == ".csv":
            df = pd.read_csv(file_path)
        elif file_extension == ".json":
            df = pd.read_json(file_path, lines=True)
        elif file_extension == ".parquet":
            df = pd.read_parquet(file_path)
        else:
            return f"Unsupported input file format: {file_extension}. Please use 'csv', 'json', or 'parquet'."
        top_3_rows = str(df.head(3))
        return top_3_rows

    def execute_code(self, code:str):

        """
            This tool executes the provided Python code and returns the output.
            Args:
                code (str): The Python code to execute.
            returns:
                str: The output of teh executed code or an error message if the execution fails 
        
        """
        try:
            exec(code)
            return "code executed successfully"
        except Exception as e:
            return f"failed to  execute code: {e}"
        
    






if __name__ == "__main__":
    obj = ETLTools()
    path ="D:\\Sexy laptop Data\\all data\\data agent\\output_folder\\extracted_data.csv"
    print (obj.transform_load_context(path))