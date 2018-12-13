import pandas as pd


from DataReader import *
from piiFeaturesUtil import *

input_file_path = 'D:\\python_examples\\PII_DATA\\files\\'

output_field =['has_dot','dot_count','is_ip_pattern','has_no_alpha','is_numeric','field_len','is_ip_in_range','has_at','domain_sep_count','has_dot_aft_at','is_min_len','is_email_pattern','has_hyphen','has_bracket','has_curley_bracket','is_alpha_num','is_hexa_decimal','is_guid_pattern','has_plus','is_num_in_range','label']

def prepareData(inputFilePath):
        total_row_list = list()
        reader = DataReader()
        df = reader.mergeData(inputFilePath)
        print(df.columns.values)
        cols = df.columns.values
        print(df.head())
        for eachColName in cols:
            feature_data = df[eachColName]
            feature_data = feature_data[feature_data.notnull()]
            for colData in feature_data:
                each_row = generate_feature_list(colData, eachColName)
                total_row_list.append(each_row)
        features_df = pd.DataFrame(total_row_list, columns=output_field)
        return (cols, features_df)

def generate_feature_list(data,colName):

        return (has_dot(data),
        dot_count(data),
        is_ip_pattern(data),
        has_no_alpha(data),
        is_numeric(data),
        get_field_length(data),
        is_ip_in_range(data),
        has_at(data),
        domain_sep_count(data),
        has_dot_aft_at(data),
        is_min_len(data),
        is_email_pattern(data),
        has_hyphen(data),
        has_bracket(data),
        has_curley_brackets(data),
        is_alpha_num(data),
        is_hexa_decimal(data),
        is_guid_pattern(data),
        has_plus(data),
        is_num_in_range(data),
        colName)



def main():
    print("Main")
    cols, features_df = prepareData(input_file_path)

    print(features_df.head())


if __name__ == '__main__':
    main()