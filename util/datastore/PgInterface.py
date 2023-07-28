import os
import sys
from sqlalchemy import create_engine
from pandas import DataFrame


class PgInterface:
    def __init__(self):
        try:
            # Get PostgreSQL connection details from environment variables
            self.engine = create_engine(f'postgresql://{os.environ.get("DATABASE_USER")}:{os.environ.get("DATABASE_PASSWORD")}@{os.environ.get("DATABASE_HOST")}:{os.environ.get("DATABASE_PORT")}/{os.environ.get("DATABASE_NAME")}', pool_size=10, max_overflow=20)
        except Exception as error:
            print("Error while connecting to PostgreSQL:", error, file=sys.stderr)

        
    def load_data(self, dataframe: DataFrame):
        try:
            # save df to postgres
            dataframe.to_sql(f'{dataframe.table_name}', self.engine, if_exists='replace', index=False)
            # add elapsed time to final print out
            print("Data imported successful", file=sys.stderr)
        except Exception as error:
            print("Data load error:", error, file=sys.stderr)

    
